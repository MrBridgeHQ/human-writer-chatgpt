#!/usr/bin/env python3
"""
human-writer / analyze.py — deterministic AI-tell detector.

httpx is permitted ONLY for --external detector POSTs.
It MUST NEVER be used to fetch the input text. Input comes from --input or stdin only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

RULES_PATH = Path(__file__).parent / "rules.yaml"

# Module-level httpx import: deferred to call sites because httpx is only
# permitted for outbound POSTs to explicitly configured external detector APIs.
# We import lazily inside the call_* helpers so that a missing httpx install
# does not break offline use of the analyzer.


def load_rules() -> dict:
    with RULES_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


IGNORE_REGION_RX = re.compile(
    # The start marker tolerates a trailing annotation (e.g. the reason for the
    # exemption) between the marker name and the closing `-->`.
    r"<!--\s*human-writer:ignore-start\b[^>]*-->.*?<!--\s*human-writer:ignore-end\b[^>]*-->",
    flags=re.DOTALL | re.IGNORECASE,
)
FENCED_CODE_RX = re.compile(r"```.*?```", flags=re.DOTALL)
# A markdown table row is a line whose content is pipe-delimited. This matches
# the header, the `| --- | --- |` separator, and every data row. Table cells are
# data, not prose, and would otherwise skew lexical diversity (many unique tokens)
# and burstiness (rows split oddly on sentence boundaries).
TABLE_ROW_RX = re.compile(r"^[ \t]*\|.*\|[ \t]*$\n?", flags=re.MULTILINE)


def strip_non_prose(text: str) -> str:
    """Remove non-prose regions before any detector runs.

    Honors the prose-only contract documented in references/adapter-technical.md:
    fenced code blocks, config samples, CLI examples, and data tables are not
    prose and must not be scored. Opt-in ignore regions let doctrine files quote
    intentionally AI-flavored bad examples without self-flagging. Ignore regions
    are stripped first so a fenced block nested inside one is removed as part of
    the region.
    """
    text = IGNORE_REGION_RX.sub("", text)
    text = FENCED_CODE_RX.sub("", text)
    text = TABLE_ROW_RX.sub("", text)
    return text


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def count_sentences(text: str) -> int:
    sentences = re.split(r"[.!?]+\s+", text.strip())
    return len([s for s in sentences if s.strip()])


def sentence_lengths(text: str) -> list[int]:
    sentences = re.split(r"[.!?]+\s+", text.strip())
    lengths = []
    for s in sentences:
        s = s.strip()
        if s:
            lengths.append(len(re.findall(r"\b\w+\b", s)))
    return lengths


def detect_sentence_stdev(text: str, threshold: float) -> dict:
    lengths = sentence_lengths(text)
    if len(lengths) < 2:
        stdev = 0.0
    else:
        mean = sum(lengths) / len(lengths)
        var = sum((x - mean) ** 2 for x in lengths) / len(lengths)
        stdev = var ** 0.5
    flag = stdev < threshold
    if stdev < threshold / 2:
        severity = "high"
    elif stdev < threshold:
        severity = "medium"
    else:
        severity = "low"
    return {
        "value": round(stdev, 2),
        "threshold": threshold,
        "flag": flag,
        "severity": severity,
    }


BULLET_RX = re.compile(r"^\s*[-*+]\s+(.+?)\s*$", flags=re.MULTILINE)
H2_RX = re.compile(r"^##\s+\S", flags=re.MULTILINE)
H3_RX = re.compile(r"^###\s+\S", flags=re.MULTILINE)


def detect_bullet_parallelism(text: str, threshold: float) -> dict:
    """Parallelism = max(ratio sharing first word, ratio sharing last word).
    AI lists often share either an opening verb or a repeated trailing noun phrase.
    """
    bullets = [b.strip() for b in BULLET_RX.findall(text) if b.strip()]
    if len(bullets) < 2:
        return {
            "value": 0.0,
            "threshold": threshold,
            "flag": False,
            "severity": "low",
            "bullet_count": len(bullets),
        }
    # Extract the first/last *word token* of each bullet. Using \b\w+\b (rather
    # than splitting on \W+) skips leading markdown markup such as **bold** or
    # _italic_, which would otherwise yield an empty first token and make every
    # markup-led bullet falsely share it (parallelism = 1.0).
    firsts = []
    lasts = []
    for b in bullets:
        toks = re.findall(r"\b\w+\b", b.lower())
        if toks:
            firsts.append(toks[0])
            lasts.append(toks[-1])
    first_ratio = Counter(firsts).most_common(1)[0][1] / len(firsts) if firsts else 0.0
    last_ratio = Counter(lasts).most_common(1)[0][1] / len(lasts) if lasts else 0.0
    ratio = max(first_ratio, last_ratio)
    flag = ratio >= threshold
    if ratio >= threshold + 0.1:
        severity = "high"
    elif ratio >= threshold:
        severity = "medium"
    else:
        severity = "low"
    return {
        "value": round(ratio, 3),
        "threshold": threshold,
        "flag": flag,
        "severity": severity,
        "bullet_count": len(bullets),
    }


def detect_header_pyramid(text: str) -> bool:
    """Pyramid = >=2 H2 blocks each containing exactly 3 H3s."""
    lines = text.splitlines()
    blocks: list[int] = []  # count of H3s in current H2 block
    current: int | None = None
    for line in lines:
        if re.match(r"^##\s+\S", line) and not line.startswith("###"):
            # H2 found
            if current is not None:
                blocks.append(current)
            current = 0
        elif re.match(r"^###\s+\S", line):
            if current is not None:
                current += 1
    if current is not None:
        blocks.append(current)
    pyramid_blocks = [b for b in blocks if b == 3]
    return len(pyramid_blocks) >= 2


def build_recommendations(tells: dict) -> list[dict]:
    recs: list[dict] = []
    styl = tells.get("stylistic", {})
    stat = tells.get("statistical", {})
    struct = tells.get("structural", {})

    em = styl.get("em_dash_count")
    if em and em.get("flag"):
        priority = "high" if em.get("severity") == "high" else "medium"
        recs.append({
            "priority": priority,
            "action": (
                f"Reduce em-dash usage: found {em.get('value')} em-dashes "
                f"({em.get('per_1000_words')} per 1000 words). Replace with commas, "
                "parentheses, or full sentences."
            ),
        })

    vocab = styl.get("suspect_vocabulary") or []
    if vocab:
        top = sorted(vocab, key=lambda v: -v.get("count", 0))[:5]
        words = ", ".join(f"{v['word']} (x{v['count']})" for v in top)
        recs.append({
            "priority": "high" if len(vocab) >= 4 else "medium",
            "action": f"Rewrite suspect vocabulary: {words}.",
        })

    constrs = styl.get("ai_constructions") or []
    if constrs:
        recs.append({
            "priority": "high" if len(constrs) >= 2 else "medium",
            "action": (
                f"Remove formulaic constructions ({len(constrs)} detected). "
                "Rephrase opener and closing sentences in your own voice."
            ),
        })

    sd = stat.get("sentence_length_stdev")
    if sd and sd.get("flag"):
        recs.append({
            "priority": "medium",
            "action": (
                f"Increase sentence-length variance (stdev={sd.get('value')}). "
                "Mix short punchy sentences with longer ones."
            ),
        })

    tr = stat.get("lexical_diversity_ttr")
    if tr and tr.get("flag"):
        recs.append({
            "priority": "low",
            "action": (
                f"Lift lexical diversity (TTR={tr.get('value')} < {tr.get('threshold')}). "
                "Avoid repeating the same nouns and verbs."
            ),
        })

    bp = struct.get("bullet_parallelism_ratio")
    if bp and bp.get("flag"):
        recs.append({
            "priority": "medium",
            "action": (
                f"Break bullet parallelism (ratio={bp.get('value')}). "
                "Vary bullet length, structure, and ending."
            ),
        })

    if struct.get("header_pyramid_detected"):
        recs.append({
            "priority": "medium",
            "action": "Break the header pyramid: collapse or merge symmetric H2/H3 blocks.",
        })

    priority_rank = {"high": 0, "medium": 1, "low": 2}
    recs.sort(key=lambda r: priority_rank.get(r["priority"], 3))
    return recs


def compute_score(tells: dict, weights: dict) -> int:
    """Composite AI-likelihood score in [0, 100], weighted by content-type."""
    stat = tells.get("statistical", {})
    styl = tells.get("stylistic", {})
    struct = tells.get("structural", {})

    # Statistical (max 30 raw)
    statistical_pts = 0
    sd = stat.get("sentence_length_stdev")
    if sd and sd.get("flag"):
        statistical_pts += 10
    tr = stat.get("lexical_diversity_ttr")
    if tr and tr.get("flag"):
        statistical_pts += 8

    # Stylistic (max 50 raw)
    stylistic_pts = 0
    em = styl.get("em_dash_count")
    if em and em.get("flag"):
        stylistic_pts += 15 if em.get("severity") == "high" else 8
    vocab = styl.get("suspect_vocabulary") or []
    vocab_total = sum(v.get("count", 0) for v in vocab)
    stylistic_pts += min(20, vocab_total * 3)
    constrs = styl.get("ai_constructions") or []
    constr_total = sum(c.get("count", 0) for c in constrs)
    stylistic_pts += min(10, constr_total * 3)
    tricolons = styl.get("tricolon_count", 0)
    if tricolons >= 3:
        stylistic_pts += 5

    # Structural (max 20 raw)
    structural_pts = 0
    bp = struct.get("bullet_parallelism_ratio")
    if bp and bp.get("flag"):
        structural_pts += 10
    if struct.get("header_pyramid_detected"):
        structural_pts += 10

    weighted = (
        statistical_pts * weights.get("statistical", 1.0)
        + stylistic_pts * weights.get("stylistic", 1.0)
        + structural_pts * weights.get("structural", 1.0)
    )
    return max(0, min(100, int(round(weighted))))


def verdict_for(score: int, bands: dict) -> str:
    for name, (lo, hi) in bands.items():
        if lo <= score <= hi:
            return name
    return "LOW_RISK"


TRICOLON_EN = re.compile(r"\b\w+,\s*\w+,?\s*and\s+\w+\b", flags=re.IGNORECASE)
TRICOLON_FR = re.compile(r"\b\w+,\s*\w+,?\s*et\s+\w+\b", flags=re.IGNORECASE)


def detect_tricolons(text: str, lang: str) -> int:
    pat = TRICOLON_EN if lang == "en" else TRICOLON_FR
    return len(pat.findall(text))


def _pattern_label(pat: str) -> str:
    """Human-readable label: collapse [' ’] apostrophe classes to a single '."""
    label = re.sub(r"\[['’]+\]", "'", pat)
    return label


def detect_ai_constructions(text: str, patterns: list[dict]) -> list[dict]:
    out = []
    for entry in patterns:
        pat = entry["pattern"]
        severity = entry.get("severity", "medium")
        try:
            rx = re.compile(pat, flags=re.IGNORECASE)
        except re.error:
            continue
        matches = list(rx.finditer(text))
        if matches:
            out.append({
                "pattern": _pattern_label(pat),
                "count": len(matches),
                "positions": [m.start() for m in matches],
                "severity": severity,
            })
    return out


def detect_suspect_vocab(text: str, vocab: list[str]) -> list[dict]:
    out = []
    for word in vocab:
        pat = re.compile(r"\b" + re.escape(word) + r"\b", flags=re.IGNORECASE)
        matches = list(pat.finditer(text))
        if matches:
            out.append({
                "word": word,
                "count": len(matches),
                "positions": [m.start() for m in matches],
            })
    return out


def detect_ttr(text: str, threshold: float) -> dict:
    words = [w.lower() for w in re.findall(r"\b\w+\b", text)]
    if not words:
        ttr = 0.0
    else:
        ttr = len(set(words)) / len(words)
    flag = ttr < threshold
    if ttr < threshold * 0.6:
        severity = "high"
    elif ttr < threshold:
        severity = "medium"
    else:
        severity = "low"
    return {
        "value": round(ttr, 3),
        "threshold": threshold,
        "flag": flag,
        "severity": severity,
    }


def detect_em_dashes(text: str, word_count: int, threshold: float) -> dict:
    count = text.count("—")
    per_1000 = (count / word_count * 1000.0) if word_count else 0.0
    flag = per_1000 > threshold
    if per_1000 > threshold * 2:
        severity = "high"
    elif per_1000 > threshold:
        severity = "medium"
    else:
        severity = "low"
    return {
        "value": count,
        "per_1000_words": round(per_1000, 2),
        "threshold": threshold,
        "flag": flag,
        "severity": severity,
    }


# ---------------------------------------------------------------------------
# External AI-detector providers (Copyleaks, GPTZero, Originality.ai)
#
# Constraint:
#   - httpx is permitted ONLY for these outbound POSTs.
#   - The INPUT TEXT must NEVER be fetched over HTTP by this script.
#     Input arrives via --input <file> or stdin; the orchestrator (Claude)
#     is responsible for fetching any URL with Firecrawl / Tavily / Exa MCP.
#
# Each call_<provider> returns either:
#   - {"ai_probability": float in [0.0, 1.0], "raw_response": dict}
#   - {"status": "skipped_no_key"}           — env var missing
#   - {"status": "error", "message": str}    — wrapped at dispatch level
#
# Endpoints below are the most likely current endpoints as of 2026-05.
# Verify against current provider docs before deploying — these APIs change.
# Unit tests mock call_<provider>, so they don't depend on the live API.
# ---------------------------------------------------------------------------

# Copyleaks uses a two-step auth (verified against docs.copyleaks.com 2026-06):
#   1. POST email+key to the login endpoint -> short-lived access_token (48h).
#   2. POST text to writer-detector/{scanId}/check with Authorization: Bearer.
# The detector response carries summary.ai (0..1) as the AI probability.
COPYLEAKS_LOGIN_ENDPOINT = "https://id.copyleaks.com/v3/account/login/api"
COPYLEAKS_ENDPOINT = "https://api.copyleaks.com/v2/writer-detector"
GPTZERO_ENDPOINT = "https://api.gptzero.me/v2/predict/text"
ORIGINALITY_ENDPOINT = "https://api.originality.ai/api/v1/scan/ai"
HTTP_TIMEOUT_S = 30.0


def _copyleaks_login(email: str, key: str) -> str:
    """Exchange (email, API key) for a short-lived access token.

    httpx is permitted ONLY for external detector POSTs. Split out as its own
    helper so call_copyleaks is unit-testable without touching the network.
    """
    import httpx
    resp = httpx.post(
        COPYLEAKS_LOGIN_ENDPOINT,
        json={"email": email, "key": key},
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        timeout=HTTP_TIMEOUT_S,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def _copyleaks_detect(token: str, text: str, scan_id: str, sandbox: bool = False) -> dict:
    """POST text to the writer-detector endpoint with a Bearer access token."""
    import httpx
    resp = httpx.post(
        f"{COPYLEAKS_ENDPOINT}/{scan_id}/check",
        json={"text": text, "sandbox": sandbox},
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        timeout=HTTP_TIMEOUT_S,
    )
    resp.raise_for_status()
    return resp.json()


def call_copyleaks(text: str, sandbox: bool = False) -> dict:
    """Run Copyleaks AI detection via its two-step auth flow.

    Requires BOTH COPYLEAKS_EMAIL and COPYLEAKS_API_KEY. Returns
    {ai_probability, raw_response} on success, or {status: "skipped_no_key"}
    if either credential is unset. With sandbox=True the API returns simulated
    results without consuming credits (used to smoke-test the flow).
    """
    key = os.environ.get("COPYLEAKS_API_KEY")
    email = os.environ.get("COPYLEAKS_EMAIL")
    if not key or not email:
        return {"status": "skipped_no_key"}
    token = _copyleaks_login(email, key)
    scan_id = os.urandom(8).hex()
    data = _copyleaks_detect(token, text, scan_id, sandbox=sandbox)
    summary = data.get("summary") or {}
    ai_prob = summary.get("ai")
    if ai_prob is None:
        # Defensive fallback if the response shape changes
        ai_prob = data.get("ai_probability") or 0.0
    return {"ai_probability": float(ai_prob), "raw_response": data}


def call_gptzero(text: str) -> dict:
    """POST text to GPTZero v2 predict endpoint.

    httpx is permitted ONLY for external detector POSTs (this function).
    Input text MUST NOT be fetched via HTTP — see module docstring.
    """
    key = os.environ.get("GPTZERO_API_KEY")
    if not key:
        return {"status": "skipped_no_key"}
    import httpx
    headers = {
        "x-api-key": key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {"document": text}
    with httpx.Client(timeout=HTTP_TIMEOUT_S) as client:
        resp = client.post(GPTZERO_ENDPOINT, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()
    # GPTZero shape (verify): documents[0].class_probabilities.ai
    docs = data.get("documents") or []
    ai_prob = 0.0
    if docs:
        cp = docs[0].get("class_probabilities") or {}
        ai_prob = cp.get("ai", 0.0)
        if not ai_prob:
            # Older shape: completely_generated_prob
            ai_prob = docs[0].get("completely_generated_prob", 0.0)
    return {"ai_probability": float(ai_prob), "raw_response": data}


def call_originality(text: str) -> dict:
    """POST text to Originality.ai AI scan endpoint.

    httpx is permitted ONLY for external detector POSTs (this function).
    Input text MUST NOT be fetched via HTTP — see module docstring.
    """
    key = os.environ.get("ORIGINALITY_AI_API_KEY")
    if not key:
        return {"status": "skipped_no_key"}
    import httpx
    headers = {
        "X-OAI-API-KEY": key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {"content": text}
    with httpx.Client(timeout=HTTP_TIMEOUT_S) as client:
        resp = client.post(ORIGINALITY_ENDPOINT, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()
    # Originality shape (verify): score.ai (0..1)
    score = data.get("score") or {}
    ai_prob = score.get("ai")
    if ai_prob is None:
        ai_prob = data.get("ai_score") or 0.0
    return {"ai_probability": float(ai_prob), "raw_response": data}


def call_external(text: str, provider: str) -> dict | None:
    """Dispatch to the chosen provider, wrapping all exceptions.

    Returns None for an unknown provider (caller can decide what to do).
    Returns the provider's dict otherwise, possibly with status="error".
    """
    dispatch = {
        "copyleaks": call_copyleaks,
        "gptzero": call_gptzero,
        "originality": call_originality,
    }
    fn = dispatch.get(provider)
    if not fn:
        return None
    try:
        return fn(text)
    except Exception as exc:  # noqa: BLE001 — intentional broad catch
        return {"status": "error", "message": str(exc)}


def analyze(text: str, lang: str, content_type: str) -> dict:
    rules = load_rules()
    lang_rules = rules[lang]
    thresholds = lang_rules["thresholds"]
    text = strip_non_prose(text)
    wc = count_words(text)
    sc = count_sentences(text)
    em_dash = detect_em_dashes(text, wc, thresholds["em_dash_per_1000_words"])
    stdev = detect_sentence_stdev(text, thresholds["sentence_stdev_min"])
    ttr = detect_ttr(text, thresholds["lexical_diversity_min"])
    suspects = detect_suspect_vocab(text, lang_rules.get("suspect_vocabulary") or [])
    constructions = detect_ai_constructions(text, lang_rules.get("ai_constructions") or [])
    tricolons = detect_tricolons(text, lang)
    bullet_par = detect_bullet_parallelism(text, thresholds["bullet_parallelism_max"])
    header_pyramid = detect_header_pyramid(text)
    tells = {
        "statistical": {"sentence_length_stdev": stdev, "lexical_diversity_ttr": ttr},
        "stylistic": {
            "em_dash_count": em_dash,
            "suspect_vocabulary": suspects,
            "ai_constructions": constructions,
            "tricolon_count": tricolons,
        },
        "structural": {
            "bullet_parallelism_ratio": bullet_par,
            "header_pyramid_detected": header_pyramid,
        },
    }
    weights = rules.get("content_type_weights", {}).get(content_type, {
        "statistical": 1.0, "stylistic": 1.0, "structural": 1.0,
    })
    score = compute_score(tells, weights)
    bands = rules.get("verdict_bands", {})
    verdict = verdict_for(score, bands)
    return {
        "language": lang,
        "content_type": content_type,
        "word_count": wc,
        "sentence_count": sc,
        "ai_probability_score": score,
        "verdict": verdict,
        "tells": tells,
        "recommendations": build_recommendations(tells),
        "_config": {
            "em_dash_threshold_per_1000_words": thresholds["em_dash_per_1000_words"],
        },
    }


def analyze_with_external(
    text: str,
    lang: str,
    content_type: str,
    external: str | None = None,
) -> dict:
    """Wrap analyze() and (if requested) attach an external_detector block.

    Backward-compatible: analyze() is unchanged; this is the function CLI uses.
    """
    result = analyze(text, lang, content_type)
    if external:
        ext = call_external(text, external)
        if ext is not None:
            result["external_detector"] = {"provider": external, **ext}
    return result


def render_human(result: dict) -> str:
    lines: list[str] = []
    lines.append("=" * 60)
    lines.append(f"  human-writer / analyze.py — {result.get('input_file', '<stdin>')}")
    lines.append("=" * 60)
    lines.append(
        f"Score: {result['ai_probability_score']}/100  →  {result['verdict']}  "
        f"({result['language']}, {result['content_type']})"
    )
    lines.append(
        f"Words: {result['word_count']}  |  Sentences: {result['sentence_count']}"
    )
    lines.append("")

    tells = result.get("tells", {})
    styl = tells.get("stylistic", {})
    stat = tells.get("statistical", {})
    struct = tells.get("structural", {})

    lines.append("-- Top tells -----------------------------------------------")
    em = styl.get("em_dash_count") or {}
    em_flag = "FLAG" if em.get("flag") else "ok"
    lines.append(
        f"em-dash      : {em.get('value', 0)} "
        f"({em.get('per_1000_words', 0)} per 1000 words)  [{em_flag}]"
    )
    sd = stat.get("sentence_length_stdev") or {}
    sd_flag = "FLAG" if sd.get("flag") else "ok"
    lines.append(
        f"sentence stdev: {sd.get('value', 0)}  threshold>={sd.get('threshold', 0)}  [{sd_flag}]"
    )
    tr = stat.get("lexical_diversity_ttr") or {}
    tr_flag = "FLAG" if tr.get("flag") else "ok"
    lines.append(
        f"TTR (lex div): {tr.get('value', 0)}  threshold>={tr.get('threshold', 0)}  [{tr_flag}]"
    )

    vocab = styl.get("suspect_vocabulary") or []
    if vocab:
        top = sorted(vocab, key=lambda v: -v.get("count", 0))[:5]
        joined = ", ".join(f"{v['word']} (x{v['count']})" for v in top)
        lines.append(f"vocab (top 5): {joined}")
    constrs = styl.get("ai_constructions") or []
    if constrs:
        top = sorted(constrs, key=lambda c: -c.get("count", 0))[:3]
        joined = " | ".join(f"{c['pattern']} (x{c['count']})" for c in top)
        lines.append(f"constructions: {joined}")

    tri = styl.get("tricolon_count", 0)
    lines.append(f"tricolons   : {tri}")
    bp = struct.get("bullet_parallelism_ratio") or {}
    if bp.get("bullet_count", 0):
        bp_flag = "FLAG" if bp.get("flag") else "ok"
        lines.append(
            f"bullets     : {bp.get('bullet_count')} items, "
            f"parallelism={bp.get('value', 0)} [{bp_flag}]"
        )
    if struct.get("header_pyramid_detected"):
        lines.append("headers     : pyramid detected [FLAG]")
    lines.append("")

    recs = result.get("recommendations") or []
    if recs:
        lines.append("-- Recommendations (top 5) ---------------------------------")
        for r in recs[:5]:
            lines.append(f"[{r['priority'].upper():6}] {r['action']}")
        lines.append("")

    ext = result.get("external_detector")
    if ext:
        lines.append("-- External detector --------------------------------------")
        provider = ext.get("provider", "?")
        if "ai_probability" in ext:
            ai_pct = round(float(ext["ai_probability"]) * 100, 1)
            lines.append(f"provider: {provider}  →  AI probability: {ai_pct}%")
        elif ext.get("status") == "skipped_no_key":
            lines.append(f"provider: {provider}  →  skipped (no API key set)")
        elif ext.get("status") == "error":
            lines.append(f"provider: {provider}  →  error: {ext.get('message')}")
        else:
            lines.append(f"provider: {provider}  →  {ext}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Deterministic AI-tell analyzer")
    p.add_argument("--input", type=Path, help="Input file (markdown/txt). Stdin if omitted.")
    p.add_argument("--lang", choices=["en", "fr"], required=True)
    p.add_argument("--type", dest="content_type",
                   choices=["marketing", "short-comms", "technical", "editorial-seo"],
                   required=True)
    p.add_argument("--external", choices=["copyleaks", "gptzero", "originality"])
    p.add_argument("--format", choices=["json", "human"], default="json")
    args = p.parse_args()

    text = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
    result = analyze_with_external(text, args.lang, args.content_type, external=args.external)
    result["input_file"] = str(args.input) if args.input else "<stdin>"

    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(render_human(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Status — lead-enrichment-engine

**Updated:** 2026-09-30 (PT)  
**Visibility:** public  
**Maturity:** scaffold / stalled  
**Trajectory:** sales-ops utility candidate; not productized

## What works (local)

- `pip install -e .` exposes console script `enrich-lead`
- `--help` documents single-lead, `--json`, and `--csv` modes
- Dependencies: `requests`, `httpx`, `dnspython` (see `requirements.txt` / `pyproject.toml`)

## What is not claimed

- Verified bulk deliverability rates, email accuracy %, or revenue impact
- That SMTP checks are undetectable or ToS-safe on every provider
- Production SLA, hosted API, or Micap bundling without a separate product decision

## Gaps

- No test suite exercised in this hygiene pass (optional `.[dev]` present in metadata)
- README was missing prior to 2026-09-30 docs PR
- Ethics / rate-limit guidance must stay in the README when promoting internally

## Next (owner)

1. Add a tiny offline unit test for pure parsers in `utils.py` (no network)
2. Decide Micap sales-ops packaging vs keep-as-library
3. No GitHub Actions workflow in this pass (token lacks `workflow` scope)

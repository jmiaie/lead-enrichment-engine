# lead-enrichment-engine

> **Status (2026-09-30):** Public **scaffold / stalled** sales-ops utility. See [`STATUS.md`](STATUS.md).

Zero-API-cost-oriented lead enrichment helpers: domain guess patterns, optional SMTP mailbox checks, and light page parse utilities. Extracted lineage noted in package docstring (Scout-inspired).

**Not** a SaaS product, CRM, or guaranteed email-finder. No enrichment accuracy or “deliverability rate” metrics are claimed in this README.

## Install (offline-friendly)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
enrich-lead --help
```

Optional: `pip install -e ".[proxy]"` for proxy helper extras; `".[dev]"` for pytest.

## CLI sketch

```bash
# Single lead (JSON out) — may perform DNS/HTTP/SMTP network I/O
enrich-lead --name "Ada Lovelace" --company "Analytical Engines" --website "https://example.com"

# Batch CSV round-trip
enrich-lead --csv leads.csv --output enriched.csv --verbose
```

Network calls are **opt-in by running the enrich commands**. Prefer dry review of inputs and local policy before batch jobs.

## Ethics, consent, and rate limits

Use only on data you are allowed to process.

- **Consent / purpose:** Enrichment for unsolicited cold outreach can be restricted by law and by recipient preference. Prefer opted-in lists and clear business purpose.
- **SMTP verify:** Probing mail servers can look like abuse. Keep concurrency low (`--workers` default is conservative), back off on errors, and honor provider blocks.
- **DNS / HTTP:** Same courtesy — no aggressive scraping; respect `robots.txt` and site terms where applicable.
- **Secrets:** Optional `--hunter-key` is for callers who already have a Hunter.io key; do not commit keys. This repo’s “zero API cost” path does not require paid APIs.
- **Compliance:** You are responsible for CAN-SPAM, CASL, GDPR/CCPA, TCPA, and local rules. This tool does not provide legal advice.

## Package layout

| Path | Role |
|------|------|
| `lead_enrichment/cli.py` | `enrich-lead` entrypoint |
| `lead_enrichment/enricher.py` | Enrichment orchestration |
| `lead_enrichment/stealth.py` | UA / delay / optional proxy helpers |
| `lead_enrichment/utils.py` | Parse helpers |

## License

MIT (see `pyproject.toml`).

#!/usr/bin/env python3
"""
CLI for lead enrichment engine.
Usage:
    enrich-lead --name "John Doe" --company "Acme Corp" --website "https://acme.com"
    enrich-lead --json '{"full_name": "John Doe", "company": "Acme Corp"}'
    enrich-lead --csv leads.csv --output enriched.csv
"""

import argparse
import csv
import json
import sys
from pathlib import Path

from lead_enrichment import enrich_lead, enrich_bulk


def main():
    parser = argparse.ArgumentParser(
        description="Enrich leads with verified emails and phone numbers (zero API cost)"
    )

    # Single lead mode
    parser.add_argument("--name", help="Full name of the lead")
    parser.add_argument("--company", help="Company name")
    parser.add_argument("--website", help="Company/personal website")
    parser.add_argument("--bio", help="Bio or description text")
    parser.add_argument("--headline", help="Professional headline (e.g., 'CEO at Acme')")
    parser.add_argument("--email", help="Known email (will be verified)")
    parser.add_argument("--phone", help="Known phone number")

    # JSON mode
    parser.add_argument("--json", help="Lead data as JSON string")

    # CSV batch mode
    parser.add_argument("--csv", help="Input CSV file with lead data")
    parser.add_argument("--output", "-o", help="Output CSV file (default: stdout)")

    # Options
    parser.add_argument("--hunter-key", help="Optional Hunter.io API key")
    parser.add_argument("--workers", type=int, default=3, help="Parallel workers for batch mode")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()

    # JSON mode
    if args.json:
        lead_data = json.loads(args.json)
        result = enrich_lead(lead_data, hunter_api_key=args.hunter_key)
        print(json.dumps(result, indent=2))
        return

    # CSV batch mode
    if args.csv:
        input_path = Path(args.csv)
        if not input_path.exists():
            print(f"Error: {args.csv} not found", file=sys.stderr)
            sys.exit(1)

        with open(input_path) as f:
            reader = csv.DictReader(f)
            leads = list(reader)

        if args.verbose:
            print(f"Enriching {len(leads)} leads with {args.workers} workers...", file=sys.stderr)

        results = enrich_bulk(leads, hunter_api_key=args.hunter_key, max_workers=args.workers)

        if args.output:
            with open(args.output, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=results[0].keys())
                writer.writeheader()
                writer.writerows(results)
            if args.verbose:
                print(f"Wrote {len(results)} enriched leads to {args.output}", file=sys.stderr)
        else:
            writer = csv.DictWriter(sys.stdout, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        return

    # Single lead mode
    if args.name:
        lead_data = {
            "full_name": args.name,
            "company": args.company or "",
            "website": args.website or "",
            "bio": args.bio or "",
            "headline": args.headline or "",
        }
        if args.email:
            lead_data["email"] = args.email
        if args.phone:
            lead_data["phone"] = args.phone

        result = enrich_lead(lead_data, hunter_api_key=args.hunter_key)
        print(json.dumps(result, indent=2))
        return

    parser.print_help()


if __name__ == "__main__":
    main()

"""
Lead Enrichment Engine
Standalone module extracted from Scout (kiryano/scout).
Zero-API-cost lead enrichment via SMTP verification, domain detection, and email pattern prediction.
"""

__version__ = "1.0.0"

from .enricher import LeadEnricher, enrich_lead, enrich_bulk
from .stealth import random_user_agent, random_delay, get_proxy
from .utils import extract_email, extract_phone, parse_abbreviated_number

__all__ = [
    "LeadEnricher",
    "enrich_lead",
    "enrich_bulk",
    "random_user_agent",
    "random_delay",
    "get_proxy",
    "extract_email",
    "extract_phone",
    "parse_abbreviated_number",
]

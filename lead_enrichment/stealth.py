"""
Stealth utilities for web scraping.
Provides user agent rotation, delays, and proxy management.
"""

import random
import time
from typing import Optional

# Rotating user agents to avoid detection
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]


def random_user_agent() -> str:
    """Return a random user agent string."""
    return random.choice(USER_AGENTS)


def random_delay(min_seconds: float = 0.5, max_seconds: float = 1.5) -> None:
    """Sleep for a random duration to avoid rate limiting."""
    time.sleep(random.uniform(min_seconds, max_seconds))


def get_proxy() -> Optional[str]:
    """
    Get proxy URL from environment variable LEAD_ENRICHMENT_PROXY.
    Returns None if not set.
    """
    import os
    return os.environ.get("LEAD_ENRICHMENT_PROXY")

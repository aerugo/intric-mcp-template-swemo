"""
Riksbank Monetary Policy API client.

This module provides an async HTTP client for querying Sveriges Riksbank's
Monetary Policy Data API.
"""

import asyncio
import logging
from typing import Any, Optional
from urllib.parse import urlencode

import httpx

logger = logging.getLogger(__name__)

BASE_URL = "https://api.riksbank.se/monetary_policy_data/v1/forecasts"


async def riksbanken_request(
    endpoint: str = "",
    params: Optional[dict[str, Any]] = None,
) -> dict[str, Any]:
    """
    Make an async request to the Riksbank API with retry logic for rate limiting.

    Args:
        endpoint: Optional endpoint suffix to append to the base URL
        params: Optional query parameters to include in the request

    Returns:
        JSON response as a dictionary

    Raises:
        httpx.HTTPError: For non-404, non-429 HTTP errors
    """
    url = f"{BASE_URL}/{endpoint}" if endpoint else BASE_URL
    params = params or {}

    # Use urlencode with safe=":" to preserve colons in policy round IDs (e.g., "2021:2")
    query_string = urlencode(params, safe=":")
    full_url = f"{url}?{query_string}" if query_string else url

    max_retries = 5
    retry_delays = [1, 2, 4, 8, 16]  # Exponential backoff delays in seconds

    async with httpx.AsyncClient(timeout=30.0) as client:
        for attempt in range(max_retries):
            try:
                logger.debug(f"Requesting {full_url}")
                response = await client.get(full_url)

                if response.status_code == 404:
                    logger.warning(f"Got 404 at {full_url}, returning empty.")
                    return {}

                if response.status_code == 429:
                    # Rate limited
                    if attempt < max_retries - 1:
                        wait = retry_delays[attempt]
                        logger.warning(f"Rate limited, retrying in {wait}s...")
                        await asyncio.sleep(wait)
                        continue
                    else:
                        logger.error("Max retries exceeded for rate limiting")
                        response.raise_for_status()

                response.raise_for_status()
                return response.json() if response.content else {}

            except httpx.HTTPError as e:
                logger.error(f"HTTP error occurred: {e}")
                if attempt == max_retries - 1:
                    raise
                if hasattr(e, 'response') and e.response.status_code != 429:
                    raise

    return {}

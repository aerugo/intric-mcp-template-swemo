"""
Riksbank Monetary Policy Data Tools.

This module provides functions to fetch Swedish economic data from
Sveriges Riksbank's Monetary Policy API.
"""

from typing import Optional

from monetary_policy_api import riksbanken_request


# Discovery Functions

async def list_policy_rounds() -> dict:
    """
    List all available policy round identifiers.

    Returns policy rounds in format 'YYYY:I' (e.g., '2025:2') which represent
    discrete forecast publication sets from Monetary Policy Reports or Updates.

    Returns:
        Dictionary containing list of available policy rounds
    """
    return await riksbanken_request("policy_rounds")


async def list_series_ids() -> dict:
    """
    List all available economic data series with metadata.

    Provides metadata for all series including series IDs, descriptions,
    units, source agencies, and decimal precision.

    Returns:
        Dictionary containing metadata for all available series
    """
    return await riksbanken_request("series")


# Generic Data Fetcher

async def get_policy_data(series_id: str, policy_round: Optional[str] = None) -> dict:
    """
    Fetch data for any Riksbank series identifier.

    Low-level function accepting any Riksbank series identifier and optional
    round filter, returning forecasts and observations with cutoff-date annotations.

    Args:
        series_id: The Riksbank series identifier (e.g., 'SEQGDPNAYCA')
        policy_round: Optional policy round filter (e.g., '2024:3' or 'latest')

    Returns:
        Dictionary containing forecast and observation data
    """
    params = {"series_id": series_id}
    if policy_round:
        params["policy_round"] = policy_round
    return await riksbanken_request("data", params)


# Real Economy Indicators

async def get_gdp_data(policy_round: Optional[str] = None) -> dict:
    """
    Get calendar-adjusted year-over-year GDP growth data.

    Series: SEQGDPNAYCA - Quarterly GDP growth rate, calendar-adjusted.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        GDP growth forecasts and observations
    """
    return await get_policy_data("SEQGDPNAYCA", policy_round)


async def get_unemployment_data(policy_round: Optional[str] = None) -> dict:
    """
    Get seasonally adjusted unemployment rate data.

    Series: SEQLABUEASA - Unemployment rate as percentage of labor force,
    seasonally adjusted.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Unemployment rate forecasts and observations
    """
    return await get_policy_data("SEQLABUEASA", policy_round)


async def get_hourly_labour_cost_data(policy_round: Optional[str] = None) -> dict:
    """
    Get annual hourly labour cost changes from National Accounts.

    Series: SEACOMNAYCA - Year-over-year changes in hourly labour costs.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Hourly labour cost change forecasts and observations
    """
    return await get_policy_data("SEACOMNAYCA", policy_round)


async def get_hourly_wage_na_data(policy_round: Optional[str] = None) -> dict:
    """
    Get National Accounts hourly wage growth data.

    Series: SEAWAGNAYCA - Year-over-year hourly wage growth from National Accounts.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Hourly wage growth forecasts and observations
    """
    return await get_policy_data("SEAWAGNAYCA", policy_round)


async def get_hourly_wage_nmo_data(policy_round: Optional[str] = None) -> dict:
    """
    Get National Mediation Office hourly wage measure.

    Series: SEAWAGKLYNA - Wage statistics from the National Mediation Office.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        NMO wage measure forecasts and observations
    """
    return await get_policy_data("SEAWAGKLYNA", policy_round)


async def get_gdp_gap_data(policy_round: Optional[str] = None) -> dict:
    """
    Get GDP output gap data.

    Series: SEQGDPGAPYSA - Output gap as percentage of potential output,
    showing economic slack or overheating.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        GDP gap forecasts and observations
    """
    return await get_policy_data("SEQGDPGAPYSA", policy_round)


async def get_general_government_net_lending_data(policy_round: Optional[str] = None) -> dict:
    """
    Get general government net lending (fiscal position) data.

    Series: SEAPBSNAYNA - Government fiscal position as percentage of GDP.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Government net lending forecasts and observations
    """
    return await get_policy_data("SEAPBSNAYNA", policy_round)


# Labor Market

async def get_employed_persons_data(policy_round: Optional[str] = None) -> dict:
    """
    Get employed persons data.

    Series: SEQLABEPASA - Seasonally adjusted employment level in thousands.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Employment level forecasts and observations
    """
    return await get_policy_data("SEQLABEPASA", policy_round)


async def get_labour_force_data(policy_round: Optional[str] = None) -> dict:
    """
    Get labour force data.

    Series: SEQLABLFASA - Seasonally adjusted labor force level in thousands.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Labour force level forecasts and observations
    """
    return await get_policy_data("SEQLABLFASA", policy_round)


# Demographics

async def get_population_data(policy_round: Optional[str] = None) -> dict:
    """
    Get total population forecast data.

    Series: SEPOPYRCA - Total population in thousands.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Population forecasts and observations
    """
    return await get_policy_data("SEPOPYRCA", policy_round)


async def get_population_level_data(policy_round: Optional[str] = None) -> dict:
    """
    Get population aged 15-74 data.

    Series: SEQPOPNAANA - Population in working age range (15-74 years) in thousands.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Working-age population forecasts and observations
    """
    return await get_policy_data("SEQPOPNAANA", policy_round)


# Inflation Measures

async def get_cpi_data(policy_round: Optional[str] = None) -> dict:
    """
    Get headline CPI year-over-year inflation data.

    Series: SEMCPINAYNA - Consumer Price Index year-over-year change.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        CPI inflation forecasts and observations
    """
    return await get_policy_data("SEMCPINAYNA", policy_round)


async def get_cpi_index_data(policy_round: Optional[str] = None) -> dict:
    """
    Get CPI index level data.

    Series: SEMCPINAANA - CPI index level with base 1980=100.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        CPI index level forecasts and observations
    """
    return await get_policy_data("SEMCPINAANA", policy_round)


async def get_cpi_yoy_data(policy_round: Optional[str] = None) -> dict:
    """
    Get CPI year-over-year change data.

    Series: SEMCPINAYNA - CPI year-over-year percentage change.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        CPI year-over-year change forecasts and observations
    """
    return await get_policy_data("SEMCPINAYNA", policy_round)


async def get_cpif_data(policy_round: Optional[str] = None) -> dict:
    """
    Get CPIF inflation data (Riksbank's operational target).

    Series: SEMCPIFNAYNA - CPIF (CPI with fixed interest rate) is the
    Riksbank's operational inflation target measure.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        CPIF inflation forecasts and observations
    """
    return await get_policy_data("SEMCPIFNAYNA", policy_round)


async def get_cpif_yoy_data(policy_round: Optional[str] = None) -> dict:
    """
    Get CPIF year-over-year inflation data.

    Series: SEMCPIFNAYNA - CPIF year-over-year percentage change.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        CPIF year-over-year change forecasts and observations
    """
    return await get_policy_data("SEMCPIFNAYNA", policy_round)


async def get_cpif_ex_energy_data(policy_round: Optional[str] = None) -> dict:
    """
    Get core CPIF inflation excluding energy.

    Series: SEMCPIFFEXYNA - Core inflation measure excluding energy prices.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Core CPIF ex-energy forecasts and observations
    """
    return await get_policy_data("SEMCPIFFEXYNA", policy_round)


async def get_cpif_ex_energy_index_data(policy_round: Optional[str] = None) -> dict:
    """
    Get core CPIF index excluding energy.

    Series: SEMCPIFFEXANA - Core inflation index level (base 1987=100)
    excluding energy.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Core CPIF ex-energy index forecasts and observations
    """
    return await get_policy_data("SEMCPIFFEXANA", policy_round)


# GDP Variants

async def get_gdp_level_saca_data(policy_round: Optional[str] = None) -> dict:
    """
    Get real GDP level with full seasonal and calendar adjustment.

    Series: SEQGDPNAASA - Real GDP in million SEK, seasonally AND calendar adjusted.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        GDP level (SACA) forecasts and observations
    """
    return await get_policy_data("SEQGDPNAASA", policy_round)


async def get_gdp_level_ca_data(policy_round: Optional[str] = None) -> dict:
    """
    Get real GDP level with calendar adjustment only.

    Series: SEQGDPNAACA - Real GDP in million SEK, calendar-adjusted only.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        GDP level (CA) forecasts and observations
    """
    return await get_policy_data("SEQGDPNAACA", policy_round)


async def get_gdp_level_na_data(policy_round: Optional[str] = None) -> dict:
    """
    Get real GDP level without adjustments.

    Series: SEQGDPNAANA - Real GDP in million SEK, non-adjusted raw series.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        GDP level (NA) forecasts and observations
    """
    return await get_policy_data("SEQGDPNAANA", policy_round)


async def get_gdp_yoy_sa_data(policy_round: Optional[str] = None) -> dict:
    """
    Get GDP year-over-year growth with full adjustments.

    Series: SEQGDPNAYSA - GDP year-over-year with seasonal and calendar adjustment.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        GDP YoY (SA) growth forecasts and observations
    """
    return await get_policy_data("SEQGDPNAYSA", policy_round)


async def get_gdp_yoy_na_data(policy_round: Optional[str] = None) -> dict:
    """
    Get GDP year-over-year growth without adjustments.

    Series: SEQGDPNAYNA - GDP year-over-year non-adjusted.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        GDP YoY (NA) growth forecasts and observations
    """
    return await get_policy_data("SEQGDPNAYNA", policy_round)


# Monetary Policy

async def get_policy_rate_data(policy_round: Optional[str] = None) -> dict:
    """
    Get Riksbank policy rate (repo rate) data.

    Series: SEQRATENAYNA - Riksbank repo rate, quarterly mean in percent.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        Policy rate forecasts and observations
    """
    return await get_policy_data("SEQRATENAYNA", policy_round)


# Exchange Rates

async def get_nominal_exchange_rate_kix_index_data(policy_round: Optional[str] = None) -> dict:
    """
    Get KIX exchange rate index data.

    Series: SEQKIXNAANA - KIX exchange rate index (base November 1992=100).
    KIX is a trade-weighted index of the Swedish krona.

    Args:
        policy_round: Optional policy round (e.g., '2024:3' or 'latest')

    Returns:
        KIX index forecasts and observations
    """
    return await get_policy_data("SEQKIXNAANA", policy_round)

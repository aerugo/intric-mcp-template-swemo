"""
Sveriges Riksbank Monetary Policy Data MCP Server.

This server provides access to Swedish economic data from Sveriges Riksbank's
Monetary Policy API through the Model Context Protocol (MCP).
"""

from fastmcp import FastMCP

from monetary_policy_tools import (
    # Discovery functions
    list_policy_rounds,
    list_series_ids,
    # Generic data fetcher
    get_policy_data,
    # Real economy indicators
    get_gdp_data,
    get_unemployment_data,
    get_hourly_labour_cost_data,
    get_hourly_wage_na_data,
    get_hourly_wage_nmo_data,
    get_gdp_gap_data,
    get_general_government_net_lending_data,
    # Labor market
    get_employed_persons_data,
    get_labour_force_data,
    # Demographics
    get_population_data,
    get_population_level_data,
    # Inflation measures
    get_cpi_data,
    get_cpi_index_data,
    get_cpi_yoy_data,
    get_cpif_data,
    get_cpif_yoy_data,
    get_cpif_ex_energy_data,
    get_cpif_ex_energy_index_data,
    # GDP variants
    get_gdp_level_saca_data,
    get_gdp_level_ca_data,
    get_gdp_level_na_data,
    get_gdp_yoy_sa_data,
    get_gdp_yoy_na_data,
    # Monetary policy
    get_policy_rate_data,
    # Exchange rates
    get_nominal_exchange_rate_kix_index_data,
)

# Initialize the FastMCP server
mcp = FastMCP(
    name="Sveriges Riksbank Monetary Policy Data MCP Server",
)

# Register Discovery Tools
mcp.tool()(list_policy_rounds)
mcp.tool()(list_series_ids)

# Register Generic Data Fetcher
mcp.tool()(get_policy_data)

# Register Real Economy Indicators
mcp.tool()(get_gdp_data)
mcp.tool()(get_unemployment_data)
mcp.tool()(get_hourly_labour_cost_data)
mcp.tool()(get_hourly_wage_na_data)
mcp.tool()(get_hourly_wage_nmo_data)
mcp.tool()(get_gdp_gap_data)
mcp.tool()(get_general_government_net_lending_data)

# Register Labor Market Tools
mcp.tool()(get_employed_persons_data)
mcp.tool()(get_labour_force_data)

# Register Demographics Tools
mcp.tool()(get_population_data)
mcp.tool()(get_population_level_data)

# Register Inflation Measures
mcp.tool()(get_cpi_data)
mcp.tool()(get_cpi_index_data)
mcp.tool()(get_cpi_yoy_data)
mcp.tool()(get_cpif_data)
mcp.tool()(get_cpif_yoy_data)
mcp.tool()(get_cpif_ex_energy_data)
mcp.tool()(get_cpif_ex_energy_index_data)

# Register GDP Variants
mcp.tool()(get_gdp_level_saca_data)
mcp.tool()(get_gdp_level_ca_data)
mcp.tool()(get_gdp_level_na_data)
mcp.tool()(get_gdp_yoy_sa_data)
mcp.tool()(get_gdp_yoy_na_data)

# Register Monetary Policy Tools
mcp.tool()(get_policy_rate_data)

# Register Exchange Rate Tools
mcp.tool()(get_nominal_exchange_rate_kix_index_data)

# Start the server with streamable HTTP transport for Intric compatibility
if __name__ == "__main__":
    mcp.run(transport="streamable-http")

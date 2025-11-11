# Sveriges Riksbank MCP Server

An MCP (Model Context Protocol) server that provides access to Swedish economic data from Sveriges Riksbank's Monetary Policy API. This server uses streamable HTTP transport for seamless integration with Intric.

## Overview

This server wraps Sveriges Riksbank's open API for monetary policy data, exposing approximately 30 economic series as callable tools through the MCP. It enables AI assistants to query Swedish economic indicators including GDP, inflation, employment, and monetary policy data.

## Features

- **Comprehensive Economic Data**: Access to 30+ Swedish economic indicators
- **Forecast & Historical Data**: Both forecasts from policy rounds and realized observations
- **Vintage Control**: Query specific policy rounds or retrieve latest consolidated data
- **HTTP Transport**: Compatible with Intric's built-in MCP client
- **Type-Safe**: Full async/await with proper error handling

## Available Data Categories

### Discovery Tools
- `list_policy_rounds` - Available policy round identifiers (e.g., "2025:2")
- `list_series_ids` - Metadata for all available series

### Real Economy Indicators
- GDP growth (calendar-adjusted, various measures)
- Output gap
- Government fiscal position

### Labor Market
- Unemployment rate
- Employment levels
- Labor force statistics
- Hourly wages and labor costs

### Demographics
- Total population
- Working-age population (15-74 years)

### Inflation Measures
- CPI (Consumer Price Index)
- CPIF (CPI with fixed interest rate - Riksbank's target)
- Core inflation (excluding energy)
- Various index levels and year-over-year changes

### Monetary Policy
- Policy rate (repo rate)

### Exchange Rates
- KIX exchange rate index (trade-weighted krona index)

## Running the Server

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the server:
```bash
python server.py
```

The server will start on `http://localhost:8000` by default.

## Connecting to Intric

1. Expose your server URL (e.g., using ngrok for testing):
```bash
ngrok http 8000
```

2. Add the exposed URL (ending with `/mcp`) to Intric's MCP connections settings

3. Intric will automatically discover all available tools

## Tool Usage

All data fetching tools accept an optional `policy_round` parameter:

- **Specific round**: e.g., `"2024:3"` for a specific forecast vintage
- **Latest data**: `"latest"` for consolidated historical observations
- **All vintages**: Omit parameter to get all forecasts across rounds

### Example Tool Calls

```python
# Get latest GDP data
get_gdp_data(policy_round="latest")

# Get unemployment forecast from specific policy round
get_unemployment_data(policy_round="2024:3")

# Get all CPIF inflation vintages
get_cpif_data()

# Query any series by ID
get_policy_data(series_id="SEQGDPNAYCA", policy_round="latest")
```

## Data Structure

The Riksbank publishes forecasts 4-5 times yearly in `YYYY:I` format. Each time-series follows this naming convention:

`COUNTRY-FREQUENCY-AREA-DECOMPOSITION-UNIT-ADJUSTED`

Example: `SEQGDPNAYCA` = Sweden, Quarterly GDP, National Accounts, Year-over-year change, Calendar-adjusted

## Project Structure

```
swemo-mcp/
├── server.py                    # Main server with tool registration
├── monetary_policy_tools.py     # Tool implementations
├── monetary_policy_api.py       # Riksbank API client
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## API Reference

The server uses Sveriges Riksbank's Monetary Policy Data API:
- Base URL: `https://api.riksbank.se/monetary_policy_data/v1/forecasts`
- Built-in retry logic with exponential backoff for rate limiting
- Comprehensive error handling

## License

Apache 2.0

## Disclaimers

This is an unofficial project. Sveriges Riksbank has no involvement with this server. Data is provided by Riksbank "as is" without warranties.

## Technical Details

- **Framework**: FastMCP with streamable HTTP transport
- **Python**: 3.12+
- **HTTP Client**: httpx with async support
- **Rate Limiting**: Automatic exponential backoff retry logic
- **Transport**: Streamable HTTP for Intric compatibility

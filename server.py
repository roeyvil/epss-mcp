# server.py
from fastmcp import FastMCP, Context
import requests

# Create an MCP server
mcp = FastMCP("EPSS", dependencies=["requests"])

# Base URL for the API
BASE_URL = "https://api.first.org/data/v1/epss"


@mcp.tool()
async def get_epss_api_description(ctx: Context):
    """Fetch the documentation about using the EPSS API"""
    await ctx.info("Fetching API description")
    return requests.get("https://www.first.org/epss/api").text


@mcp.tool()
async def query_api(ctx: Context, params):
    """Run a query against the base URL of the EPSS API
    :param ctx: MCP context
    :param params: the HTTP params to be appended to the base URL
    """
    await ctx.info(f"Fetching EPSS data with params {params}")
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # This code only runs when the file is executed directly
    mcp.run()

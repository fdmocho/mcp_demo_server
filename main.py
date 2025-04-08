
import httpx
import asyncio
from apiconfig import API_KEYS
# server.py
from mcp.server.fastmcp import FastMCP

NEO_API_KEY = API_KEYS["nasa"]

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool for getting NEO json by date
@mcp.tool()
async def getNeo(start_date: str, end_date: str = None):

    """Get NEO (Nasa's Near Earth Object) by date, if an end date is not provided use start date as end date as well.

    Args:
        startdate: Start date of the request
        enddate: End date of the request
    """

    if end_date is None:
        end_date = start_date
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": NEO_API_KEY  # Replace with your actual API key
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.text

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

""" if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') """
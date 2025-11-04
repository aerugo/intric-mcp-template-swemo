# Intric MCP Template Server

A template for building Model Context Protocol (MCP) servers that connect seamlessly with Intric's built-in MCP client. This template demonstrates how to create custom tools and resources that extend your AI assistant's capabilities.

## Features

- **Tools**: Functions the AI can call to perform actions
- **Resources**: Static data the AI can access
- **Resource Templates**: Dynamic resources based on parameters

## Running the Server

Start the MCP server with HTTP transport:

```bash
python server.py
```

The server will start on `http://localhost:8000` by default.

## Connecting to Intric

Add your exposed server URL in Intric's MCP connections settings. Intric will automatically discover all available tools and resources.

Tip: You can use a service like ngrok to expose a https url binded to a local port and put that url (ending with /mcp) into Intric

## Building Your Own MCP Server

### Adding Tools

```python
@mcp.tool
def your_function_name(param1: str, param2: int) -> str:
    """Description of what this tool does."""
    return f"Result: {param1} - {param2}"
```

### Adding Resources

```python
@mcp.resource("resource://your_resource_name")
def get_your_data() -> str:
    """Description of what data this resource provides"""
    return "Your data here"
```

### Adding Resource Templates

```python
@mcp.resource("data://{category}/{id}")
def get_dynamic_data(category: str, id: str) -> dict:
    """Provide data based on category and id."""
    return {"category": category, "id": id, "data": "..."}
```

## Project Structure

```
intric-mcp-template/
├── server.py         # Main server file with examples
├── tools.py          # Example tool implementations
├── resources.py      # Example resource implementations
├── requirements.txt  # Python dependencies
```



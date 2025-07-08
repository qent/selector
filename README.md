# XPath Prompt MCP Server

This repository contains a minimal [MCP](https://github.com/modelcontextprotocol) server built with the `mcp` Python package. The server exposes a single prompt describing best practices for generating XPath selectors for Android UI elements.

## Requirements
- Python 3.12+

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the server

Clone the repository and start the server using the standard I/O transport:

```bash
git clone <repo-url>
cd selector
python server.py
```

The server will start in `stdio` mode. Use any compatible MCP client to request the `xpath_rules` prompt.

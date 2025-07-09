# Android Hierarchy Element Selector MCP Server

This repository contains a minimal [MCP](https://github.com/modelcontextprotocol) server built with the `mcp` Python package. 

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

The server will start in `stdio` mode. Use any compatible MCP client to request
the `xpath_selector_rules` prompt.

## Debug a client

Install the optional CLI tools and launch in dev mode:

```bash
pip install "mcp[cli]"
mcp dev server.py
```

## Connecting to a client

Add configuration for Claude desktop (```/Users/username/Library/Application Support/Claude/claude_desktop_config.json```) or other client:
```json
"android_selector_mcp": {
    "command": "/Users/username/selector/venv/bin/python",
    "args": [
        "/Users/username/selector/server.py"
    ]
}
```

After installation, start the server from the client and request the
`xpath_selector_rules` prompt or call the `android_screen_hierarchy` tool as
needed.

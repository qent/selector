# Android XPath Selector Server

This project implements a minimal [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol) server that assists with building stable selectors for Android user interfaces. The server exposes three tools:

- **Tool `xpath_selector_rules`** – Returns guidelines describing how to craft robust XPath expressions.
- **Tool `espresso_selector_rules`** – Provides best practices for reliable Espresso selectors.
- **Tool `android_screen_hierarchy`** – Connects to an Android device using `uiautomator2` and returns a structured representation of the current UI hierarchy.

## Requirements
- Python 3.12+
- An Android device accessible via `adb` for the hierarchy tool

Install dependencies with:

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

The server will run in `stdio` mode. Any MCP-compatible client can invoke the provided tools.

## Development

Before committing changes, format and test the code:

```bash
isort .
black .
pytest
```

You can also launch the server with the optional CLI provided by `mcp`:

```bash
pip install "mcp[cli]"
mcp dev server.py
```

## Example client configuration

For Claude Desktop, add an entry to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
"android_selector_mcp": {
    "command": "/path/to/python",
    "args": ["/path/to/selector/server.py"]
}
```

After configuring, start the server from the client and use the provided tools as needed.

from pathlib import Path

from mcp.server.fastmcp import FastMCP

PROMPT_FILE = Path(__file__).with_name("prompt.txt")

server = FastMCP(name="XPathPromptServer")


@server.prompt(name="xpath_rules", title="XPath selector rules")
def xpath_rules() -> str:
    """Return rules for generating robust XPath selectors."""
    return PROMPT_FILE.read_text()


def main() -> None:
    """Run the server using stdio transport."""
    server.run()


if __name__ == "__main__":
    main()

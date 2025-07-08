from pathlib import Path

import uiautomator2 as u2  # type: ignore
from mcp.server.fastmcp import FastMCP

PROMPT_FILE = Path(__file__).with_name("prompt.txt")

server = FastMCP(name="XPathPromptServer")


@server.prompt(name="xpath_rules", title="XPath selector rules")
def xpath_rules() -> str:
    """Return rules for generating robust XPath selectors."""
    return PROMPT_FILE.read_text()


@server.tool(name="screen_hierarchy", title="Android screen hierarchy")
def screen_hierarchy(device: str | None = None) -> str:
    """Return the current screen hierarchy as an XML string.

    Args:
        device: Optional device URL or serial for ``uiautomator2.connect``.

    Returns:
        XML representation of the UI hierarchy.
    """

    d = u2.connect(device) if device else u2.connect()
    return d.dump_hierarchy(compressed=False, pretty=True)


def main() -> None:
    """Run the server using stdio transport."""
    server.run()


if __name__ == "__main__":
    main()

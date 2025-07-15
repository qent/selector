from pathlib import Path
from typing import Any

import uiautomator2 as u2  # type: ignore
from mcp.server.fastmcp import FastMCP

from .hierarchy import parse_xml_to_tree

PROMPTS_DIR = Path(__file__).with_name("prompts")
XPATH_PROMPT_FILE = PROMPTS_DIR / "xpath_prompt.txt"
ESPRESSO_PROMPT_FILE = PROMPTS_DIR / "espresso_prompt.txt"

server = FastMCP(name="SelectorServer")


@server.tool(name="xpath_selector_rules", title="XPath selector rules")
def xpath_selector_rules() -> str:
    """Return rules for generating robust XPath selectors."""
    return XPATH_PROMPT_FILE.read_text()


@server.tool(name="espresso_selector_rules", title="Espresso selector rules")
def espresso_selector_rules() -> str:
    """Return best practices for Espresso selectors."""
    return ESPRESSO_PROMPT_FILE.read_text()


@server.tool(name="android_screen_hierarchy", title="Android screen hierarchy")
def android_screen_hierarchy(device: str | None = None) -> list[dict[str, Any]]:
    """Return the current screen hierarchy.

    Args:
        device: Optional device URL or serial for ``uiautomator2.connect``.

    Returns:
        Parsed representation of the UI hierarchy.
    """

    d = u2.connect(device) if device else u2.connect()
    xml = d.dump_hierarchy(compressed=False)
    return parse_xml_to_tree(xml)


if __name__ == "__main__":
    server.run()

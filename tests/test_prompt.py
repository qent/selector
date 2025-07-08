import asyncio
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from mcp.types import TextContent

from server import PROMPT_FILE, server


async def get_prompt_text() -> str:
    result = await server.get_prompt("xpath_selector_rules")
    messages = result.messages
    assert messages, "No messages returned"
    content = messages[0].content
    assert isinstance(content, TextContent)
    return content.text


def test_xpath_prompt() -> None:
    expected = PROMPT_FILE.read_text()
    text = asyncio.run(get_prompt_text())
    assert expected == text

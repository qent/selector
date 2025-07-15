import asyncio

from mcp.types import TextContent

from selector.server import ESPRESSO_PROMPT_FILE, XPATH_PROMPT_FILE, server


async def get_tool_text(tool_name: str) -> str:
    result = await server.call_tool(tool_name, {})
    assert isinstance(result, tuple), "Unexpected tool result type"
    content_list, _ = result
    assert content_list, "No content returned"
    content = content_list[0]
    assert isinstance(content, TextContent)
    return content.text


def test_xpath_rules_tool() -> None:
    expected = XPATH_PROMPT_FILE.read_text()
    text = asyncio.run(get_tool_text("xpath_selector_rules"))
    assert expected == text


def test_espresso_rules_tool() -> None:
    expected = ESPRESSO_PROMPT_FILE.read_text()
    text = asyncio.run(get_tool_text("espresso_selector_rules"))
    assert expected == text

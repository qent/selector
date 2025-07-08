import asyncio
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.append(str(Path(__file__).resolve().parents[1]))

from mcp.types import TextContent

from server import server


async def call_tool() -> str:
    fake_device = MagicMock()
    fake_device.dump_hierarchy.return_value = "<hierarchy/>"
    with patch("server.u2.connect", return_value=fake_device):
        result = await server.call_tool("screen_hierarchy", {})
    assert isinstance(result, tuple), "Unexpected tool result type"
    content_list, _ = result
    assert content_list, "No content returned"
    content = content_list[0]
    assert isinstance(content, TextContent)
    return content.text


def test_screen_hierarchy_tool() -> None:
    text = asyncio.run(call_tool())
    assert text == "<hierarchy/>"

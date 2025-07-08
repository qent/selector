import asyncio
import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.append(str(Path(__file__).resolve().parents[1]))

from mcp.types import TextContent

from hierarchy import parse_xml_to_tree
from server import server

XML = """
<hierarchy>
    <node index='0' package='pkg' class='android.widget.TextView' text='foo' resource-id='res' content-desc='desc' bounds='[0,0][1,1]' visible-to-user='true'>
        <node index='1' visible-to-user='false'/>
        <node index='2' visible-to-user='true'/>
    </node>
</hierarchy>
"""


async def call_tool() -> tuple[list[TextContent], dict[str, list[dict]]]:
    fake_device = MagicMock()
    fake_device.dump_hierarchy.return_value = XML
    with patch("server.u2.connect", return_value=fake_device):
        result = await server.call_tool("android_screen_hierarchy", {})
    assert isinstance(result, tuple), "Unexpected tool result type"
    content_list, structured = result
    assert content_list, "No content returned"
    for content in content_list:
        assert isinstance(content, TextContent)
    return content_list, structured


def test_screen_hierarchy_tool() -> None:
    contents, structured = asyncio.run(call_tool())
    expected = parse_xml_to_tree(XML)
    parsed = [json.loads(content.text) for content in contents]
    assert parsed == expected
    assert structured == {"result": expected}

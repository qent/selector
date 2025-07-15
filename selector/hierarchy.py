from typing import Any
from xml.etree import ElementTree


def parse_node(xml_node: ElementTree.Element) -> dict[str, Any]:
    """Recursively parse ``xml_node`` into dictionaries."""

    attrib = xml_node.attrib
    children = [
        parse_node(child)
        for child in xml_node.findall("node")
        if child.attrib.get("visible-to-user") == "true"
    ]
    node: dict[str, Any] = {
        "index": int(attrib["index"]) if attrib.get("index") else None,
        "package": attrib.get("package"),
        "bounds": attrib.get("bounds"),
        "class": attrib.get("class"),
        "text": attrib.get("text"),
        "resource-id": attrib.get("resource-id"),
        "content-desc": attrib.get("content-desc"),
        "children": children,
    }
    return {k: v for k, v in node.items() if v not in (None, "", [], {})}


def parse_xml_to_tree(xml_path: str) -> list[dict[str, Any]]:
    """Parse ``xml_path`` hierarchy string into a list of dictionaries."""

    root = ElementTree.fromstring(xml_path)
    return [parse_node(node) for node in root.findall("node")]

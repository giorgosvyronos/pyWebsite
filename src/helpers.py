from textnode import TextNode, TextType
from htmlnode import LeafNode
import re

def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            for item in element:
                flatList.append(item)
        else:
            flatList.append(element)
    return flatList

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if not text_node:
        raise Exception("text_node is empty")
    else:
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, props={"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode(
                "img", "", props={"src": text_node.url, "alt": text_node.text}
            )
        else:
            raise Exception("Not a valid text type")


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
):
    new_nodes = []
    for node in old_nodes:
        if not delimiter in node.text:
            new_nodes.append(node)
            continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_phrase = node.text.split(delimiter)
        if not len(split_phrase) % 2 != 0:
            raise Exception(f"Missing matching delimiter {delimiter}")
        for idx, item in enumerate(split_phrase):
            if idx % 2 == 0:
                if item:
                    new_nodes.append(TextNode(item, TextType.TEXT))
            else:
                new_nodes.append(TextNode(item, text_type))
    return new_nodes


def extract_markdown_images(text: str):
    """
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    """
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text: str):
    """
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    """
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        possible_images = extract_markdown_images(node.text)
        splitters = [f"![{a[0]}]({a[1]})" for a in possible_images]
        remainder = node.text
        for splitter in splitters:
            left, remainder = remainder.split(splitter, maxsplit=1)
            if left:
                new_nodes.append(TextNode(left, TextType.TEXT))
            alt, link = extract_markdown_images(splitter)[0]
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))
        if remainder:
            new_nodes.append(TextNode(remainder,TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        possible_images = extract_markdown_links(node.text)
        splitters = [f"[{a[0]}]({a[1]})" for a in possible_images]
        remainder = node.text
        for splitter in splitters:
            left, remainder = remainder.split(splitter, maxsplit=1)
            if left:
                new_nodes.append(TextNode(left, TextType.TEXT))
            alt, link = extract_markdown_links(splitter)[0]
            new_nodes.append(TextNode(alt, TextType.LINK, link))
        if remainder:
            new_nodes.append(TextNode(remainder,TextType.TEXT))
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    old_node = TextNode(text, TextType.TEXT)
    extracted_img = split_nodes_image([old_node])
    extracted_links = [
            split_nodes_link([item]) if item.text_type == TextType.TEXT else item
            for item in extracted_img
            ]
    extracted_links = flat(extracted_links)
    extracted_bold =[
            split_nodes_delimiter([item],delimiter="**",text_type=TextType.BOLD) if item.text_type == TextType.TEXT else item
            for item in extracted_links
            ]
    extracted_bold = flat(extracted_bold)
 
    extracted_code =[
            split_nodes_delimiter([item],delimiter="`",text_type=TextType.CODE) if item.text_type == TextType.TEXT else item
            for item in extracted_bold
            ]
    extracted_code = flat(extracted_code)

    extracted_italic =[
            split_nodes_delimiter([item],delimiter="_",text_type=TextType.ITALIC) if item.text_type == TextType.TEXT else item
            for item in extracted_code
            ]
    return flat(extracted_italic)

from textnode import TextNode,TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node:TextNode) -> LeafNode:
    if not text_node:
        raise Exception("text_node is empty")
    else:
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None,text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b",text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i",text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code",text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a",text_node.text,props={"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img","",props={"src":text_node.url,"alt":text_node.text})
        else:
            raise Exception("Not a valid text type")

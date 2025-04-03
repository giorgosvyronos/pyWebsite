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

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_phrase = node.text.split(delimiter)
        if not len(split_phrase)%2!=0:
            raise Exception(f"Missing matching delimiter {delimiter}")
        for idx,item in enumerate(split_phrase):
            if idx%2==0:
                if item:
                    new_nodes.append(TextNode(item,TextType.TEXT))
            else:
                new_nodes.append(TextNode(item,text_type))
    return new_nodes

from enum import Enum
from helpers import markdown_to_blocks, text_node_to_html_node, text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.paragraph
        return BlockType.quote
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.paragraph
        return BlockType.unordered_list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.paragraph
            i += 1
        return BlockType.ordered_list
    return BlockType.paragraph

def text_to_children(text:str) -> HTMLNode:
    new_text = text.replace("\n"," ")
    text_nodes = text_to_textnodes(new_text)
    leaf_nodes = list(map(text_node_to_html_node,text_nodes))
    return ParentNode("p",leaf_nodes)

def heading_to_html(text:str) -> HTMLNode:
    tag = f"h{text.split()[0].count('#')}"
    value = " ".join(text.split()[1:])
    return LeafNode(tag=tag,value=value)

def code_to_html(text:str) -> HTMLNode:
    inline_code = text[3:-3].lstrip()
    child = LeafNode("code",inline_code)
    return ParentNode("pre",children=[child])

def quote_to_html(text:str) -> HTMLNode:
    new_text = text.replace(">","").strip()
    return LeafNode("blockquote",new_text)

def unordered_to_html(text:str) -> HTMLNode:
    text_nodes = [text_to_textnodes(item[2:]) for item in text.split("\n")]
    leaf_nodes = [list(map(text_node_to_html_node,nodes)) for nodes in text_nodes]
    parent_nodes = [ParentNode("li",children=items) for items in leaf_nodes]
    return ParentNode("ul",parent_nodes)

def ordered_to_html(text:str) -> HTMLNode:
    text_nodes = [text_to_textnodes(item[3:]) for item in text.split("\n")]
    leaf_nodes = [list(map(text_node_to_html_node,nodes)) for nodes in text_nodes]
    parent_nodes = [ParentNode("li",children=items) for items in leaf_nodes]
    return ParentNode("ol",parent_nodes)

def markdown_to_html_node(markdown:str) -> HTMLNode:
    total_html_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block:
            block_type = block_to_block_type(block)
            if block_type == BlockType.paragraph:
                total_html_nodes.append(text_to_children(block))
            if block_type == BlockType.heading:
                total_html_nodes.append(heading_to_html(block))
            elif block_type == BlockType.code:
                total_html_nodes.append(code_to_html(block))
            elif block_type == BlockType.quote:
                total_html_nodes.append(quote_to_html(block))
            elif block_type == BlockType.unordered_list:
                total_html_nodes.append(unordered_to_html(block))
            elif block_type == BlockType.ordered_list:
                total_html_nodes.append(ordered_to_html(block))
    return ParentNode("div",total_html_nodes)

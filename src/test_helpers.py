import unittest

from helpers import split_nodes_delimiter, text_node_to_html_node
from textnode import TextNode, TextType


class TestHelpers(unittest.TestCase):
    def test_empty_text_node(self):
        with self.assertRaises(Exception) as e:
            _ = text_node_to_html_node(None)
            self.assertEqual(e.msg, "text_node is empty")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "<code>This is a text node</code>")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK,url="www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": node.url})
        self.assertEqual(html_node.to_html(), f'<a href="{node.url}">This is a text node</a>')

    def test_image(self):
        node = TextNode("Example Website", TextType.IMAGE, "www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":node.url,"alt":node.text})
        self.assertEqual(html_node.to_html(), f'<img src="{node.url}" alt="{node.text}"></img>')

    def test_delimiter_1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,result)

    def test_delimiter_2(self):
        node = TextNode("*bold block* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        result = [
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,result)

    def test_delimiter_3(self):
        node = TextNode("This is a _italic block_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        result = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes,result)

    def test_delimiter_4(self):
        node = TextNode("This is a _italic block_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        result = [
            TextNode("This is a _italic block_", TextType.TEXT)
        ]
        self.assertEqual(new_nodes,result)

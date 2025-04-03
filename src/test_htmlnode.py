import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq_tag_val(self):
        node = HTMLNode("p", "hello")
        nod1 = HTMLNode("p", "hello")
        self.assertEqual(node, nod1)

    def test_non_eq_tag_val(self):
        node = HTMLNode("p", "hello")
        nod1 = HTMLNode("a", "hello")
        self.assertNotEqual(node, nod1)

    def test_eq_props(self):
        node = HTMLNode("p", "hello", None, {"href": "example.com", "target": "_blank"})
        nod1 = HTMLNode("p", "hello", None, {"href": "example.com", "target": "_blank"})
        self.assertEqual(node, nod1)

    def test_not_props(self):
        node = HTMLNode("p", "hello", None, {"href": "example.com", "target": "_blank"})
        nod1 = HTMLNode("p", "hello", None, {"href": "amazon.com", "target": "_blank"})
        self.assertNotEqual(node, nod1)

    def test_eq_children(self):
        child = HTMLNode(
            "p", "hello", None, {"href": "example.com", "target": "_blank"}
        )
        node = HTMLNode(
            "p", "hello", [child], {"href": "amazon.com", "target": "_blank"}
        )
        nod1 = HTMLNode(
            "p", "hello", [child], {"href": "amazon.com", "target": "_blank"}
        )
        self.assertEqual(node, nod1)

    def test_not_eq_children(self):
        child = HTMLNode(
            "p", "hello", None, {"href": "example.com", "target": "_blank"}
        )
        node = HTMLNode(
            "p", "hello", [child], {"href": "amazon.com", "target": "_blank"}
        )
        nod1 = HTMLNode(
            "p", "hello", [node], {"href": "amazon.com", "target": "_blank"}
        )
        self.assertNotEqual(node, nod1)

    def test_props_to_html(self):
        child = HTMLNode(
            "p", "hello", None, {"href": "example.com", "target": "_blank"}
        )
        self.assertEqual(child.props_to_html(), ' href="example.com" target="_blank"')

    def test_props_to_html2(self):
        child = HTMLNode(
            "p", "hello", None, {"href": "example.com", "target": "_blank"}
        )
        self.assertNotEqual(child.props_to_html(), ' href="p" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(
            "a", "Hello, world!", {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com" target="_blank">Hello, world!</a>',
        )


if __name__ == "__main__":
    unittest.main()

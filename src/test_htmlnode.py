import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
    def test_leaf_raw(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
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

class TestParentNode(unittest.TestCase):

    def test_to_html_with_some_none(self):
        parent_node = ParentNode( "p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"), ],)
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_double_parent(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node1 = ParentNode("p", [parent_node])
        parent_node2 = ParentNode("a", [parent_node1])
        self.assertEqual(parent_node2.to_html(), "<a><p><div><span>child</span></div></p></a>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()

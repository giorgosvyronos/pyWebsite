import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD,"www.example.com")
        node1 = TextNode("This is a text node", TextType.IMAGE,"www.example.com")
        self.assertNotEqual(node, node1)
    
    def test_eq_none(self):
        node = TextNode("This is a text node", TextType.IMAGE,"www.example.com")
        node1 = TextNode("This is a text node", TextType.IMAGE,"www.example.com")
        self.assertEqual(node, node1)

    def test_not_eq_none(self):
        node = TextNode("This", TextType.LINK,"www.example.com")
        node1 = TextNode("This is a text node", TextType.IMAGE,"www.example.com")
        self.assertNotEqual(node, node1)

if __name__ == "__main__":
    unittest.main()

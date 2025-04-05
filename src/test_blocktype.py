import unittest

from helpers import markdown_to_blocks
from blocktype import BlockType,block_to_block_type,markdown_to_html_node

class TestHelpers(unittest.TestCase):

    def test_paragraph(self):
        paragraph = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nunc et bibendum consequat, velit eros interdum nunc, vel vulputate eros lectus at nunc. Aenean sed nisl ut eros bibendum maximus. Mauris vitae sapien tincidunt, gravida eros nec, interdum metus.
        Integer tincidunt, velit a vehicula facilisis, metus nulla dignissim nulla, vitae varius nunc nisi eget velit. Ut laoreet sapien a lectus venenatis, sed vehicula libero scelerisque. Vivamus ac lobortis mi.
        """
        blocks = markdown_to_blocks(paragraph)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.paragraph)

    def test_heading(self):
        markdown = """
        # Test Heading
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.heading)

    def test_broken_heading(self):
        markdown = """
        ####### Test Heading
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.paragraph)

    def test_code(self):
        markdown = """
        ```
        int a = 0; return a;
        ```
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.code)

    def test_broken_code(self):
        markdown = """
        ``
        int a = 0; return a;
        ``
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.paragraph)

    def test_quote(self):
        markdown = """
        > How you like them apples.
        > Got him.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.quote)

    def test_broken_quote(self):
        markdown = """
        > How you like them apples.
        Got him.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.paragraph)
    
    def test_unordered_list(self):
        markdown = """
        - One big potato.
        - One large apple.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.unordered_list)

    def test_broken_unordered_list(self):
        markdown = """
        -One big potato.
        -One large apple.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.paragraph)

    def test_ordered_list(self):
        markdown = """
        1. One big potato.
        2. One large apple.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.ordered_list)

    def test_broken_ordered_list(self):
        markdown = """
        2. One big potato.
        1.One large apple.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.paragraph)

    def test_all(self):
        markdown = """
        # Test Heading

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, nunc et bibendum consequat, velit eros interdum nunc, vel vulputate eros lectus at nunc. Aenean sed nisl ut eros bibendum maximus. Mauris vitae sapien tincidunt, gravida eros nec, interdum metus.
        Integer tincidunt, velit a vehicula facilisis, metus nulla dignissim nulla, vitae varius nunc nisi eget velit. Ut laoreet sapien a lectus venenatis, sed vehicula libero scelerisque. Vivamus ac lobortis mi.

        ```
        int a = 0; return a;
        ```

        > How you like them apples.
        > Got him.

        - One big potato.
        - One large apple.

        1. One big potato.
        2. One large apple.
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.heading)
        self.assertEqual(block_to_block_type(blocks[1]),BlockType.paragraph)
        self.assertEqual(block_to_block_type(blocks[2]),BlockType.code)
        self.assertEqual(block_to_block_type(blocks[3]),BlockType.quote)
        self.assertEqual(block_to_block_type(blocks[4]),BlockType.unordered_list)
        self.assertEqual(block_to_block_type(blocks[5]),BlockType.ordered_list)

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

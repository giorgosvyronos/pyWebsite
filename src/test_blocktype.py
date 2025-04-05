import unittest

from helpers import markdown_to_blocks
from blocktype import BlockType,block_to_block_type

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

import unittest

from block import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
  def test_outputs(self):
    markdown = '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''
    blocks = markdown_to_blocks(markdown)
    expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']

    self.assertListEqual(blocks, expected)
    self.assertEqual(len(blocks), 3)
    self.assertEqual(blocks[0], expected[0])

if __name__ == "__main__":
  unittest.main()
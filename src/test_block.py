import unittest

from block import (
  markdown_to_blocks,
  block_to_block_type,
  markdown_to_html_node,
  block_type_code,
  block_type_heading,
  block_type_olist,
  block_type_paragraph,
  block_type_quote,
  block_type_ulist
)

from htmlnode import ParentNode, LeafNode
from textnode import TextNode

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


class TestBlockToBlockType(unittest.TestCase):
  def test_heading(self):
    block = '# This is a heading'
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_heading)

  def test_paragraph(self):
    block = 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.'
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_paragraph)

  def test_quote(self):
    block = '> This is the first list item in a list block\n> This is a list item\n> This is another list item'
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_quote)

  def test_ulist_hyphen(self):
    block = '- This is the first list item in a list block\n- This is a list item\n- This is another list item'
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_ulist)

  def test_ulist_star(self):
    block = '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_ulist)

  def test_olist(self):
    block = '1. This is the first list item in a list block\n2. This is a list item\n3. This is another list item'
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_olist)


class TestMarkdownToHTMLNode(unittest.TestCase):
  def test_paragraph(self):
    markdown = "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    self.assertEqual(
      html,
      '<div><p>This is a paragraph of text. It has some bold and <i>italic</i> words inside of it.</p></div>'
    )

  def test_heading(self):
    markdown = "# My Heading"
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    self.assertEqual(
      html,
      '<div><h1>My Heading</h1></div>'
    )

  def test_code(self):
    markdown = '''
```
def f(x):
  print(x)
```
'''
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    self.assertEqual(
      html,
      '<div><pre><code>\ndef f(x):\n  print(x)\n</code></pre></div>'
    )

  def test_quote(self):
    markdown = '''
> To be
> or not to be!
'''
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    self.assertEqual(
      html,
      '<div><blockquote>To be\nor not to be!</blockquote></div>'
    )

  def test_olist(self):
    markdown = '''
1. one
2. two
'''
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    self.assertEqual(
      html,
      '<div><ol><li>one</li><li>two</li></ol></div>'
    )

  def test_ulist(self):
    markdown = '''
* one
* two
'''
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    self.assertEqual(
      html,
      '<div><ul><li>one</li><li>two</li></ul></div>'
    )

if __name__ == "__main__":
  unittest.main()


  
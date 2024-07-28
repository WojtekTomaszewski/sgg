import unittest

from inline import (
  split_nodes_delimiter,
  extract_markdown_images,
  extract_markdown_links,
  split_nodes_link,
  split_nodes_image,
  text_to_textnodes
)
from textnode import TextNode

class TestSpliteNodesDelimiter(unittest.TestCase):
  def test_code_delimiter(self):
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")
    expected_nodes = [
      TextNode("This is text with a ", "text"),
      TextNode("code block", "code"),
      TextNode(" word", "text"),
    ]
    self.assertEqual(new_nodes, expected_nodes)

  def test_bold_delimiter(self):
    node = TextNode("This is text with a **code block** word", "text")
    new_nodes = split_nodes_delimiter([node], "**", "bold")
    expected_nodes = [
      TextNode("This is text with a ", "text"),
      TextNode("code block", "bold"),
      TextNode(" word", "text"),
    ]
    self.assertEqual(new_nodes, expected_nodes)

  def test_italic_delimiter(self):
    node = TextNode("This is text with a *code block* word", "text")
    new_nodes = split_nodes_delimiter([node], "*", "italic")
    expected_nodes = [
      TextNode("This is text with a ", "text"),
      TextNode("code block", "italic"),
      TextNode(" word", "text"),
    ]
    self.assertEqual(new_nodes, expected_nodes)


class TestExtractMarkdownImages(unittest.TestCase):
  def test_extract_images(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    images = extract_markdown_images(text)
    self.assertListEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])


class TestExtractMarkdownLinks(unittest.TestCase):
  def test_extract_images(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    images = extract_markdown_links(text)
    self.assertListEqual(images, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])


class TestSplitNodesLink(unittest.TestCase):
  def test_spli_nodes_image(self):
    node = TextNode(
      "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
      "text",
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
      new_nodes,
      [
        TextNode("This is text with a link ", "text"),
        TextNode("to boot dev", "link", "https://www.boot.dev"),
        TextNode(" and ", "text"),
        TextNode(
          "to youtube", "link", "https://www.youtube.com/@bootdotdev"
        ),
      ]
    )


class TestSplitNodesImage(unittest.TestCase):
  def test_split_nodes_image(self):
    node = TextNode(
      "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
      "text",
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      new_nodes,
      [
        TextNode("This is text with a link ", "text"),
        TextNode("to boot dev", "image", "https://www.boot.dev"),
        TextNode(" and ", "text"),
        TextNode(
          "to youtube", "image", "https://www.youtube.com/@bootdotdev"
        ),
      ]
    )


  class TestTextToTestNodes(unittest.TestCase):
    def test_split_complex_text(self):
      text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
      nodes = text_to_textnodes(text)
      expected = [
        TextNode("This is ", "text"),
        TextNode("text", "bold"),
        TextNode(" with an ", "text"),
        TextNode("italic", "italic"),
        TextNode(" word and a ", "text"),
        TextNode("code block", "code"),
        TextNode(" and an ", "text"),
        TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", "text"),
        TextNode("link", "link", "https://boot.dev"),
      ]
      self.assertListEqual(nodes, expected)

if __name__ == "__main__":
  unittest.main()
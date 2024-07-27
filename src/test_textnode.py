import unittest

from textnode import TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("My text node", "italic")
    node1 = TextNode("My text node", "italic")
    self.assertEqual(node, node1)

  def test_ne(self):
    node = TextNode("My text node", "bold")
    node1 = TextNode("My text node", "italic")
    self.assertNotEqual(node, node1)

  def test_with_url_ne(self):
    node = TextNode("My text node", "bold", "https://example.com")
    node1 = TextNode("My text node", "italic")
    self.assertNotEqual(node, node1)

  def test_with_url_eq(self):
    node = TextNode("My text node", "bold", "https://example.com")
    node1 = TextNode("My text node", "bold", "https://example.com")
    self.assertEqual(node, node1)


class TestTextNodeToHTMLNode(unittest.TestCase):
  def test_text_node(self):
    text_node = TextNode("text_node", "text")
    html_node = text_node_to_html_node(text_node)
    html = html_node.to_html()
    self.assertEqual(html, "text_node")

  def test_bold_node(self):
    text_node = TextNode("text_node", "bold")
    html_node = text_node_to_html_node(text_node)
    html = html_node.to_html()
    self.assertEqual(html, "<b>text_node</b>")

  def test_italic_node(self):
    text_node = TextNode("text_node", "italic")
    html_node = text_node_to_html_node(text_node)
    html = html_node.to_html()
    self.assertEqual(html, "<i>text_node</i>")

  def test_code_node(self):
    text_node = TextNode("text_node", "code")
    html_node = text_node_to_html_node(text_node)
    html = html_node.to_html()
    self.assertEqual(html, "<code>text_node</code>")

  def test_link_node(self):
    text_node = TextNode("text_node", "link", url="http://example.com")
    html_node = text_node_to_html_node(text_node)
    html = html_node.to_html()
    self.assertEqual(html, "<a href=\"http://example.com\">text_node</a>")

  def test_img_node(self):
    text_node = TextNode("text_node", "image", url="http://example.com")
    html_node = text_node_to_html_node(text_node)
    html = html_node.to_html()
    self.assertEqual(html, "<img src=\"http://example.com\" alt=\"text_node\"></img>")

  def test_not_supported_node(self):
    text_node = TextNode(None, "dummy")
    self.assertRaises(ValueError, text_node_to_html_node, text_node)

if __name__ == "__main__":
  unittest.main()
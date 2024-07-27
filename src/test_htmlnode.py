import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
  def test_node_props_eq(self):
    node = HTMLNode(props={"href": "https://www.google.com"})
    props_html = node.props_to_html()
    self.assertEqual(props_html, " href=\"https://www.google.com\"")

  def test_node_props_eq_2(self):
    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
    props_html = node.props_to_html()
    self.assertEqual(props_html, " href=\"https://www.google.com\" target=\"_blank\"")

  def test_node_props_eq_2(self):
    node = HTMLNode(props={})
    props_html = node.props_to_html()
    self.assertEqual(props_html, "")


class TestLeafNode(unittest.TestCase):
  def test_leaf_node_1(self):
    node = LeafNode("p", "This is a paragraph of text.")
    node_html = node.to_html()
    self.assertEqual(node_html, "<p>This is a paragraph of text.</p>")

  def test_leaf_node_2(self):
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    node_html = node.to_html()
    self.assertEqual(node_html, "<a href=\"https://www.google.com\">Click me!</a>")


class TestParentNode(unittest.TestCase):
  def test_parent_node_eq(self):
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
    html = node.to_html()
    self.assertEqual(html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

  def test_parent_node_nested(self):
    node = ParentNode(
      "p",
      [
        ParentNode("a", [])
      ]
      )
    html = node.to_html()
    self.assertEqual(html, "<p><a></a></p>")


if __name__ == "__main__":
  unittest.main()
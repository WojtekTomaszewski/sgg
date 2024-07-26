import unittest

from textnode import TextNode

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

if __name__ == "__main__":
  unittest.main()
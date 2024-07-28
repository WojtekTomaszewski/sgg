import re

from pprint import pprint

from htmlnode import ParentNode, LeafNode
from inline import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown) -> list[str]:
  splits = markdown.split("\n\n")

  blocks = []
  for split in splits:
    if split == "":
      continue
    blocks.append(split.strip())

  return blocks


def block_to_block_type(block) -> str:
  if re.match(r"^#{1,6}\s{1}\w+", block):
    return block_type_heading
  
  lines = block.split("\n")

  if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
    return block_type_code
  
  if block.startswith(">"):
    for line in lines:
      if not line.startswith(">"):
        return block_type_paragraph
    return block_type_quote
  
  if block.startswith("* "):
    for line in lines:
      if not line.startswith("* "):
        return block_type_paragraph
    return block_type_ulist
  
  if block.startswith("- "):
    for line in lines:
      if not line.startswith("- "):
        return block_type_paragraph
    return block_type_ulist
  
  if block.startswith("1. "):
    i = 1
    for line in lines:
      if not line.startswith(f"{i}. "):
        return block_type_paragraph
      i += 1
    return block_type_olist
  
  return block_type_paragraph


def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)

  div = ParentNode("div", [])

  for block in blocks:
    type = block_to_block_type(block)

    if type == block_type_paragraph:
      div.children.append(paragraph_block_to_node(block))
      continue

    if type == block_type_heading:
      div.children.append(heading_block_to_node(block))
      continue

    if type == block_type_code:
      div.children.append(code_block_to_node(block))
      continue

    if type == block_type_quote:
      div.children.append(quote_block_to_node(block))
      continue

    if type == block_type_olist:
      div.children.append(olist_block_to_node(block))
      continue

    if type == block_type_ulist:
      div.children.append(ulist_block_to_node(block))
      continue
  return div


def paragraph_block_to_node(block):
  inline_nodes = text_to_textnodes(block)
  return ParentNode("p", text_to_children(inline_nodes))

def heading_block_to_node(block):
  hashes, value = block.split(" ", maxsplit=1)
  inline_nodes = text_to_textnodes(value)
  return ParentNode(f"h{len(hashes)}", text_to_children(inline_nodes))

def code_block_to_node(block):
  value = block.strip("```")
  inline_nodes = text_to_textnodes(value)
  code_node = ParentNode("code", text_to_children(inline_nodes))
  pre_node = ParentNode("pre", [code_node])
  return pre_node

def quote_block_to_node(block):
  value_lines = block.replace("> ", "")
  inline_nodes = text_to_textnodes(value_lines)
  return ParentNode("blockquote", text_to_children(inline_nodes))

def olist_block_to_node(block):
  value_lines = block.split("\n")
  value_lines_without_number = list(map(lambda x: x.split(" ", maxsplit=1)[1], value_lines))
  inline_nodes = []
  for value_line in value_lines_without_number:
    inline_nodes.extend(text_to_textnodes(value_line))
  li_nodes = []
  for inline_node in inline_nodes:
    li_nodes.append(ParentNode("li", [text_node_to_html_node(inline_node)]))
  return ParentNode("ol", li_nodes)

def ulist_block_to_node(block):
  value_lines = block.split("\n")
  value_lines_without_number = list(map(lambda x: x.split(" ", maxsplit=1)[1], value_lines))
  inline_nodes = []
  for value_line in value_lines_without_number:
    inline_nodes.extend(text_to_textnodes(value_line))
  li_nodes = []
  for inline_node in inline_nodes:
    li_nodes.append(ParentNode("li", [text_node_to_html_node(inline_node)]))
  return ParentNode("ul", li_nodes)

def text_to_children(text_nodes) -> list[LeafNode]:
  return list(map(text_node_to_html_node, text_nodes))

if __name__ == "__main__":
#   markdown = '''
# # This is a heading

# This is a paragraph of text. It has some **bold** and *italic* words inside of it.

# * This is the first list item in a list block
# * This is a list item
# * This is another list item
# '''
  markdown = '''
**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)
'''
  node = markdown_to_html_node(markdown)

  pprint(node.to_html())
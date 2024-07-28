import re
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != "text":
      new_nodes.append(old_node)
      continue

    split_nodes = []
    split = old_node.text.split(delimiter)
    if len(split) % 2 == 0:
      raise ValueError("Markdown text wrongly formatted")
    
    for index in range(len(split)):
      if split[index] == "":
        continue
      if index % 2 == 0:
        split_nodes.append(TextNode(split[index], "text"))
      else:
        split_nodes.append(TextNode(split[index], text_type))
    new_nodes.extend(split_nodes)
  return new_nodes


def extract_markdown_images(text):
  return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
  return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != "text":
      new_nodes.append(old_node)
      continue
    if old_node.text is None or old_node.text == "":
      continue

    text = old_node.text
    matches = extract_markdown_images(text)
    if len(matches) == 0:
      new_nodes.append(old_node)
      continue
    
    for match in matches:
      split = text.split(f"![{match[0]}]({match[1]})", 1)
      if len(split) != 2:
        raise ValueError("Markdown format error, can't extract image")
      if split[0] != "":
        new_nodes.append(TextNode(split[0], "text"))
      new_nodes.append(
        TextNode(
          match[0],
          "image",
          match[1]
        )
      )
      text = split[1]

    if text != "":
      new_nodes.append(TextNode(text, "text"))
  
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != "text":
      new_nodes.append(old_node)
      continue
    if old_node.text is None or old_node.text == "":
      continue

    text = old_node.text
    matches = extract_markdown_links(text)
    if len(matches) == 0:
      new_nodes.append(old_node)
      continue
    
    for match in matches:
      split = text.split(f"[{match[0]}]({match[1]})", 1)
      if len(split) != 2:
        raise ValueError("Markdown format error, can't extract link")
      if split[0] != "":
        new_nodes.append(TextNode(split[0], "text"))
      new_nodes.append(
        TextNode(
          match[0],
          "link",
          match[1]
        )
      )
      text = split[1]

    if text != "":
      new_nodes.append(TextNode(text, "text"))

  return new_nodes
  

def text_to_textnodes(text):
  init_node = TextNode(text, "text")
  nodes = split_nodes_delimiter([init_node], "*", "italic")
  nodes = split_nodes_delimiter(nodes, "**", "bold")
  nodes = split_nodes_delimiter(nodes, "`", "code")
  nodes = split_nodes_image(nodes)
  nodes = split_nodes_link(nodes)

  return nodes


if __name__ == "__main__":
  text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
  nodes = text_to_textnodes(text)
  pprint(nodes)
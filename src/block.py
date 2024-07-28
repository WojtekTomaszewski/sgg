
def markdown_to_blocks(markdown):
  splits = markdown.split("\n\n")

  blocks = []
  for split in splits:
    if split == "":
      continue
    blocks.append(split.strip())

  return blocks


if __name__ == "__main__":
  markdown = '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''
  blocks = markdown_to_blocks(markdown)
  print(len(blocks))
  print(markdown_to_blocks(markdown))

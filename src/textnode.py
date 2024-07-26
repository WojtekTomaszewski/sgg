class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other: object) -> bool:
    return (
      self.text == other.text
      and self.text_type == other.text_type
      and self.url == other.url
    )
  
  def __repr__(self) -> str:
    return f"TextNode({self.text}, {self.text_type}, {self.url})"
  

if __name__ == "__main__":
  node = TextNode("my text", "bold")

  print(node)
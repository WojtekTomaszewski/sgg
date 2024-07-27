from functools import reduce

class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError

  def props_to_html(self) -> str:
    if not self.props:
      return ""
    return reduce(lambda x, y: x + f' {y[0]}="{y[1]}"', self.props.items(), "")

  def __repr__(self) -> str:
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag=tag, value=value, props=props)

  def to_html(self) -> str:
    if not self.value:
      raise ValueError("leaf node must have a value")
    if self.tag:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    return self.value
  
  def __repr__(self) -> str:
    return f"LeafNode({self.tag}, {self.value}, {self.props})"


if __name__ == "__main__":
  node = HTMLNode()
  props = node.props_to_html()
  node = LeafNode("p", "This is a paragraph of text.")
  props = node.props_to_html()
  print(props)
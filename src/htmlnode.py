from functools import reduce

class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self) -> str:
    raise NotImplementedError

  def props_to_html(self) -> str:
    if self.props is None:
      return ""
    return reduce(lambda x, y: x + f' {y[0]}="{y[1]}"', self.props.items(), "")

  def __repr__(self) -> str:
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

  def to_html(self) -> str:
    if self.value is None:
      raise ValueError("Leaf node must have a value")
    if self.tag:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    return self.value
  
  def __repr__(self) -> str:
    return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
  def __init__(self, tag,  children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self) -> str:
    if self.tag is None:
      raise ValueError("Parent node must have a tag")
    if self.children is None:
      raise ValueError("Parrent node must have childrens")
    
    output = f"<{self.tag}>"
    for child in self.children:
      output += child.to_html()
    output += f"</{self.tag}>"
    return output
  
  def __repr__(self) -> str:
    return f"ParentNode({self.tag}, {self.children}, {self.props})"


if __name__ == "__main__":
  node = ParentNode(
      "p",
      [
        ParentNode("a", [])
      ]
      )

  txt = node.to_html()
  print(txt)
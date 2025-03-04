class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        item = ""
        for key,value in self.props.items():
           item = item + " " f'{key}="{value}"'
        return item
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.props == other.props:
            return True
        return False
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must include a tag")
        if self.children == None:
            raise ValueError("Missing children value")
        item = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            item += child.to_html()
        item = item + f"</{self.tag}>"
        return item

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    

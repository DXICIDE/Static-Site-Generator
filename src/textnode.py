from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "Code"
    LINKS = "link"
    IMAGES = "image"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.NORMAL_TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD_TEXT:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC_TEXT:
                return LeafNode("i", text_node.text)
            case TextType.CODE_TEXT:
                return LeafNode("code", text_node.text)
            case TextType.LINKS:
                return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
            case TextType.IMAGES:
                return LeafNode("img", None, {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
            case _:
                raise Exception("Unknown TextType")
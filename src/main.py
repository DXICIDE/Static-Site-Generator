from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(text_node)

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    print(node.to_html())
    
if __name__ == "__main__":
    main()



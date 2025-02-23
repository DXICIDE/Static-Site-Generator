from textnode import *
from htmlnode import *

def main():
    text_node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(text_node)

    node = HTMLNode("a", "Hi, this is a link")
    print(node) 
if __name__ == "__main__":
    main()



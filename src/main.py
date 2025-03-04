from textnode import *
from htmlnode import *
from split_nodes import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
    
    
if __name__ == "__main__":
    main()



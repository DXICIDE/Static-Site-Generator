from textnode import *
from htmlnode import *
from split_nodes import split_nodes_delimiter, split_nodes_image

def main():
    
    node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", 
                    TextType.NORMAL_TEXT)
    new_nodes = split_nodes_image([node])
    
if __name__ == "__main__":
    main()



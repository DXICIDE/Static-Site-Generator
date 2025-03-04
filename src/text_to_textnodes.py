from src.textnode import *
from src.split_nodes import *


def text_to_textnodes(text):
    node = [TextNode(text, TextType.NORMAL_TEXT)]
    node = split_nodes_delimiter(node, "`", TextType.CODE_TEXT)
    node = split_nodes_delimiter(node, "**", TextType.BOLD_TEXT)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC_TEXT)
    node = split_nodes_links(node)
    node = split_nodes_image(node)
    return node
from enum import Enum
import re
from .split_blocks import markdown_to_blocks
from .htmlnode import *
from .text_to_textnodes import text_to_textnodes
from .textnode import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    split_list = block.splitlines() 
    
    matches = re.match(r"(#{1,6} )\w+", block)
    if matches != None:
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    is_quote = True
    for line in split_list:
        if line.startswith("> ") == False:
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    
    is_unordered_list = True
    for line in split_list:
        if line.startswith("- ") == False:
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST

    is_ordered_list = True
    cnt = 1
    for line in split_list:
        matches = re.match(r"(\d{1,}\. )", line)
        if matches == None:
            is_ordered_list = False
            break
        number = int(matches.group(1).strip(". "))
        if number != cnt:
            is_ordered_list = False
            break
        cnt += 1
    if is_ordered_list:
        return BlockType.ORDERED_LIST 
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    div_node = ParentNode("div", [])
    for block in blocks:
        type = block_to_block_type(block)
        

        match(type):
            case BlockType.PARAGRAPH:
                children = text_to_children(block)
                parent_node = ParentNode("p", children) 
                div_node.children.append(parent_node)

            case BlockType.HEADING:
                cnt = 0
                for character in block:
                    if character == "#":
                        cnt += 1
                        continue
                    break
                block = block[cnt:].strip()
                tag = "h" + str(cnt)

                children = text_to_children(block)
                parent_node = ParentNode(tag, children)
                div_node.children.append(parent_node)

            case BlockType.CODE:
                block = block.replace("```", "").strip()
                block = block + "\n"
                node = TextNode(block, TextType.CODE_TEXT)
                node = node.text_node_to_html_node()
                pre_node = ParentNode("pre", [])
                pre_node.children.append(node)
                div_node.children.append(pre_node)

            case BlockType.QUOTE:    
                block = block.replace("> ", "")
                children = text_to_children(block)
                parent_node = ParentNode("blockquote", children) 
                div_node.children.append(parent_node)

            case BlockType.UNORDERED_LIST:
                block = block.split('\n')
                parent_node = ParentNode("ul", [])
                for item in block:
                    item = item.replace("- ", "")
                    children = text_to_children(item)
                    list_node = ParentNode("li", children)
                    parent_node.children.append(list_node)
                div_node.children.append(parent_node)

            case BlockType.ORDERED_LIST:
                block = block.split('\n')
                parent_node = ParentNode("ol", [])
                cnt = 1
                for item in block:
                    replace = str(cnt) + ". "
                    item = item.replace(replace, "")
                    children = text_to_children(item)
                    list_node = ParentNode("li", children)
                    parent_node.children.append(list_node)
                    cnt = int(cnt) + 1
                div_node.children.append(parent_node)

            case _:
                raise Exception("Unknown BlockType")
    
    return div_node

def text_to_children(block):
    leaf_nodes = []
    block = block.replace("\n", " ")
    nodes = text_to_textnodes(block)
    for node in nodes:
        leaf_nodes.append(node.text_node_to_html_node())
    return leaf_nodes
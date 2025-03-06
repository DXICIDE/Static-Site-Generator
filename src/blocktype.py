from enum import Enum
import re

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
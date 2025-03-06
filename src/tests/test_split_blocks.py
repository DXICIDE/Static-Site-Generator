import unittest

from src.split_blocks import markdown_to_blocks
from src.blocktype import block_to_block_type, BlockType



class TestBlocks(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
   
    def test_block_type_paragpraph(self):
        
        block = "This is **bolded** paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)    

    def test_block_type_unordered_list(self):
        
        block =  "- This is a list\n- with items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)    
    
    def test_block_type_code(self):
        
        block =  "```This is a list with items```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)   

    def test_block_type_not_code(self):
        
        block =  "```This is a list with``` items"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)  

    def test_block_type_quote(self):
        
        block =  "> This is a list\n> with items"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)  

    def test_block_type_heading(self):
        
        block =  "## This is a list with items"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_block_type_ordered_list(self):
        
        block =  "1. This is a list\n2. with items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_type_ordered_list_wrong_nmbr(self):
        
        block =  "1. This is a list\n1. with items"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_type_ordered_list_wrong_nmbr2(self):
        
        block =  "1. This is a list\n3. with items"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from split_nodes import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.NORMAL_TEXT)
        self.assertNotEqual(node, node2)    

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
        self.assertEqual(node, node2)   

    def test_TextNode_to_html_bold(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node.text_node_to_html_node(), LeafNode("b", "This is a text node"))

    def test_TextNode_to_html_normal(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        self.assertEqual(node.text_node_to_html_node(), LeafNode(None, "This is a text node"))
        
    def test_TextNode_to_html_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertEqual(node.text_node_to_html_node(), LeafNode("i", "This is a text node"))

    def test_TextNode_to_html_code(self):
        node = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertEqual(node.text_node_to_html_node(), LeafNode("code", "This is a text node"))
    
    def test_TextNode_to_html_links(self):
        node = TextNode("This is a text node", TextType.LINKS, "https://www.boot.dev")
        self.assertEqual(node.text_node_to_html_node(), LeafNode("a", "This is a text node", {"href": "https://www.boot.dev"}))

    def test_TextNode_to_html_images(self):
        node = TextNode("some link to a img", TextType.IMAGES, "https://www.boot.dev")
        self.assertEqual(node.text_node_to_html_node(), LeafNode("img", None, {"src": "https://www.boot.dev", "alt": "some link to a img"}))

    def test_textnode(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]            
        )

    def test_boldnode(self):
        node = TextNode("This is text with a **bold block** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]            
        )
    
    def test_italicnode(self):
        node = TextNode("This is text with a _italic block_ word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("italic block", TextType.ITALIC_TEXT),
            TextNode(" word", TextType.NORMAL_TEXT),
        ]            
        )


if __name__ == "__main__":
    unittest.main()

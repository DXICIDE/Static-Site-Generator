import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_links


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
    
    def test_node_attribute_error(self):
        with self.assertRaises(AttributeError):
            node = TextNode("", TextType.HEADER)

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL_TEXT),
                TextNode(
                "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
        
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
        ],
        new_nodes,
    )
        
    def test_split_image_and_rest(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and the rest",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL_TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and the rest", TextType.NORMAL_TEXT),
        ],
        new_nodes,
    )
    
    def test_split_image_with_nothin(self):
        node = TextNode("", TextType.NORMAL_TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([], new_nodes)
        
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual( 
            [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode(
            "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"
            ),
        ], 
        new_nodes
        )

    def test_split_one_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual( 
            [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
        ], 
        new_nodes
        )

    def test_split_link_and_the_rest(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and the rest",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual( 
            [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and the rest", TextType.NORMAL_TEXT),
        ], 
        new_nodes
        )
    def test_split_no_link_and_the_rest(self):
        node = TextNode(
            "This is text with a link [to boot dev]() and the rest",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual( 
            [
            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
            TextNode("to boot dev", TextType.LINKS, ""),
            TextNode(" and the rest", TextType.NORMAL_TEXT),
        ], 
        new_nodes
        )

if __name__ == "__main__":
    unittest.main()

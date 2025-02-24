import unittest

from htmlnode import LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_Leaf_node(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>') 
    
    def test_all_leaf_node_attributes(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>') 

    def test_none_tag_leaf_node(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), "Click me!")

if __name__ == "__main__":
    unittest.main()

import unittest

from src.htmlnode import ParentNode, LeafNode, HTMLNode

class TestParentNode(unittest.TestCase):
    
    def test_parent_node(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_node_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_node_with_parent_children(self):
        node = ParentNode(
        "p",
        [
            ParentNode(
            "p",
            [
                LeafNode("b", "Hello"),
                LeafNode(None, "NotHello"),
            ],
            ),
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), "<p><p><b>Hello</b>NotHello</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_props_node(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ], {"href": "https://www.google.com"}
        )
        self.assertEqual(node.to_html(), '<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

if __name__ == "__main__":
    unittest.main()
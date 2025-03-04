import unittest

from htmlnode import *


class TestHtmlNode(unittest.TestCase):
    def test_html_node(self):
        node = HTMLNode("a", "Hi, this is a paragraph", None ,{"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"') 
    
    def test_multiple_html_node(self):
        node = HTMLNode("a", "Hi, this is a paragraph", None ,{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"') 

    def test_none_html_node(self):
        node = HTMLNode("p", "Hi, this is a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hi, this is a paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()

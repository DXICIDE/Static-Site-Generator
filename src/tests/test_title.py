import unittest

from src.main import extract_title


class TestTitle(unittest.TestCase):
    def test_title_basic(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello") 
    def test_title_whitespace(self):
        title = extract_title("#    Hello   ")
        self.assertEqual(title, "Hello")
    def test_title_middle(self):
        title = extract_title("""
> This is a
# Title in the middle
                              
this is paragraph text

""")
        self.assertEqual(title, "Title in the middle")
    def test_title_multiple(self):
        title = extract_title("""
> This is a
# Title in the middle
                              
# Also a title
# Another?
# Four in a row?

""")
        self.assertEqual(title, "Title in the middle")


        

if __name__ == "__main__":
    unittest.main()

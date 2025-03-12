from .split_nodes import split_nodes_delimiter, split_nodes_image
from .text_to_textnodes import *
from .blocktype import *

def main():
    
    md = """
```
This is **bolded** paragraph
text in a p
tag here
```

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)
    #self.assertEqual(
    #    html,
    #    "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    #)
    
if __name__ == "__main__":
    main()



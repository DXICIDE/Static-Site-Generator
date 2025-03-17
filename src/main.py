from .split_nodes import split_nodes_delimiter, split_nodes_image
from .text_to_textnodes import *
from .blocktype import *
import os
import shutil

def main():
    folder_cleanup()
    recursive_copy("static", "public")
    generate_page("content/index.md", "template.html" , "public/index.html")
    generate_page("content/blog/glorfindel/index.md", "template.html" , "public/blog/glorfindel/index.html")
    generate_page("content/blog/tom/index.md", "template.html" , "public/blog/tom/index.html")
    generate_page("content/blog/majesty/index.md", "template.html" , "public/blog/majesty/index.html")
    generate_page("content/contact/index.md", "template.html" , "public/contact/index.html")

def folder_cleanup():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")

def recursive_copy(source_dir, dest_dir):
    if os.path.exists(source_dir):
        dir_list = os.listdir(source_dir)
        for item in dir_list:
            source_item = os.path.join(source_dir, item)
            dest_item = os.path.join(dest_dir, item)
            if os.path.isfile(source_item):
                shutil.copy(source_item, dest_item)
                print(f"Copied file: {source_item} -> {dest_item}")
            else:
                os.mkdir(dest_item)
                print(f"Created directory: {dest_item}")
                recursive_copy(source_item, dest_item)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            output = line.replace("# ", "")
            return output.strip()
    raise Exception("No title")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    file = open(from_path, "r")
    content = file.read()
    title = extract_title(content)
    file.close()

    file_template = open(template_path, "r")
    content_template = file_template.read()
    file_template.close()

    content = markdown_to_html_node(content)
    content = content.to_html()

    content_template = content_template.replace("{{ Title }}", title)
    content_template = content_template.replace("{{ Content }}", content)

    file = dest_path
    dest_path = os.path.dirname(dest_path) 
    print(dest_path)
    os.makedirs(dest_path, 0o777, True)
    f = open(file, "a")
    f.write(content_template)
    f.close()

if __name__ == "__main__":
    main()


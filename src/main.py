from .split_nodes import split_nodes_delimiter, split_nodes_image
from .text_to_textnodes import *
from .blocktype import *
import os
import shutil

def main():
    folder_cleanup()
    recursive_copy("static", "public")
    yo = extract_title("# Hello f ")
    print(yo)

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
    
if __name__ == "__main__":
    main()


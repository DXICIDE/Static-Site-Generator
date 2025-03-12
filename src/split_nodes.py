from .textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        result = []

        while delimiter in text:
            start_idx = text.find(delimiter)
            if start_idx > 0:
                result.append(TextNode(text[:start_idx], TextType.NORMAL_TEXT))
            end_idx = text.find(delimiter, start_idx + len(delimiter))
            if end_idx == -1:
                raise Exception(f"No closing delimiter {delimiter} found")
            content = text[start_idx + len(delimiter):end_idx]
            result.append(TextNode(content, text_type))

            text = text[end_idx + len(delimiter):]

        if text:
            result.append(TextNode(text, TextType.NORMAL_TEXT))
        
        new_nodes.extend(result)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        
        text = node.text       
        if text == "":
            continue
        
        if extract_markdown_images(node.text) == []:
            result.append(node)
            continue
        

        images = extract_markdown_images(text)
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            result.append(TextNode(sections[0], TextType.NORMAL_TEXT))
            result.append(TextNode(image[0], TextType.IMAGES, image[1])),
            text = sections[1]
        
        if text != "":
            result.append(TextNode(text, TextType.NORMAL_TEXT))  
    return result

def split_nodes_links(old_nodes):
    result = []
    for node in old_nodes:
        
        text = node.text       
        if text == "":
            continue
        
        if extract_markdown_links(node.text) == []:
            result.append(node)
            continue
        

        links = extract_markdown_links(text)
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            result.append(TextNode(sections[0], TextType.NORMAL_TEXT))
            result.append(TextNode(link[0], TextType.LINKS, link[1])),
            text = sections[1]
        
        if text != "":
            result.append(TextNode(text, TextType.NORMAL_TEXT))  
    return result
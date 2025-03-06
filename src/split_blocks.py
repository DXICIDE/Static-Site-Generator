def markdown_to_blocks(markdown):
    output = []
    markdown = markdown.split("\n\n")
    for mark in markdown:
        mark = mark.strip()
        if mark == "":
            continue
        output.append(mark)
    return output
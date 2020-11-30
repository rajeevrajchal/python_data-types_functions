def add_tag(tag, element):
    return (f"<{tag}>{element}</{tag}>")

print(add_tag('i', 'Python'))
print(add_tag('b', 'Python Tutorial'))
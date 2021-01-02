from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import requests


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    output = []  
    for line in visible_texts:
        line = line.strip()
        line = line.replace("\n", "")
        output.append(line.strip())

    output_2 = []
    black_list = set(["|", "»", "©", "?"])
    for text in output:
        if text:
            if all([i not in text for i in black_list]):
                output_2.append(text + "\n")
    return " ".join(output_2)
# html = urllib.request.urlopen('https://docs.python.org').read()
html = requests.get('https://docs.python.org').content
print(text_from_html(html))
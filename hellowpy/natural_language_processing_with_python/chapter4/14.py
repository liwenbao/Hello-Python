import nltk
from nltk.corpus import gutenberg

def load_text():
    return gutenberg.words('austen-emma.txt')

def novel10(text):
    pos90 = int(len(text)*9/10)
    set90 = set(text[:pos90])
    # print(len(text), pos90)
    return (w for w in text[pos90:] if w not in set90)

text = load_text()
print(set(novel10(text)))

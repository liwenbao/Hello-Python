
def find_nouse_words1(text, worddic):
    wordset = set(worddic)
    return [w for w in set(text) if w not in wordset]

def find_nouse_words2(text, worddic):
    return set(text).difference(set(worddic))

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import words

onuse_words = find_nouse_words2(gutenberg.words('austen-emma.txt'), words.words('en'))
print(len(onuse_words))

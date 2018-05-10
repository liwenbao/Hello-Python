import nltk
from nltk.corpus import state_union 

fid = '1945-Truman.txt'

def shorten(text, n):
    fq = nltk.FreqDist(text)
    sorted_words = sorted((w for w in fq), key=fq.freq, reverse = True)
    topn = set(sorted_words[:n])
    return [w for w in text if w not in topn]

text = state_union.words(fid)
text = shorten(text, 3)
print(' '.join(text))
    

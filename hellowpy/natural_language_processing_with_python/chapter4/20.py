import nltk

def sort_by_freq(words):
    fq = nltk.FreqDist(words)
    return sorted(set(words), key = fq.freq, reverse = True)

s = input('please input your words list: ')
print('you enter', s)
print('sort result is', sort_by_freq(s.split()))

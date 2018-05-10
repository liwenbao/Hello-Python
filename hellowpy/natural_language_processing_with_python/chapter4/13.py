_max_word_len = 6
word_vowels = [[set() for j in range(_max_word_len)]for i in range(_max_word_len)]

def index_word(w):
    l = len(w)
    if l > _max_word_len:
        raise IndexError
    v = sum(1 for c in w if c in 'aeuio')   # 使用iterable对象进行sum，而不要先生成[]。
    word_vowels[l-1][v-1].add(w)

sent = 'this is a text for tesing'.split()
for w in sent:
    index_word(w)

print(word_vowels)

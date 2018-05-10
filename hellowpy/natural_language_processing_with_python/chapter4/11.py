sent1 = 'this is a text'.split()
sent2 = sent1
sent2.append('.')
print(sent1)    # ['this', 'is', 'a', 'text', '.']
print(sent2)    # ['this', 'is', 'a', 'text', '.']

sent3 = sent1[:]
sent3[4] = '!'
print(sent1)    # ['this', 'is', 'a', 'text', '.']
print(sent2)    # ['this', 'is', 'a', 'text', '.']
print(sent3)    # ['this', 'is', 'a', 'text', '!']

text1 = ['this is a text'.split(), 'this text is used to test'.split()]
text2 = text1[:]
text2[0] = 'this is a new text'.split()
print(text1)    # [['this', 'is', 'a', 'text'], ['this', 'text', 'is', 'used', 'to', 'test']]
print(text2)    # [['this', 'is', 'a', 'new', 'text'], ['this', 'text', 'is', 'used', 'to', 'test']]

text2[1][5] = 'testing'
print(text1)    # [['this', 'is', 'a', 'text'], ['this', 'text', 'is', 'used', 'to', 'testing']]
print(text2)    # [['this', 'is', 'a', 'new', 'text'], ['this', 'text', 'is', 'used', 'to', 'testing']]

import copy

text3 = copy.deepcopy(text1)
text3[1][5] = 'test'
print(text1)    # [['this', 'is', 'a', 'text'], ['this', 'text', 'is', 'used', 'to', 'testing']]
print(text3)    # [['this', 'is', 'a', 'text'], ['this', 'text', 'is', 'used', 'to', 'test']]

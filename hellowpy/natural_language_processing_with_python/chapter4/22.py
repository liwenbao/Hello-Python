import operator
from operator import itemgetter

words = ['python', 'is','fun']
print(sorted(words, key=itemgetter(1)))     #按照第二个字母排序
print(sorted(words, key=itemgetter(-1)))    #按照尾字母排序
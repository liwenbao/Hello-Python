def Translate1():
    words = ['is', 'NLP', 'fun', '?']
    temp = words[0]
    words[0] = words[1]
    words[1] = temp
    words[3] = '!'
    print(words)

def Translate2():
    words = ['is', 'NLP', 'fun', '?']
    words[0], words[1], words[3] = words[1], words[0], '!'
    print(words)

Translate1()
Translate2()


import re

def sent_normalize1(sent):
    return ' '.join(sent.split())

def sent_normalize2(sent):
    sent = re.sub(r'^ *| *$', '', sent)
    return re.sub(r' {2,}', ' ', sent)

print(sent_normalize1('  abc  '))
print(sent_normalize1('  abc de  f   gh  '))
print(sent_normalize2('  abc  '))
print(sent_normalize2('  abc de  f   gh  '))

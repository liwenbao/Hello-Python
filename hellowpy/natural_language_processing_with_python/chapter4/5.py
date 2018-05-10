# python 3.x 没有cmp方法

import operator as op

def cmp(a, b):
    if op.eq(a, b):
        return 0
    elif op.gt(a, b):
        return 1
    else:
        return -1

print('cmp(1, 1)', cmp(1, 1))
print('cmp(1, 2)', cmp(1, 2))
print('cmp(2, 1)', cmp(2, 1))

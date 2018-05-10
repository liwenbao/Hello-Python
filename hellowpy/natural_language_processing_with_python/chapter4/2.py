str = 'monty python'
list = ['monty', 'python']
tuple = ('monty', 'python')

print('%-20s%d' % ('len(str)',len(str)))
print('%-20s%d' % ('len(list)',len(list)))
print('%-20s%d' % ('len(tuple)',len(tuple)))
print()

print('%-20s%d' % ("str.index('p')",str.index('p')))
print('%-20s%d' % ("list.index('python')",list.index('python')))
print('%-20s%d' % ("tuple.index('python')",tuple.index('python')))
print()

print('%-20s%s' % ("sorted(str)", sorted(str)))
print('%-20s%s' % ("sorted(list)", sorted(list)))
print('%-20s%s' % ("sorted(tuple)", sorted(tuple)))
print()

print(hash(tuple))
print(hash(list))   # TypeError: unhashable type: 'list'

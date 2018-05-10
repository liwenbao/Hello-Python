def n_grame(words, n):
    return [tuple(words[j] for j in range(i, i+n))  # 每个元组从i开始，取n个词
            for i in range(len(words)-n+1)]         # len(words)-n+1个元组

words = ['a','b','c','d','e','f','g']
print(n_grame(words, 3))

print(n_grame(words, 1))            # 支持极端情况n=1

print(n_grame(words, len(words)))   # 支持极端情况n=len(words)

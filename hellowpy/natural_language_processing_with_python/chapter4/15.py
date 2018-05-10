import nltk
import re

def word_tokenize(raw):
    return re.sub(r'\W+', ' ', raw).split()
    #return re.findall(r' (\w+) ', raw)

def get_freqdist(words):
    return nltk.FreqDist(words)

def show_wordfreq(freqdist):
    for w in sorted((w for w in freqdist), key = str.lower):
        print('%-15s%2.2f%%' % (w, freqdist.freq(w)*100))

raw = '''If the second argument is omitted, the super object returned is unbound. If the second argument is an object, isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type) must be true (this is useful for classmethods).

There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.

The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).

For both use cases, a typical superclass call looks like this:'''

words = word_tokenize(raw)
fd = get_freqdist(words)
show_wordfreq(fd)

sent = ['python','is','fun']
print(sorted(sent, key = len))
print(sorted(sent, key = lambda w:len(w)))

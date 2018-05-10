def iftest(o):
    if o:
        return True
    else:
        return False

print(iftest(0))            # False
print(iftest(1))            # True
print(iftest(-1))           # True
print(iftest(tuple()))      # False
print(iftest(tuple('1',)))  # True

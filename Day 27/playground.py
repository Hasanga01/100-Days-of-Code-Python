def add(*args):
    a = 0
    for n in args:
        a += n
    return a


k = add(2, 3, 4, 5, 1)
print(k)

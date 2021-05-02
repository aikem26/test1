def mysum(r, *args):
    for num in args:
        r += num
    return r

print(mysum(3, 5, 6, 0, 1))
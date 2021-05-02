#def mysum(a, b, c):
    #return a + b +c

#print(mysum(5, 2, 8))

def mysum(r, lst):
    for num in lst:
        r += num
    return r

print(mysum(3, [5, 2]))
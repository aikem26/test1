m = [5, 2, 5, 3, 7, 4, 3, 1, 4, 6]
k = []

while m: #for num in m:
    c = m[0] #num
    for e in m:
        if c > e:
            c = e
    k.append(c)
    m.remove(c)
    print(m)
    print(k)

print(k)


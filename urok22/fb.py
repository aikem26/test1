def fb(n):
    if n <= 1:
        return 1
    else:
        return fb(n-1) + fb(n-2)

#print(fb(4))
n = 10
for i in range(n):
    print(fb(i))

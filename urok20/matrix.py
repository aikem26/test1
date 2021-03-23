a = [
    [5, 2, 4, 6, 2],
    [5, 2, 4, 6, 2],
    [5, 2, 4, 6, 2],
    [5, 2, 4, 6, 2],
]

b = []

for element_list in a:
    b.append([])
    for num in element_list:
        c = num * 10
        b[-1].append(c)
        #for i in range(c):
            #print(f"hello {i} - {c}")
            #for j in range(i*100):
                #print(f"hi {i} {j}")

print(b)

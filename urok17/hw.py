# Задание № 1
a = list(range(1000))
b = []
q = 0
for num in a:
    if num % 17 == 0:
        b.append(num)
        q += 1
print(b)
print(q)


# Задание № 2
nums = []
count = 0
for i in range(1000):
    if i % 17 == 0 and i % 2 == 0:
        nums.append(i)
        count += 1
print(nums)
print(count)

# Задание № 3
a = [5, 7, -35, 34, 0, 4]
b = []
c = []

m = len(a)

i = 0
while i < m:
    r = a[i] * 5
    b.append(r)
    i += 1

for j in range(m):
    d =  a[j] * 10
    c.append(d)

print(b)
print(d)









    

    
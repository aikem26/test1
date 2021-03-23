# Задание №1
password_list = ["password", 123456, 12345678, "qwerty", "abc123", "monkey", 1234567]
while True:
    print("Введите пароль:")
    a = input()
    if a == "password":
        break
    if a == "123456":
        break
    if a == "12345678":
        break
    if a == "qwerty":
        break
    if a == "abc123":
        break
    if a == "monkey":
        break
    if a == "1234567":
        break
    continue

# Задание №2
for i in range(23, 87, 8):
    print(i)

# Задание №3
for i in range(57):
    print("I LOVE PYTHON")

# Задание №4
i = 1
while i > 0:
    print("I LOVE YOU", i)
    if i == 57:
        break
    i += 1

# Задание №5 
people = ["Regina", "Erkaiym", "Begaiym"]
country = ["Germany", "France", "Spain", "Portugal", "Holland", "Japan", "South Korea", "Singapore"]
for name in people:
    for c in country:
        print(name, "lives in", c)

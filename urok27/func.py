def mydivision(num_1, num_2):
    if num_2 == 0:
        raise ZeroDivisionError("На 0 делить нельзя!")
    return num_1 / num_2

a = int(input())
b = int(input())
print(mydivision(a, b)) # На 0 делить нельзя

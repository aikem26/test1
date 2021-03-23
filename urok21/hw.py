# Задание № 1

# Задание № 2
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

print(fizz_buzz(15))

# Задание № 3

# Задание № 4
def is_year_leap(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Високосный год") 
    else:
        print("Обычный год") 

print(is_year_leap(2020))


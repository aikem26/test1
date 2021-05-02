try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Операция не удалась")
    print("На ноль делить нельзя")
except ValueError:
    print("Произошла ошибка")
    print("Неверный ввод")
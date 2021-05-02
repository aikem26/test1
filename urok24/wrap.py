def mysum():
    print(5 + 3)

def test_1():
    print("test")

def wrap(myfunction):
    print("Дополнительный текст")
    myfunction()
    print("Вызов функции завершен")

wrap(mysum)
wrap(test_1)
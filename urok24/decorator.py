
def mydecorator(my_f):
    def wrap():
        print("Начало от декоратора")
        print(f"Сейчас вызовится функция (my_f)")
        my_f()
        print("Декоратор закончил свое исполнение")
    return wrap

@mydecorator
def myfunction():
    print("Основная функция запущена")
    print("Основная функция запущена")
    print("Основная функция запущена")

mydecorator(myfunction)()
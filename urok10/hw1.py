
a = int(input("Введите сторону а: "))
b = int(input("Введите сторону б: "))
c = int(input("Введите сторону с: ")) 
netto_w = int(input("Введите вес товара(нетто): ")) 
quantity = int(input("Введите количество товара: "))

V = round(((a / 100) * (b / 100) * (c / 100)), 2)
brutto_w = int(netto_w + ((netto_w * 15) / 100))
price = 650

if (V * quantity <= 1) and (brutto_w * quantity) <= 55:
    print("Стоимость перевозки:",price, "сом")
else:
    print("Стоимость перевозки:",price * quantity, "сом")








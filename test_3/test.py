class Beauty:
    is_sold = False

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sell(self, money_object):
        if self.is_sold:
            raise Exception("Товар уже продан")
        
        self.is_sold = True
        money_object.money += self.price
        return money_object

class Cream(Beauty):
    volume = 1000
    type_of = "Увлажняющий"

    def __init__(self, price, model):
        name = f"Beuty {model}"
        super().__init__(name=name, price=price)

class SPF(Cream):
    def __init__(self, price, model):
        name = f"SPF {model}"
        super(Cream, self).__init__(name=name, price=price)

class Mascara(Beauty):
    def __init__(self):
        name = "Maybelinne Lash Sensation"
        price = 10.95
        super().__init__(name,price)

class Money:
    money = 0

mascara_1 = Mascara()
mascara_2 = Mascara()

cream_1 = Cream(29.75, 'Aqua Intense')
cream_2 = Cream(34.99, 'Clinique')
cream_3 = Cream(12.90, 'CeraVe')


SPF_1 = SPF(18.50, 'Vichy spf50')

m = Money()

print(m.money)

m = cream_2.sell(m)
print(cream_2.is_sold)
print(m.money)

m = mascara_1.sell(m)
print(mascara_1.is_sold)
print(m.money)

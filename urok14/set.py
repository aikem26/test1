a = {12, 34, 52} #набор уникальных значений
print(a)
print(type(a)) #невозможно добавить одинаковый элемент, напр 34, 34 будет просто перезапишен

a.add(42)
print(a) 
print(len(a))

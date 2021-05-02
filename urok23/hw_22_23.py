
def rev(num):
    if num < 10:
        return str(num)
    else:
        str_num = str(num)
        digit = str_num[-1]
        new_num = str_num[:-1]
        return digit + rev(int(new_num), )

print(rev(179))



from random import randint

def generate_list_with_random_numbers(length):
    lst = [randint(1, 10) for _ in range(length)]
    return lst

def generate_list_with_squared_numbers(lst):
    new_lst = list(map(lambda x: x ** 2, lst))
    return new_lst

if __name__ == "__main__":
    num = int(input())
    a = generate_list_with_random_numbers(num)
    b = generate_list_with_squared_numbers(a) 
    print(a)
    print(b)


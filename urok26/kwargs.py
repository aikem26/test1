def test(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    

test(4, 2, 3, 22, a=4, b=2, c= "hi")
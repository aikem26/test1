def myprint(n):
    print(n, end="\t")
    if n > 5:
        print(n, "> 5")
    else:
        print(n, "<= 5")

    if n > 0:
        myprint(n - 1)
    
myprint(10)

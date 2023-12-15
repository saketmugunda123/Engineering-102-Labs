c = 50

def outer():
    c = 55

    def inner():
        global c
        c = 60

    inner()
    print(c)

outer()
print(c)


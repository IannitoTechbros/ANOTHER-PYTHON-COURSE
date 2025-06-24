def outer():
    x = "local"
    def inner():
        nonlocal x  #grab the parent local variable scope
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer", x)


outer()
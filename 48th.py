#positional parameters


def say_hello(name, emoji):
    print(f"hello {name} {emoji}")


#positional arguments

say_hello("Ian", "😂")


#keyword arguments

say_hello(emoji="😂", name="Ian")


#default parameters

def say_hello(name = "Ian", emoji="😂"):
    print(f"hello {name} {emoji}")


say_hello()


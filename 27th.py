dictionary = {
    "basket" : 12345,
    "greet" : "Hello"
}


print("basket" in dictionary)

print("user" in dictionary)


print("basket" in dictionary.keys())

print("basket" in dictionary.values())


dictionary2 = dictionary.copy()

print(dictionary2)


dictionary2.pop("basket")

print(dictionary2)


#lets talk about loops

#an iterable is a word/object that can be looped over

for item in "Zero":
    print(item[0])


for item in (1, 2, 3, 4, 5, 6):
    for x in ["a", "b", "c", "d"]:
        print(1, "c")


#an iterable can be a list , dictionary, tuple, set, string - which means they can be iterated....one by one


#How to iterate through dictionaries

users = {
    "name": "Golem",
    "age": 5006,
    "can_swim": False
}

for item in users:
    print(item)

for item in users.items():
    print(item)

for item in users.values():
    print(item)


for item in users.keys():
    print(item)



#Exercise Check for duplicates in a list

some_list = ["a", "b", "c", "d", "e", "f", "b", "a"]

duplicate = []


for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in duplicate:
            duplicate.append(letter)


print(duplicate)


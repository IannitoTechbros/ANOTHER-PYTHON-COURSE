my_tuple = (1, 2, 3, 4, 5, 6)


new_tuple = my_tuple[:]  #copy new tuple

print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5, 6)

print(*other)


print(my_tuple.count(5)) #counts how many times a value appears in a tuple

print(len(my_tuple))  #see length of the values in a tuple
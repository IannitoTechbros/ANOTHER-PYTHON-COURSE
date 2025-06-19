#lets look at sets

#They are unordered collection of unique values

my_set = {1, 2, 3, 4, 5}

my_set2 = {1, 2, 3, 4, 5, 5}

print(my_set)
print(my_set2)  #there can't be duplicates in sets

#we can convert lists to sets

my_list = [1, 2, 3, 4, 5, 6]

my_set3 = set(my_list)

print(my_set3)


print(len(my_set3))


my_set4 = my_set3.copy()

print(my_set4)
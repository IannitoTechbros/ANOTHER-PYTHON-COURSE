my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

your_set = {4, 5, 6, 7, 8, 9, 10}


print(my_set.difference(your_set)) #any duplicates are removed and left with values that dont repeat in both sets

print(my_set.discard(5)) #removes a specific value

print(my_set)


my_set.difference_update(your_set)

print(my_set)


print(my_set.intersection(your_set))


print(my_set.isdisjoint(your_set))  #returns True of False based on if there is anything similar

print(my_set.union(your_set)) #join the two sets but removes the duplicates

print(my_set.issubset(your_set))

print(my_set.issuperset(your_set))


print(your_set.issuperset(my_set))
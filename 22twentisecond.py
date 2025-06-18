first_list = ["Ian", "Mutugi", "Kinyua", "Emilio"]


print(len(first_list))

first_list.append("Moreen") #add an item at the end

print(first_list)


first_list.sort() #sort 

print(first_list)


second_list = first_list.copy() #copy another list

print(second_list)


second_list.pop() #remove the last item

print(second_list)


second_list.insert(4, "Mutugi")  #insert an item inside a list at a particular index

print(second_list)


second_list.extend([10, 100, 1000])  #add another list to the original list


print(second_list)

third_list = second_list.copy()

third_list.remove(100)  #remove a specific value in a list

print(third_list)


third_list.clear() #remove everything

print(third_list)


basket = ["a", "b", "c", "d", "e"]

new_basket = basket[:] #copy of a new list

print(new_basket)


new_basket.reverse()

print(new_basket)
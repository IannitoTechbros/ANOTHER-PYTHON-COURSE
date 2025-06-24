# def highest_even(li):
#     for digit in li:
#         if digit % 2 == 0:
#             print(digit.max())



def highest_even(li):
    evens = []
    for digit in li:
        if digit % 2 == 0 :
            evens.append(digit)
    return max(evens)
        

print(highest_even([10,2,3,4,8,11]))


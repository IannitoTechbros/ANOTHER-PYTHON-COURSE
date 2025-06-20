#lets talk about data types:

number = 2345

floater = 9.667


number1 = input("Enter a number: ")

float1 = input("Enter a float: ")


def calculator(number1, float1):
    result = float(number1) + float(float1)
    return result


print(calculator(number1, float1))



print(type(number))

print(type(number ** number))   

print( 2 // 4) #floors the result

print(5 % 4)  #remainder
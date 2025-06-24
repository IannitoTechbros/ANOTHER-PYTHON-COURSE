#lets talk about return


def addition(num1, num2):
    result = num1 + num2
    print(result)



addition(1, 3)


def addition2(num1, num2):
    return num1 + num2

print(addition2(1, 3))


#a function either modifies something or returns something
#should do one thing really welll

total = addition2(4, 5)

print(total)
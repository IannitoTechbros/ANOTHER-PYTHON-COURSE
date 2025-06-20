#while loops


# i = 0 

# while i < 10:
#     i += 1
#     print(f"Ruto must go: {i}")


#you can use break to break out of while loops



fifty = 0

while fifty < 5 :
    fifty += 1
    print("fifty")
else:
    print("I'm done")


#while statements can also have else partsi = 0 

# while i < 10:
#     i += 1
#     print(f"Ruto must go: {i}")


while True:
    response = input("Input your password: ")
    if response == "Bye":
        print("correct password")
        break
    else:
        print("Incorrect password")
for i,char in enumerate("Hellooo"):
    print(i, char)


#enumerate is very useful when you need the index counter of the object being enumerated

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f"The index of 50 is: {i}")


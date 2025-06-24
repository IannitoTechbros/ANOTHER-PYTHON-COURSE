#Error handling

while True:
    try:
        age = int(input("What is your age: "))
        print(age)
    except ValueError:
        print("Enter a number")
    except ZeroDivisionError:
        print("Really boy")
    else:
        print("Good boy")
        break






def summit(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter numbers {err}")
    else:
        print("Thank you")

 

print(summit(1, "4"))




while True:
    try:
        age = int(input("What is your age: "))
        print(age)
    except ValueError:
        print("Enter a number")
        continue
    except ZeroDivisionError:
        print("Really boy")
        break
    else:
        print("Good boy")
        break
    finally:
        print("Ok but im finally done")
    
    print("Can you hear me")
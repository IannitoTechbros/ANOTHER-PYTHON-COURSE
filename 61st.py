while True:
    try:
        age = int(input("What is your age: "))
        10/age
        raise ValueError("he cut it out")
        print(age)
    except ValueError:
        print("Enter a number")
        continue
    except ZeroDivisionError:
        print("Enter a number higher than 0")
        break
    else:
        print("Good boy")
    finally:
        print("Ok but im finally done")
    
    print("Can you hear me")
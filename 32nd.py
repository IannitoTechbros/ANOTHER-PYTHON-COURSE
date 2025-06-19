#lets talk about conditional logic

age = int(input("Enter your age : "))
licensed = input("Are you licenced; Y or N: ")


def check_age(age, licensed):
    if age > 18 and licensed == "Y":
        print("You are old enough and licensed to drive")
    elif age < 18 and licensed == "Y":
        print("You are a scam...We are coming for you!!!")
    elif age > 18 and licensed == "N":
        print("You are old enought to drive but you don't have your license. Fuck You!!!!")
    else:
        print("GO HOME BUDDY GO HOME!!!!!!!!!!!!!!!!!!")
    
check_age(age, licensed)




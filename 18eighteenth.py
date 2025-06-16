from datetime import datetime

username = "Ian"

age =  50

relationship_status = "single"


birth_year = input("Enter year of birth: ")

current_year = datetime.now().year


age = int(current_year) - int(birth_year)

print(f"You are {age} years old")
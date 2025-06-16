username = input("Enter username: ")

password = input("Enter password: ")



password_length = len(password)


encrypted_password = "*" * password_length




print(f"Hello, {username}. Your password {encrypted_password} is {password_length} letters long.")
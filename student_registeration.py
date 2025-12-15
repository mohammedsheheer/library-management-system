name = input("Enter your name: ")
pwd = input("Enter your password: ")

#password validation
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

if(validate_password):
    print("Student registeration successful!")
else:
    print("Please enter a strong password!")

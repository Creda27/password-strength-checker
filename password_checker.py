password = input("Enter your password: ")
# print(password) # we dont want to print the password for security reasons
length = len(password)

# print(f"Password length: {length}") 
# protecting password because even metadata can reveal sensitive information

common_passwords = ["password", "password123", "123456", "qwerty", "654321", "111111", "iloveyou", "admin", "guest", "12344321"]

has_upper = has_lower = has_digit = has_symbol = False
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_symbol = True
# print(f"Does password have upper: {has_upper}, lower: {has_lower}, digit: {has_digit}, symbol: {has_symbol}")

score = 0
if password.lower() not in common_passwords:
    if length >= 12:
        score += 1
    else:
        print("password too short, must be atleast 12 characters")
    if has_upper == True:
        score += 1
    else:
        print("add upper case")
    if has_lower == True:
        score+= 1
    else:
        print("add lower case")
    if has_symbol == True:
        score += 1
    else:
        print("add special character")
    if has_digit == True:
        score += 1
    else:
        print("add number")
else:
    print("password too common, please choose something else")

match score:
    case 0 | 1 | 2:
        print("Password Weak")
    case 3 | 4:
        print("Password Okay")
    case 5 :
        print("Password Strong")
    case _:
        print("Password Weak")
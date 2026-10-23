password = input("Enter your password: ")
# print(password) # we dont want to print the password for security reasons
length = len(password)

if length < 12:
    print("Password is too short")
else:
    print("Password meets the length requirements")

# print(f"Password length: {length}") 
# protecting password because even metadata can reveal sensitive information

common_passwords = ["password", "password123", "123456", "qwerty", "654321", "111111", "iloveyou", "admin", "guest", "12344321"]

if password.lower() in common_passwords:
     print("Password is too common, please choose a different password")
else:
    print("password wasn't found in the current blocklist")
           
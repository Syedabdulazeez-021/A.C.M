def special(password):
    # This function checks if the password contains at least one special character
    spe = ["$", "@", "#", "%", "!", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "~", "`"]
    return any(char in spe for char in password)

def num_char(password):
    # This function checks if the password does not start with a digit or special character
    if password[0].isdigit() or password[0] in ["$", "@", "#", "%", "!", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "~", "`"]:
        return False
    return True

def length(password):
    # This function checks the length of the password
    return len(password) == 8

def capital_small(password):
    # This function checks if the password contains both uppercase and lowercase characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_upper and has_lower

def not_allowed(password):
    # This function checks if the password is in the list of not allowed passwords
    notallowed = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]
    return password not in notallowed

def validity(password):
    # This function checks the validity of the password based on multiple criteria
    a = length(password)
    b = not_allowed(password)
    c = special(password)
    d = num_char(password)
    e = capital_small(password) 

    if a and b and c and d and e:
        print("Password is accepted")           
    else:
        print("Sorry, your password is not accepted")

# MAIN PROGRAM
while True:
    password = input("Enter your password: ")
    validity(password)
    x = input("Do you want to retry (yes/no): ")
    if x.lower() == "no":
        break

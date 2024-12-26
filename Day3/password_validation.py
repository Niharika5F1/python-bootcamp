'''def validate_password(password):
    # Check length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Initialize flags for checks
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"

    # Iterate through each character in the password
    for char in password:
        if 'a' <= char <= 'z':  # Check for lowercase letters
            has_lowercase = True
        elif 'A' <= char <= 'Z':  # Check for uppercase letters
            has_uppercase = True
        elif '0' <= char <= '9':  # Check for digits
            has_digit = True
        elif char in special_characters:  # Check for special characters
            has_special = True

    # Validate all conditions
    if not has_lowercase:
        return "Password must contain at least one lowercase letter."
    if not has_uppercase:
        return "Password must contain at least one uppercase letter."
    if not has_digit:
        return "Password must contain at least one digit."
    if not has_special:
        return "Password must contain at least one special character."

    return "Password is valid!"

# Example usage
password_input = input("Enter your password: ")
result = validate_password(password_input)
print(result)'''
s=input()
ucount,lcount,dcount,scount=0,0,0,0

for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1

if len(s)>8 and ucount>0 and lcount>0:
    print("valid")
else:
    print('invalid')

import re

def has_uppercase(password):
    return bool(re.search(r"[A-Z]", password))

def has_lowercase(password):
    return bool(re.search(r"[a-z]",password))

def has_numbers(password):
    return bool(re.search(r"[0-9]", password))

def has_specialChar(password):
    return bool(re.search(r"[\W_]", password))

def check_password_strength(password):
    length = len(password)
    upper = has_uppercase(password)
    lower = has_lowercase(password)
    number = has_numbers(password)
    special_char = has_specialChar(password)

    score = 0
    feedback = []
    
    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be atleast 8 characters long.")
    
    if upper:
        score += 1
    else:
        feedback.append("Password should contain atleast one Upper Case Character.")

    if lower:
        score += 1
    else:
        feedback.append("Password should contain atleast one lower case character.")

    if number:
        score += 1
    else:
        feedback.append("Password should contain atleast one number.")
    
    if special_char:
        score += 1
    else:
        feedback.append("Password should contain atleast one Special character.")

    return score, feedback

def main():
        password = input("Enter the password to be analysed : ")
        pscore, feedback = check_password_strength(password)

        print(f"Password Strength Scored: {pscore}/5")
        if pscore == 5:
            print("The Password is Strong")
        else:
            print("Suggestions to improve The password : ")
            for suggestion in feedback:
                print(f"-> {suggestion}")


if __name__ == "__main__":
    main()
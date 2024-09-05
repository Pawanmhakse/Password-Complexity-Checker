import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Uppercase letter check
    if re.search(r'[A-Z]', password):
        strength += 1

    # Lowercase letter check
    if re.search(r'[a-z]', password):
        strength += 1

    # Number check
    if re.search(r'[0-9]', password):
        strength += 1

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    # Feedback based on strength
    if strength == 5:
        return "Password is very strong."
    elif strength == 4:
        return "Password is strong."
    elif strength == 3:
        return "Password is moderate."
    elif strength == 2:
        return "Password is weak."
    else:
        return "Password is very weak."

def main():
    password = input("Enter your password: ")
    feedback = check_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()

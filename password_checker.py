import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Include at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Include at least one lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Include at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("Include at least one special character (e.g., !, @, #, etc.).")

    # Determine strength level
    if strength == 5:
        status = "Strong"
    elif 3 <= strength < 5:
        status = "Moderate"
    else:
        status = "Weak"

    return status, remarks


def main():
    print("🔐 Password Complexity Checker")
    password = input("Enter your password: ")
    
    status, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {status}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f"- {s}")


if __name__ == "__main__":
    main()

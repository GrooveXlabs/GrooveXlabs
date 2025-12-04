import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short. Use at least 12 characters.")

    # Uppercase, lowercase, digits, symbols
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!, @, #, etc.)")

    # Common password patterns
    weak_patterns = ["123", "password", "qwerty", "abc", "111"]
    if any(pattern in password.lower() for pattern in weak_patterns):
        feedback.append("Avoid common patterns like '123' or 'password'.")
    else:
        score += 1

    # Final result
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Good",
        4: "Strong",
        5: "Very Strong",
        6: "Excellent"
    }

    return strength_levels.get(score, "Unknown"), feedback


if __name__ == "__main__":
    pwd = input("Enter a password to test: ")
    strength, feedback = check_password_strength(pwd)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("\nSuggestions to improve:")
        for f in feedback:
            print(f" - {f}")
    else:
        print("Your password looks strong!")

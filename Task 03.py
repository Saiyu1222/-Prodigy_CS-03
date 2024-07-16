def password_strength(password):
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_+=<>?/|\\{}[]:;" for char in password)
    
    strength_score = sum([length, has_upper, has_lower, has_digit, has_special])
    
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = []
    if not length:
        feedback.append("Password should be at least 8 characters long.")
    if not has_upper:
        feedback.append("Password should include uppercase letters.")
    if not has_lower:
        feedback.append("Password should include lowercase letters.")
    if not has_digit:
        feedback.append("Password should include digits.")
    if not has_special:
        feedback.append("Password should include special characters.")

    return strength, feedback

def main():
    while True:
        password = input("Enter a password to check its strength: ")
        strength, feedback = password_strength(password)
        
        print(f"Password strength: {strength}")
        for tip in feedback:
            print(f"- {tip}")

        repeat = input("Do you want to check another password? (if yes press 'y' / if no press 'n'): ")
        if repeat.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

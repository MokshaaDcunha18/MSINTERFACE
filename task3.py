import re

def password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password)
    lowercase_criteria = re.search(r"[a-z]", password)
    digit_criteria = re.search(r"\d", password)
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    
    # Initialize strength score
    strength_score = 0
    
    # Check each criterion and increment the score
    if length_criteria:
        strength_score += 1
    if uppercase_criteria:
        strength_score += 1
    if lowercase_criteria:
        strength_score += 1
    if digit_criteria:
        strength_score += 1
    if special_char_criteria:
        strength_score += 1
    
    # Provide feedback based on the score
    if strength_score == 5:
        feedback = "Very Strong"
    elif strength_score == 4:
        feedback = "Strong"
    elif strength_score == 3:
        feedback = "Medium"
    elif strength_score == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"
    
    # Detailed feedback
    details = []
    if not length_criteria:
        details.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        details.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        details.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        details.append("Password should contain at least one digit.")
    if not special_char_criteria:
        details.append("Password should contain at least one special character.")
    
    return {
        "strength_score": strength_score,
        "feedback": feedback,
        "details": details
    }

# Example usage
password = input("Enter a password to test its strength: ")
result = password_strength(password)
print(f"Password Strength: {result['feedback']}")
if result['details']:
    print("Feedback:")
    for detail in result['details']:
        print(f"- {detail}")

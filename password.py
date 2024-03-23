import random
import string

def generate_password(length, allow_digits=True, allow_special_chars=False, exclude_ambiguous=False, custom_digits=None, custom_alphabets=None):
    length = int(length)
    chars = []

    if allow_digits:
        if custom_digits:
            chars += custom_digits
        else:
            chars += string.digits

    if allow_special_chars:
        chars += string.punctuation
    else:
        chars = [c for c in chars if c not in string.punctuation]

    if not chars:
        raise ValueError("At least one of digits, alphabets, or special_chars must be True")

    if exclude_ambiguous:
        ambiguous_chars = "lI1O0"
        chars = [c for c in chars if c not in ambiguous_chars]

    alphabets = string.ascii_letters if not custom_alphabets else custom_alphabets
    uppercase_letters = [c for c in alphabets if c.isupper()]
    lowercase_letters = [c for c in alphabets if c.islower()]
    chars += uppercase_letters + lowercase_letters

    password = ''.join(random.choice(chars) for _ in range(length))
    while len(password) < 5 or not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        password = ''.join(random.choice(chars) for _ in range(length))
        
    return password

# Prompt the user for the password length
password_length = int(input("Enter the desired password length: "))

# Generate the password
password = generate_password(password_length, allow_digits=True, allow_special_chars=False, exclude_ambiguous=True)

# Print the generated password
print("Generated password: ", password)
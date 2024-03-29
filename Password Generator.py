import random
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    length = max(length, 8)

    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)

print("Generated Password:", generated_password)

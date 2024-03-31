#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import secrets
import string

def generate_password(length=14, include_symbols=True):

    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter desired password length (minimum 8): "))
        if length >= 8:
            break
        else:
            print("Password length must be at least 8.")
    except ValueError:
        print("Invalid input. Please enter a number.")

include_symbols = input("Include symbols (y/n)? ").lower() == "y"

# Generate and print the password
password = generate_password(length, include_symbols)
print("Generated password:", password)


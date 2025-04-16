import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("La longueur minimale est de 4.")

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Aucun type de caractère sélectionné.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

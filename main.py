import json
import secrets
import string

def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))


import json
import secrets
import string

def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))

def save_password(service, username, password):
    data = {}
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        pass

    data[service] = {"username" : username, "password" : password}
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

    
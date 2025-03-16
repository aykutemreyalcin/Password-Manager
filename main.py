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

def retrieve_password(service):
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if service in data:
                return data[service]
            else:
                return "no password stored for this device"
    except(FileNotFoundError, json.JSONDecodeError):
        return "no saved passwords found"
    
def main():
    while True:
        print("\nPassword Manager")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Retrieve Password")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            length = int(input("Enter password length: "))
            print("Generated Password:", generate_password(length))
        elif choice == "2":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password (or press enter to generate one): ")
            if not password:
                password = generate_password()
            save_password(service, username, password)
            print("Password saved successfully.")
        elif choice == "3":
            service = input("Enter service name to retrieve password: ")
            print(retrieve_password(service))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

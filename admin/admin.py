import os
import json

DATA_FOLDER = r"C:\Users\user-six\Desktop\training\mini project\user\data"

ADMIN_DETAILS = {
    "101": {"username": "Akshata", "password": "abc", "secretCode": "123"},
    "102": {"username": "Bhavya", "password": "abc", "secretCode": "123"}
}

def get_user_file_path(acc_no):
    return os.path.join(DATA_FOLDER, f"{acc_no}.json")

def load_user(acc_no):
    user_file = get_user_file_path(acc_no)
    if os.path.exists(user_file):
        with open(user_file, 'r') as f:
            return json.load(f)
    return None

def save_user(data, acc_no):
    user_file = get_user_file_path(acc_no)
    with open(user_file, 'w') as f:
        json.dump(data, f, indent=2)

def get_admin_details(username):
    for details in ADMIN_DETAILS.values():
        if details['username'] == username:
            return details
    return None

def generate_account_number():
    user_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.json')]
    acc_numbers = [int(os.path.splitext(f)[0]) for f in user_files if os.path.splitext(f)[0].isdigit()]
    next_acc = max(acc_numbers, default=1000) + 1
    return str(next_acc)

def admin_login():
    print(" ----------------WELCOME TO CITY BANK--------------------- ")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    secret_code = input("Enter secret code: ").strip()

    admin = get_admin_details(username)
    if admin and admin["password"] == password and admin["secretCode"] == secret_code:
        print(" Login successful!")
        manage_users()
    else:
        print(" Login failed! Incorrect credentials or secret code.")

def is_valid_name(name):
    return name.isalpha()

def is_valid_pin(pin):
    return pin.isdigit() and len(pin) == 4

def is_valid_balance(value):
    try:
        return float(value) >= 0
    except ValueError:
        return False

def manage_users():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add New User")
        print("2. Delete User")
        print("3. View User")
        print("4. Update User")
        print("5. View list of users")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ").strip()

        if choice == '1':
            account_no = generate_account_number()

            first_name = input("Enter first name: ").strip()
            if not is_valid_name(first_name):
                print(" Invalid first name. Please use alphabetic characters only.")
                continue

            last_name = input("Enter last name: ").strip()
            if not is_valid_name(last_name):
                print(" Invalid last name. Please use alphabetic characters only.")
                continue

            pin = input("Set PIN (4 digits): ").strip()
            if not is_valid_pin(pin):
                print(" Invalid PIN. Must be exactly 4 digits.")
                continue

            username = f"{first_name}_{account_no}"
            password = f"{username}@{account_no}**"

            user_data = {
                "accountNumber": account_no,
                "firstName": first_name,
                "lastName": last_name,
                "username": username,
                "password": password,
                "pin": pin,
                "availableBalance": 0.0
            }

            save_user(user_data, account_no)

            print(f"\n User created successfully!")
            print(f" Account No: {account_no}")
            print(f" Username: {username}")
            print(f" Password: {password}")

        elif choice == '2':
            account_no = input("Enter account number to delete: ").strip()
            user_file = get_user_file_path(account_no)
            if os.path.exists(user_file):
                os.remove(user_file)
                print(f" User {account_no} deleted successfully!")
            else:
                print(" User not found.")

        elif choice == '3':
            account_no = input("Enter account number to view: ").strip()
            user_data = load_user(account_no)
            if user_data:
                print(json.dumps(user_data, indent=2))
            else:
                print(" User not found.")

        elif choice == '4':
            account_no = input("Enter account number to update: ").strip()
            user_data = load_user(account_no)
            if user_data:
                first_name = input("Enter new first name: ").strip()
                if not is_valid_name(first_name):
                    print(" Invalid first name.")
                    continue

                last_name = input("Enter new last name: ").strip()
                if not is_valid_name(last_name):
                    print(" Invalid last name.")
                    continue

                pin = input("Enter new PIN (4 digits): ").strip()
                if not is_valid_pin(pin):
                    print(" Invalid PIN.")
                    continue

                balance_input = input("Enter updated balance: ").strip()
                if not is_valid_balance(balance_input):
                    print(" Invalid balance. Must be a non-negative number.")
                    continue

                balance = float(balance_input)
                username = f"{first_name}_{account_no}"
                password = f"{username}@{account_no}**"

                user_data.update({
                    "firstName": first_name,
                    "lastName": last_name,
                    "username": username,
                    "password": password,
                    "pin": pin,
                    "availableBalance": balance
                })

                save_user(user_data, account_no)
                print(" User updated successfully!")
            else:
                print(" User not found.")

        elif choice == '5':
            print("\n--- List of All Users ---")
            user_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.json')]

            if not user_files:
                print(" No users found in the data folder.")
            else:
                for file in user_files:
                    acc_no = os.path.splitext(file)[0]
                    user_data = load_user(acc_no)
                    if user_data:
                        print(f"Account No: {user_data['accountNumber']}")
                        print(f"Name: {user_data['firstName']} {user_data['lastName']}")
                        print(f"Balance: ₹{user_data['availableBalance']}")
                        print("-------------------------------------------------------")

        elif choice == '6':
            print("Exiting admin menu...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__": admin_login()
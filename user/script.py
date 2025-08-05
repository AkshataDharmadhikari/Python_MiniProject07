import os
import json
import subprocess

DATA_FOLDER = os.path.join(os.path.dirname(__file__), "data")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    print("~~~~~~~~~ Welcome to Citibank ~~~~~~~~~")
    print("a. Admin")
    print("b. User")
    role = input("Select your role: ").strip().lower()
    return role

def load_user(acc_no):
    file_path = os.path.join(DATA_FOLDER, f"{acc_no}.json")
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        return json.load(f)

def save_user(acc_no, data):
    file_path = os.path.join(DATA_FOLDER, f"{acc_no}.json")
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def authenticate_user():
    acc_no = input("Enter Account Number: ").strip()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    user_data = load_user(acc_no)
    if user_data and user_data["username"] == username and user_data["password"] == password:
        print("Login successful!")
        return user_data
    else:
        print("Invalid credentials.")
        return None

def show_menu():
    print("\nChoose an operation:")
    print("1. View Account Details")
    print("2. Check Balance")
    print("3. Withdraw")
    print("4. Deposit")
    print("5. Transfer")
    print("6. Change Pin")
    print("7. Exit")

def view_account(user):
    print(json.dumps(user, indent=2))

def check_balance(user):
    print(f"Available Balance: ₹{user['availableBalance']}")

def withdraw(user):
    amount_input = input("Enter amount to withdraw: ").strip()
    try:
        amount = float(amount_input)
        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid amount entered. Please enter a numeric value.")
        return

    if amount <= user["availableBalance"]:
        user["availableBalance"] -= amount
        save_user(user["accountNumber"], user)
        print("Withdrawal successful!")
    else:
        print("Insufficient balance.")

def deposit(user):
    amount_input = input("Enter amount to deposit: ").strip()
    try:
        amount = float(amount_input)
        if amount < 0:
            print("Amount cannot be negative.")
            return
    except ValueError:
        print("Invalid amount entered. Please enter a numeric value.")
        return

    user["availableBalance"] += amount
    save_user(user["accountNumber"], user)
    print("Deposit successful.")

def transfer(user):
    acc_no = input("Enter receiver's account number: ").strip()
    if not acc_no.isdigit():
        print("Invalid account number format.")
        return

    if user["availableBalance"] <= 0:
        print("Your account has insufficient balance to initiate a transfer.")
        return

    amount_input = input("Enter amount to transfer: ").strip()
    try:
        amount = float(amount_input)
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
            return
    except ValueError:
        print("Invalid amount entered. Please enter a numeric value.")
        return

    if amount > user["availableBalance"]:
        print("Insufficient balance to complete the transfer.")
        return

    receiver = load_user(acc_no)
    if receiver:
        user["availableBalance"] -= amount
        receiver["availableBalance"] += amount
        save_user(user["accountNumber"], user)
        save_user(acc_no, receiver)
        print("Transfer successful.")
    else:
        print("Receiver account not found.")

def change_pin(user):
    current = input("Enter current PIN: ").strip()
    if current == user["pin"]:
        while True:
            new = input("Enter new 4-digit PIN: ").strip()
            if new.isdigit() and len(new) == 4:
                user["pin"] = new
                save_user(user["accountNumber"], user)
                print("PIN updated successfully!")
                break
            else:
                print("Invalid PIN. Please enter exactly 4 digits.")
    else:
        print("Incorrect current PIN.")

def main():
    while True:
        role = welcome()
        clear_screen()
        if role == 'b':
            user_data = authenticate_user()
            if user_data:
                while True:
                    clear_screen()
                    show_menu()
                    choice = input("Enter your choice (1–7): ")
                    if choice == "1":
                        view_account(user_data)
                    elif choice == "2":
                        check_balance(user_data)
                    elif choice == "3":
                        withdraw(user_data)
                    elif choice == "4":
                        deposit(user_data)
                    elif choice == "5":
                        transfer(user_data)
                    elif choice == "6":
                        change_pin(user_data)
                    elif choice == "7":
                        print("Thank you for banking with us!")
                        break
                    input("\nPress Enter to continue...")
            else:
                input("Login failed. Press Enter to exit.")
        elif role == 'a':
            admin_path = r"C:\Users\user-six\Desktop\training\mini project\admin\admin.py"
            subprocess.run(["python", admin_path])
        else:
            print("Invalid selection.")
            break

if __name__ == "__main__":
    main()

# Banking ATM Application Mini Project

## Project Overview

This project simulates a basic ATM banking system with functionalities for both users and administrators. The system allows users to log in, view account details, check balances, perform transactions such as withdrawal, deposit, and transfer, and change their PIN. Administrators can create new user accounts with auto-generated account numbers and secure credentials.

## Features

- User Authentication: Users can log in using their account number, username, and password stored in individual files.
- Account Management: View account details, check balance, withdraw, deposit, transfer funds, and change PIN.
- Admin Operations: Create new user accounts with auto-generated account numbers and secure credentials.
- Data Storage: User details are stored in individual text files within a designated folder.
- Auto-Increment Account Numbers:** The system maintains a counter in a file (`autonumber.txt`) to generate unique account numbers for new users.

## Workflow

### Application Startup
- Displays a welcome message:  
  `Welcome to ~~~~~~~~~Citibank~~~~~~~~~`
- Presents a menu to select user type:
  - Admin
  - User

### User Login
- Prompts for account number, username, and password.
- Validates credentials against stored user files.
- On successful login, displays a menu with options:
  1. View Account Details
  2. Check Balance
  3. Withdraw
  4. Deposit
  5. Transfer
  6. Change PIN
  7. Exit

### User Operations
- Based on user selection, performs the corresponding transaction.
- Updates user files accordingly to reflect changes.

### Admin Operations
- Allows creation of new user accounts:
  - Automatically generates a new account number.
  - Creates a username in the format: `firstname_newAccountNo`.
  - Generates a secure password using a predefined algorithm: `username@accNo**`.
  - Stores user details in a new file named with the account number (e.g., `101.txt`).
  - Updates the `autonumber.txt` file with the new account number for future use.

## Data Storage Structure

- User Files: Stored in a dedicated folder, each named after the account number (e.g., `101.txt`).
- File Content Format:

  ```
  accNo, firstName, lastName, availableBalance, userName, Password, Pin
  ```

- Auto Number File: `autonumber.txt` contains the last assigned account number (e.g., `100`).

## Implementation Notes

- The system ensures data integrity by reading and writing to files securely.
- Validation checks are performed to prevent errors during transactions.
- The system is designed to be extendable for additional features.

---

This project provides a foundational simulation of banking operations, emphasizing file handling, user authentication, and basic transaction management in Python.

# Password-Based Door Lock using Python

## Description

The Password-Based Door Lock is a simple Python project that simulates a digital door security system. The user must enter the correct password to unlock the door.

If the correct password is entered, access is granted. If an incorrect password is entered, the system allows another attempt. After three incorrect attempts, the door is locked and the system displays a security message.

## Technologies Used

* Python
* Variables
* `while` loop
* `if-else` statements
* `input()`
* `print()`
* Basic comparison operators

No database, external library, or advanced programming concepts are used.

## Features

* Password verification
* Access granted for the correct password
* Access denied for an incorrect password
* Three password attempts
* Automatic system lock after three wrong attempts
* Simple terminal-based interface

## Default Password

```text
1234
```

The password is stored in the program as:

```python
correct_password = "1234"
```

For a project demonstration, the password can be changed directly in the code.

## Working

1. The program starts the door-lock system.
2. The user is asked to enter a password.
3. The entered password is compared with the stored password.
4. If the password is correct, access is granted and the door is unlocked.
5. If the password is incorrect, the number of remaining attempts is displayed.
6. The user gets a maximum of three attempts.
7. After three incorrect attempts, the system displays "Door Locked".
8. The program then ends.

## Example

### Correct Password

```text
Enter password: 1234

Access Granted
Door Unlocked
```

### Incorrect Password

```text
Enter password: 1111

Incorrect Password
Attempts remaining: 2
```

### Three Wrong Attempts

```text
Too many incorrect attempts.
Door Locked
System Security Activated.
```

## Project Structure

```text
Password-Based-Door-Lock/
│
├── door_lock.py
├── testbench.py
├── output.txt
└── README.md
```

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Run the Door Lock

Open the project folder in Command Prompt or Terminal and run:

```text
python door_lock.py
```

### Step 3: Run the Testbench

Run:

```text
python testbench.py
```

## Testbench

The testbench checks:

1. Correct password
2. Incorrect password
3. Wrong password detection
4. Access after entering the correct password
5. Three incorrect attempts

Expected output:

```text
Test 1: Correct Password - PASS
Test 2: Incorrect Password - PASS
Test 3: Wrong Password Detection - PASS
Test 4: Access After Correct Password - PASS
Test 5: Three Wrong Attempts - PASS
```

## Advantages

* Simple and beginner-friendly
* Easy to understand
* Uses basic Python concepts
* No external libraries
* No database required
* Easy to modify
* Suitable for a BTech mini project

## Future Scope

The project can be extended by adding a keypad, LCD display, buzzer, RFID authentication, fingerprint authentication, password-changing functionality, and a physical electronic door-lock mechanism using a microcontroller.

## Conclusion

The Password-Based Door Lock project demonstrates the basic concept of digital access control using Python. It verifies a user's password and provides access only when the correct password is entered. The three-attempt security feature provides a simple additional layer of protection.

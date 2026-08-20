# Password-Based Door Lock
# Basic Python Project

correct_password = "1234"
attempts = 0
max_attempts = 3

print("================================")
print("     PASSWORD-BASED DOOR LOCK")
print("================================")

while attempts < max_attempts:

    password = input("Enter password: ")

    if password == correct_password:
        print("\nAccess Granted")
        print("Door Unlocked")
        break

    else:
        attempts = attempts + 1
        remaining = max_attempts - attempts

        print("Incorrect Password")

        if remaining > 0:
            print("Attempts remaining:", remaining)

        else:
            print("\nToo many incorrect attempts.")
            print("Door Locked")
            print("System Security Activated.")

if attempts == max_attempts:
    print("\n================================")
    print("         SYSTEM LOCKED")
    print("================================")

print("\nThank you.")
# Password-Based Door Lock Testbench

correct_password = "1234"

print("================================")
print("   DOOR LOCK TESTBENCH")
print("================================")

# Test 1: Correct password

password = "1234"

if password == correct_password:
    print("Test 1: Correct Password - PASS")
else:
    print("Test 1: Correct Password - FAIL")


# Test 2: Incorrect password

password = "5678"

if password != correct_password:
    print("Test 2: Incorrect Password - PASS")
else:
    print("Test 2: Incorrect Password - FAIL")


# Test 3: Another incorrect password

password = "0000"

if password != correct_password:
    print("Test 3: Wrong Password Detection - PASS")
else:
    print("Test 3: Wrong Password Detection - FAIL")


# Test 4: Correct password after wrong password

password = "1234"

if password == correct_password:
    print("Test 4: Access After Correct Password - PASS")
else:
    print("Test 4: Access After Correct Password - FAIL")


# Test 5: Three wrong attempts

attempts = 0

password = "1111"

if password != correct_password:
    attempts = attempts + 1

password = "2222"

if password != correct_password:
    attempts = attempts + 1

password = "3333"

if password != correct_password:
    attempts = attempts + 1

if attempts == 3:
    print("Test 5: Three Wrong Attempts - PASS")
else:
    print("Test 5: Three Wrong Attempts - FAIL")


print("================================")
print("All tests completed.")
print("================================")
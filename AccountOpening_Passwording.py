account={}

print("\n==== SECURE EMPLOYEE ACCOUNT SYSTEM ====")

# Stage 1: Account Setup
total_account=int(input("\nEnter Number of Account to Create:"))

for i in range(1,total_account+1):
    print(f"\n----- Account{i} -----")

    # Username
    while True:
        username=input("Enter Username:")
        
        if username =="":
            print("Username connot be empty.")

        elif username in account:
            print("Username already taken. Try Again.")

        else:
            break

    # Stage 2: Password Creation
    while True:

        password=input("Enter Password:")
        errors=[]

        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")
        elif password in account:
            print("Password Already taken, Try Again.")
            continue
       

        # Check Uppercase
        has_upper=False

        for ch in password:
            if ch.isupper():
                has_upper=True
                break

        if not has_upper:
            errors.append("Password must contain at least one uppercase letter")

        # Check LowerCase
        has_lower=False

        for ch in password:
            if ch.islower():
                has_lower=True
                break

        if not has_lower:
            errors.append("Password must contain at least one lowercase letter")

        # Check Digit
        has_digits=False

        for ch in password:
            if ch.isdigit():
                has_digits=True
                break

        if not has_digits:
            errors.append("Password must contain at least (0 to 9) number")

        # Check Special Character
        has_special=False

        for ch in password:
            if ch.isalnum():
                has_special=True
                break
        if not has_special:
            errors.append("Password must contain at least one special character")

        # Check Space
        has_spaces=False
        for ch in password:
            if ch.isspace():
                has_spaces=True
                break

        if has_spaces:
            errors.append("Password must contain at least one whitespace character")

        elif password in account:
           print("Password already taken. Try Again.")
           print("Enter The Password:")

        # Check Display Error
        if len(errors) > 0:
            print("\nPassword Rejected!")

            for error in errors:
                print(error)

            print("\n Please Enter the Password Again")
            continue

        # Confirm Password
        confirm_password=input("Confirm Enter Password:")
        while confirm_password != password:
            print("Password Do not match!."
                  "Plaese Enter the Password Again.")
            confirm_password=input("Confirm Enter Password:")

        #Store Account
        account[username]=password
        print("\nAccount Created Successfully!")
        break

# Stage3: Employee Login

if len(account) > 0:
    print("\n====== EMPLPYEE LOGIN=====")
    attempts=0
    max_attempts=5
    while attempts < max_attempts:
        username=input("\nEnter Username:")
        password=input("Enter Password:")

        #Check Username and Password
        if username in account and account[username]==password:
            print("\nLogin Successfully!")
            print("Welcome To My Account",username)
            break
        else:
            attempts+=1
            print("\nInvaild username or password")
            remaining=max_attempts-attempts
            if remaining > 0:
                print("Attempts Remaining:",remaining)

        # Maximum Attempts Exceeded.
        if attempts == max_attempts:
            print("\nAccess Denied!")
            print("Maximum Login Attempts Exceeded.")
else:
    print("No Employee Accounts were created")

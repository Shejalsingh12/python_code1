def password_checker():
    password = input("Enter a password: ")

    if len(password) < 6:
        print("Weak: Too short ❌")
    elif password.isdigit() or password.isalpha():
        print("Medium: Use letters + numbers ✅")
    else:
        print("Strong Password 💪")

password_checker()

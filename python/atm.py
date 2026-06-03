def atm():
    balance = 1000  # starting balance

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your Balance = ₹", balance)

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Deposited ₹", amount)

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawn ₹", amount)
            else:
                print("❌ Insufficient balance")

        elif choice == 4:
            print("Thank you for using ATM 💳")
            break
        else:
            print("Invalid option!")

atm()

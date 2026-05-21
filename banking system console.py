from datetime import datetime

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
        self.last_deposit_time = None
        self.last_withdraw_time = None
        self.last_transaction_time = None

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            self.last_deposit_time = time
            self.last_transaction_time = time

            print("\n----- DEPOSIT DETAILS -----")
            print(f"Deposited Amount : ₹{amount}")
            print(f"Total Balance    : ₹{self.__balance}")
            print(f"Last Deposit Time: {self.last_deposit_time}")
            print("---------------------------")
        else:
            print("❌ Amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Amount must be positive")
        elif amount > self.__balance:
            print("❌ Insufficient balance")
        else:
            self.__balance -= amount
            time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            self.last_withdraw_time = time
            self.last_transaction_time = time

            print("\n----- WITHDRAW DETAILS -----")
            print(f"Withdrawal Amount : ₹{amount}")
            print(f"Total Balance     : ₹{self.__balance}")
            print(f"Last Withdraw Time: {self.last_withdraw_time}")
            print("----------------------------")

    def check_balance(self):
        print("\n----- ACCOUNT DETAILS -----")
        print(f"Name              : {self.name}")
        print(f"Total Balance     : ₹{self.__balance}")

        if self.last_transaction_time:
            print(f"Last Transaction  : {self.last_transaction_time}")
        else:
            print("Last Transaction  : No transactions yet")

        print("---------------------------")


# ---------- SAFE INPUT ----------
def get_float_input(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("❌ Invalid input! Enter numbers only.")


# ---------- MAIN ----------
name = input("Enter account holder name: ")
initial_balance = get_float_input("Enter initial balance: ")

account = BankAccount(name, initial_balance)

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = get_float_input("Enter deposit amount: ")
        account.deposit(amount)

    elif choice == '2':
        amount = get_float_input("Enter withdrawal amount: ")
        account.withdraw(amount)

    elif choice == '3':
        account.check_balance()

    elif choice == '4':
        print("\n🙏 Thanks for using the banking system!")
        break

    else:
        print("❌ Invalid choice")
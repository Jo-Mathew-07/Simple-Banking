import string as s
def star():
    print(f"***************************************")

def show():
    star()
    print("""  WELCOME TO ONLINE BANKING\n     
    1. Show Balance.
    2. Deposit Amount.
    3. Withdraw Amount.
    4. Change Password.
    5. Exit.\n""")
    star()
    return input("Select your desired option (1 - 5): ")
class Bank:
    def __init__(self):
        try:
            with open("pwd.txt", "r") as f:
                self._pwd = f.read()
            with open("bal.txt", "r") as f:
                self._bal = float(f.read())
        except FileNotFoundError:
            print("That file was not found")
        except PermissionError:
            print("You do not have permission to read that file")

    def show(self):
        try:
            with open("bal.txt", "r") as b:
                print(f"\nYour Bank Balance: ${float(b.read()):.2f}")
        except FileNotFoundError:
            print("That file was not found")
        except PermissionError:
            print("You do not have permission to read that file")


    def chk(self):
        pwd = input("Enter your Bank Password: ")
        if pwd == self._pwd:
            return True
        else:
            return False

    def deposit(self, amount):
        if not amount.isalpha():
            if amount == 0:
                print("\nNo changes done!")
                Bank().show()
            else:
                cont = float(self._bal) + float(amount)
                try:
                    with open("bal.txt", "w") as b:
                        b.write(str(cont))
                        print(f"\n${amount} has been deposited to your account!")
                except FileExistsError:
                    print("That file already exists")
                except PermissionError:
                    print("You do not have permission to read that file")

                Bank().show()
        else:
            print(f"\nInvalid Input. Please try again.")

    def withdraw(self, amount):
        if not amount.isalpha():
            amount = float(amount)
            if amount > self._bal:
                print(f"\nInsufficient funds!")
            elif amount == 0:
                print("\nNo changes done!")
                Bank().show()
            else:
                cont = float(self._bal) - float(amount)
                try:
                    with open("bal.txt", "w") as b:
                        b.write(str(cont))
                        print(f"\n${amount} has been withdrawn from your account!")
                except FileExistsError:
                    print("That file already exists")
                except PermissionError:
                    print("You do not have permission to read that file")
                Bank().show()
        else:
            print(f"\nInvalid Input. Please try again.")

    def passwd(self):
        pwd = input("Enter your current password: ")
        if pwd == self._pwd:
            pwde = input("\nEnter your new password: ")
            pwdc = input("Confirm your new password: ")
            if pwde not in (s.digits + s.punctuation + s.ascii_letters) and len(pwde) > 12:
                if pwde == pwdc:
                    try:
                        with open('pwd.txt', 'w') as f:
                            f.write(pwde)
                        print("\nPassword changed successfully!")
                    except FileExistsError:
                        print("That file already exists")
                else:
                    print("\nPasswords do not match!")
            else:
                print("\nPassword must contain at least 12 characters and at least one special characters, alphabets in lower and upper case and digits!")

        else:
            print("\nIncorrect Password")


if __name__ == "__main__":
    b = Bank()
    while True:
        choice = show()
        match choice:
            case '1':
                b.show()
            case '2':
                b.deposit(input("Enter amount to deposit: $"))
            case '3':
                b.withdraw(input("Enter amount to withdraw: $"))
            case '4':
                b.passwd()
            case '5':
                break
            case _:
                print("Invalid choice!")
    star()
    print("  ***   HAVE A GOOD DAY!   ***  ")
    star()

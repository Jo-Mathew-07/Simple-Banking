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
        pwd = input("Enter your Login Password: ")
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

def wr():
    print("Wrong password!")
if __name__ == "__main__":
    b = Bank()
    with open("limit.txt", "r") as file:
        val = int(file.read())
    if  val <= 3 and val > -1:
        if b.chk():
            while True:
                choice = show()
                match choice:
                    case '1':
                        if b.chk():
                            b.show()
                        else:
                            wr()
                            quit()
                    case '2':
                        if b.chk():
                            b.deposit(input("Enter the amount to deposit: $"))
                        else:
                            wr()
                            quit()
                    case '3':
                        if b.chk():
                            b.withdraw(input("Enter the amount to withdraw: $"))
                        else:
                            wr()
                            quit()
                    case '4':
                        b.passwd()
                    case '5':
                        break
                    case _:
                        print("Invalid choice!")
            star()
            print("  ***   HAVE A GOOD DAY!   ***  ")
            star()
        else:
            wr()
            with open("limit.txt", "r+") as t:
                cont = int(t.read())
                cont += 1
                print(f"{4 - cont} attempts left.")
                t.seek(0)
                t.write(str(cont))
            quit()

    else:
        print("Limit reached! Please try again after 48 hours.")
        quit()



















#     def show(balance):
#         print(f"Balance: ${balance:.2f}")

# def dep():
#     try:
#         amount = float(input("Enter the amount you want to deposit: $"))
#         if amount < 0:
#             print("Amount can't be negative!")
#             return 0
#         else:
#             star()
#             print(f"${amount} has been debited to your account.")
#             star()
#             return amount
#     except:
#         print("Texts not allowed! Please try again!")
#         return 0

# def wdraw(balance):
#     try:
#         amount = float(input("Enter the amount you want to withdraw: $"))
#         if amount < 0:
#             print("Amount can't be negative!")
#             return 0
#         elif amount > balance:
#             print("Insufficient funds!")
#             return 0
#         else:
#             star()
#             print(f"${amount} has been withdrawn from your account.")
#             star()
#             return amount
#     except:
#         print("Text not allowed! Please try again!")
#         return 0

# def prog():
#     balance = 0
#     while True:
#         star()
#         print("""      WELCOME TO ONLINE BANKING
#         1. Show Balance.
#         2. Deposit Amount.
#         3. Withdraw Amount.
#         4. Exit.""")
#         star()
#         choice = input("Select your desired option (1 - 4): ")
#         match choice:
#             case '1':
#                 show(balance)
#             case '2':
#                 balance += dep()
#             case '3':
#                 balance -= wdraw(balance)
#             case '4':
#                 break
#             case _ :
#                 print("Invalid choice!")
#     star()
#     print("      THANK YOU USING OUR SERVICE      ")
#     star()



# if __name__ == '__main__':
#     prog()
"""
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance
"""
class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def check(self):
        print("---------------------------------")
        print("Account No: ",self.account_no)
        print("Balance: ",self.balance)
    
    def credit(self, credit_amount):
        print("---------------------------------")
        self.balance = self.balance + credit_amount
        print("Credit Amount: ", credit_amount)
        print("Current Balance: ", self.balance)
    
    def debit(self, debit_amount):
        print("---------------------------------")
        self.balance = self.balance - debit_amount
        print("Debit Amount: ", debit_amount)
        print("Current Balance: ", self.balance)
        

a1 = Account(0, "141168-hira")
# a1.credit(1500)
# a1.debit(500)
# a1.check()

close_program = False

while(close_program == False):
    print("-----------Program is running--------------")
    print("0) Enter 0 to Close the program")
    print("1) Enter 1 to Check Account Details")
    print("2) Enter 2 to Credit Amount")
    print("3) Enter 3 to Debit Amount")
    command = str(input("Enter Your Command: "))
    if(command == "0"):
        close_program = True
        print("Program close successfully...")
    elif(command == "1"):
        a1.check()
    elif(command == "2"):
        credit_amount = int(input("Enter the Credit Amount: "))
        a1.credit(credit_amount)
    elif(command == "3"):
        debit_amount = int(input("Enter the Debit Amount: "))
        a1.debit(debit_amount)
    else:
        print("Please Enter The Correct Command")


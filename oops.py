#atm class:-
class Atm:
    def __init__(self):
        pass # init is constructor
        self.pin =""
        self.balance = 0
            
        self.menu()
    
    def menu(self):
        user_input = input('''
                hello,how would you like to proceed?
                1.enter 1 to create pin.
                2.enter 2 to deposit.
                3.enter 3 to withdraw.
                4.enter 4 to check balance.
                5.enter 5 to exit.
          ''')
        if user_input =="1":
            self.create_pin()
        elif user_input =="2":
           self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input =="4":
            self.check_balance()
        else:
            print("exit")
    def create_pin(self):
        self.pin = input("enter your pin:")
        print("pin set successfully")
    def deposit(self):
        temp = input("enter your pin:")
        if temp == self.pin:
            amount = int(input("enter your amount:"))
            self.balance = self.balance + amount
            print("deposit sucessful")
        else:
            print("invalid pin")
    def withdraw(self):   
        temp = input("enter your pin:")
        if temp == self.pin:
                amount = int(input("enter your amount:"))
                if amount<self.balance: 
                    self.balance = self.balance - amount
                    print("operation successful")  
                else:
                    print("insufficient funds")
        else:
            print("invalid pin")
    def check_balance(self):
        temp =   input("enter your pin:")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")


sbi = Atm()
sbi.create_pin()
sbi.deposit()
sbi.withdraw()







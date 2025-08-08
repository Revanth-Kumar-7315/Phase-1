class Atm:
    
    __counter = 1
    
    # Constructor
    def __init__(self):
        print(id(self))
        self.pin = ''
        self.__balance = 0
        self.cid = Atm.counter
        Atm.__counter = Atm.__counter + 1 
        self.menu()
    
    # utility functions
    @staticmethod
    def get_counter():
        return Atm.counter
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Not possible")
        
    def menu(self):
        user_input =  input("""
        1. Press 1 to Set a Pin.
        2. Press 2 to Change the Pin.
        3. Press 3 to Check Balance.
        4. Press 4 to withdraw money.
        5. Press Anything else to exit.
        """)
        
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
    
    def create_pin(self):
        user_pin = input("Enter the Pin :- ")
        self.pin = user_pin
        
        user_balance = int(input("Enter the balance :- "))
        self.__balance = user_balance
        
        self.menu()
        
    def change_pin(self):
        old_pin = input("Enter your present pin :- ")
        
        if old_pin == self.pin:
            new_pin = input("Change the Pin :- ")
            self.pin = new_pin
        else:
            print("Incorrect Pin")
        self.menu()
            
    def check_balance(self):
        user_pin =  input('Enter the pin :- ')
        if user_pin == self.pin :
            print(f"Balance :- {self.__balance}")
        else:
            print("Pin is Incorrect")
        self.menu()
    
    def withdraw(self):
        user_pin =  input('Enter the pin :- ')
        if user_pin == self.pin :
            amount = int(input('Enter amount you want to withdraw :- '))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print(f"Transaction is successful, Balance :- {self.__balance}")
            else:
                print(f'You have only {self.__balance} in your account')
        else:
            print("Pin is Incorrect")
        self.menu()
        
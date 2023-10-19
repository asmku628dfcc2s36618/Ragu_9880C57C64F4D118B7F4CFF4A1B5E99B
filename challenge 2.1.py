Class BankAccount: 
                    
  Def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    Self.__account_number = account_number
    Self.__account_holder_name = account_holder_name
    Self.__account_balance = initial_balance
 
  Def deposit(self, amount):
    If amount > 0:
      Self.__account_balance += amount
      #self.__account_balance = self.__ account_balance+amount
      Print(“Deposited â‚¹{}. New balance: â‚¹{}”.format(amount,
           Self.__account_balance)) 
    Else:
      Print(“Invalid deposit amount.”)

  Def withdraw(self, amount):
    If amount > 0 and amount <= self.__account_balance:
     Self.__account_balance -= amount
      #self.__account_balance = self.__account_balance – amount
     Print(“Withdrew â‚¹{}. New balance: â‚¹{}”.format(amount,
           Self.__account_balance))
    Else:
       Print(“Invalid withdrawal amount or insufficient balance.”)

  Def display_balance(self):
    Print(“Account balance for {} (Account #{}): â‚¹{}”.format(   
        Self.__account_holder_name, self.__account_number,
        Self.__account_balance))


# Create an instance of the BankAccount class
Account = BankAccount(account_number=”12210100003”,
            Account_holder_name=”st”,
            Initial_balance=5000.0)

# Test deposit and withdrawal functionality
Account.display_balance()
#account.deposit (500.0)
#account.withdraw(200.0)
#account.display_balance()

    
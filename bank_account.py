class BankAccount:
    int_rate = 0.01
    balance = 0
    all_accounts_info = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.all_accounts_info.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance:${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    # @classmethod
    # def all_account_info(cls):
    #     for account in cls.all_accounts_info:
    #         account.all_accounts_info.append(cls)
    #     print 


ian = BankAccount(int_rate = 0.05, balance = 1000) # Does attributes need to be reset when creating an instance?
ryan = BankAccount(int_rate = 0.02, balance = 0) # 

ian.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()

ryan.deposit(1000).deposit(500).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()


#ninja bonus: use a classmethod to print all instances of a bank account's info ????


class BankDeposit: 
    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate
    
    def __calculate_profit(self):
        return self.balance / 100 * self.rate
    
    def get_balance_with_profit(self):
        return self.balance + self.__calculate_profit()


account = BankDeposit("John Connor", 1000, 5)
print(account._BankDeposit__calculate_profit())
print(account.get_balance_with_profit())

print()

account_2 = BankDeposit("Sarah Connor", 200, 27)
print(account_2.name)
print(account_2.balance)
print(account_2.rate)
print(account_2._BankDeposit__calculate_profit())
print(account_2.get_balance_with_profit())
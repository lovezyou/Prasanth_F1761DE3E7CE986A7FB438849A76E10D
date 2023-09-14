'''this program has class BankAccount with private attribute and methods '''

#Creating a class called BankAccount 
class BankAccount:

	def __init__(self, account_number,account_holder_name, initial_balance=0.0):
		self.__account_number = account_number
		self.__account_holder_name = account_holder_name
		self.__account_balance = initial_balance


    #method for deposit function
	def deposit(self, amount):
		if amount > 0:
			self.__account_balance += amount
			print("Deposited \u20b9{}. current balance : \u20b9{}".format(amount, self.__account_balance))
		else:
			print("Invalid deposit amount. Please deposit a correct amount.")

    #method for withdrawal function
	def withdraw(self, amount):
		if amount > 0 and amount <= self.__account_balance:
			self.__account_balance -= amount
			print("Withdraw \u20b9{}. current balance: \u20b9{}".format(amount, self.__account_balance))
		else:
			print("Invalid withdrawal amount or insufficient balance.")

    #method for displaying current a/c balance 
	def display_balance(self):
		print("Account balance for {} (Account #{}): \u20b9{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))


#Creating an object of the BankAccount class
account = BankAccount(account_number = "0987654321",account_holder_name = "Mr.Ramu",initial_balance=90000.0)


#test deposit and withdrawal functionalities 
account.display_balance()
account.deposit(16666.0)
account.withdraw(8765.0)
account.display_balance()

class BankAccount:
   def __init__(self,account_holder_name,account_number,balance=0):
       self.account_holder_name = account_holder_name
       self.account_number = account_number
       self.balance = balance
   def deposit(self, amount):
       if amount > 0:
           self.balance += amount
           print(f"₹{amount} deposited successfully. New balance= {self.balance}")
   def withdraw(self, amount):
       if amount > 0:
          if amount <= self.balance:
             self.balance-= amount
             print(f"₹{amount} withdrawn successfully. Remaining balance= ₹{self.balance}")
   def check_balance(self):   
        print(f"Account Balance: ₹{self.balance}")
account1 = BankAccount("Poongu", "7765476876", 6000)
account1.check_balance()
account1.deposit(3000)
account1.check_balance()
account1.withdraw(2200)
account1.check_balance()

class Cosmetics:
  def __init__(self,name="Sunscreen",brand="BellaVita",price=200,category="Face Protection"):
     self.name=name
     self.brand=brand
     self.price=price
     self.category=category
  def show(self):
      print("Product Name:",self.name,'\n'"Product Brand:",self.brand,'\n'"Product Price:",self.price,'\n'"Product Category:",self.category)
    
style=Cosmetics()
style.show()

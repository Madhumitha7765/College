# class to perform actions wrt each category
class Category:
  def __init__(self, category):
        self.ledger =[]
        self.amount=0
        self.category = category

 # check balances
  def check_funds(self,amount):
    if self.amount< amount:
      return False
    else:
      return True

 # depositing money
  def deposit(self,amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
    self.amount += amount

 # withdrawing
  def withdraw(self,amount,description=""):
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # return balanace of budget
  def get_balance(self):
    return self.amount

  # transferring money
  def transfer(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False


# class to manipulate different budgets
class budgets(Category):

    def __init__(self):
        budget = 1000
        food_expense = 100
        clothing_expense = 100
        entertainment_expense= 100

    def food(self):
        ch = input("\nEnter action you wish to perform : 1.Deposit\n2.Withdraw\n3.Compute balances\n4.transfer")
        if int(ch)==1:
            amount = input("\nEnter amount")
            food.deposit(int(amount), "initial deposit")
            budget = budget + amount
        elif int(ch) == 2:
            amount = int(input("\nEnter amount"))
            rs = input("\nType remarks")
            budget = budget - amount
            food_expense += amount
            food.withdraw(amount,rs)
        elif int(ch) == 3:
            print(food.get_balance())
        elif int(ch) == 4 :
            option = int(input("Which category would you transfer to? \n 1.Clothing \n 2. Entertainment \n"))
            amount = int(input("\nEnter amount"))
            food.transfer(amount, option)
            food_expense += amount


    def clothing(self):
        ch = input("\nEnter action you wish to perform : 1.Deposit\n2.Withdraw\n3.Compute balances\n4.transfer")
        if int(ch)==1:
            amount = input("\nEnter amount")
            clothing.deposit(int(amount), "initial deposit")
            budget = budget + amount
        elif int(ch) == 2:
            amount = int(input("\nEnter amount"))
            rs = input("\nType remarks")
            budget = budget - amount
            clothing_expense += amount
            clothing.withdraw(amount,rs)
        elif int(ch) == 3:
            print(clothing.get_balance())
        elif int(ch) == 4 :
            option = int(input("Which category would you transfer to? \n 1.Food \n 2. Entertainment \n"))
            amount = int(input("\nEnter amount"))
            clothing.transfer(amount, option)
            clothing_expense += amount


    def entertainment(self):
        ch = input("\nEnter action you wish to perform : 1.Deposit\n2.Withdraw\n3.Compute balances\n4.transfer")
        if int(ch)==1:
            amount = input("\nEnter amount")
            entertainment.deposit(int(amount), "initial deposit")
            budget = budget + amount
        elif int(ch) == 2:
            amount = int(input("\nEnter amount"))
            rs = input("\nType remarks")
            budget = budget - amount
            entertainment_expense += amount
            clothing.withdraw(amount,rs)
        elif int(ch) == 3:
            print(entertainment.get_balance())
        elif int(ch) == 4 :
            option = int(input("Which category would you transfer to? \n 1.Food \n 2. Clothing \n"))
            amount = int(input("\nEnter amount"))
            entertainment.transfer(amount, option)
            entertainment_expense += amount


    # calculating statistics
    def check_statistics(self):
        print("********percentage of expenses in each category********")
        print("1.Food",(food_expense/budget)*100)
        print("2.Clothing", (clothing_expense / budget) * 100)
        print("3.Entertainment", (entertainment_expense / budget) * 100)

    # displaying infos of each category
    def display(self):
        print(food)
        print(clothing)
        print(entertainment)










# main of the program
if __name__=="__main__":
    # create budget class objects
    food = Category("Food")
    clothing = Category("Clothing")
    entertainment = Category("entertainment")
    while(True):
        budg = budgets()
        print("***************BUDGET APPLICATION*****************")
        print("*" * 50)
        budget = int(input("How much is your budget?\n"))
        print(f"Your total budget is ${budget}\n\n")
        main_option = int(input("Which category would you like to do access? \n 1. Food \n 2. Clothing \n 3. Entertainment \n 4. Exit \n5.Check statistics"))
        if main_option == 1:
            budg.food()
        elif main_option == 2:
            budg.clothing()
        elif main_option == 3:
            budg.entertainment()
        elif main_option == 4:
            exit()
        elif main_option == 5:
            # calculates money you are spending across class categories as a % of your total expenses
            budg.check_statistics()
        else:
            print("Invalid Input")













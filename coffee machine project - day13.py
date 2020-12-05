class CoffeeMachine:

    running = False #machine is off

    def __init__(self, water, milk, coffee_beans, cups, money):                                                                            
     #quantities of items the coffee machine already had
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

        #if the machine isnt running then start running from here
        if not CoffeeMachine.running:
            self.start()

    def start(self):
        self.running = True #machine is turned on(running)
        self.action = input("action to perform :-(order,report,off):\n")
        print()
        #possible choices to perform in the coffee machine
        if self.action == "order":
            self.order()
        elif self.action == "report":
            self.report()
        elif self.action == "off":
            exit()

    def order(self):
        self.choice =int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4- back to main menu:\n"))
        if self.choice == 1:
            self.reduced = [60, 0,7,1,0.50] # water, milk, coffee beans, cups, money
            if self.available_check():# checks if supplies are available
                if self.payment1():
                    print("Here is your espresso . Enjoy!")
                    self.deduct_supplies() # if it is, then it deducts

        elif self.choice == 2:
            self.reduced = [15, 40, 5, 1, 0.62]
            if self.available_check():
                if self.payment2():
                    print("Here is your latte . Enjoy!")
                    self.deduct_supplies()

        elif self.choice == 3:
            self.reduced = [15, 20, 5, 1,1.63]
            if self.available_check():
                if self.payment3():
                    print("Here is your cappuccino . Enjoy!")
                    self.deduct_supplies()

        elif self.choice == 4: 
            self.return_to_menu()

        self.return_to_menu()

    def report(self): # to display the quantities of supplies in the machine at the moment
        print(f"The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.coffee_beans}  grms of coffee beans")
        print(f"{self.cups} - disposable cups")
        print(f"${self.money} of money")
        self.return_to_menu()

    def available_check(self): # checks if it can afford making that type of coffee at the moment
        self.not_available = "" # by checking whether the supplies goes below 0 after it is deducted
        if self.water - self.reduced[0] < 0:
            self.not_available = "water"
        elif self.milk - self.reduced[1] < 0:
            self.not_available = "milk"
        elif self.coffee_beans - self.reduced[2] < 0:
            self.not_available = "coffee beans"
        elif self.cups - self.reduced[3] < 0:
            self.not_available = "disposable cups"

        if self.not_available != "": # if something was detected to be below zero after deduction
            print("Sorry, there is not enough ",self.not_available)
            return False
        else: # if everything is enough to make the coffee
            return True

    def deduct_supplies(self): #the used quantity of ingredients gets reduced and money gets added
        self.water -= self.reduced[0]
        self.milk -= self.reduced[1]
        self.coffee_beans -= self.reduced[2]
        self.cups -= self.reduced[3]
        self.money += self.reduced[4]

    def payment1(self):
        bill=float(input(" pay $0.50: "))
        if(bill==0.50):
            print("------transaction successful-------")
            return True
        elif(bill<0.50):
            print("------pay the cost ! transaction failed*------")
            return False
        elif(bill>0.50):
            print(" Here is ${:.2f}".format(bill-0.50)," dollars in change")
            return True

    def payment2(self):
        bill=float(input(" pay $0.62: "))
        if(bill==0.62):
            print("------transaction successful-------")
            return True
        elif(bill<0.62):
            print("------pay the cost ! transaction failed*------")
            return False
        elif(bill>0.62):
            print(" Here is ${:.2f}".format(bill-0.62)," dollars in change")
            return True

    def payment3(self):
        bill=float(input(" pay $1.63: "))
        if(bill==1.63):
            print("------transaction successful-------")
            return True
        elif(bill<1.63):
            print("------pay the cost ! transaction failed*------")
            return False
        elif(bill>1.63):
            print(" Here is ${:.2f}".format(bill-1.63)," dollars in change")
            return True     
        

    def return_to_menu(self): # returns to the menu after an action
        print()
        self.start()

print("WELCOME !!! Make your order from the MENU given below ")
print("----------------------------------MENU CARD---------------------------------------")
print("ITEM_NO          DRINKS                          COST       \n1.           espresso           :      $0.50\n2.           latte           :      $0.6\n3.           cappuccino           :      $1.43")
CoffeeMachine(1000, 550, 200, 20, 350) # water in ml, milk in ml, coffee beans(powder)in grms, cups, money present 
    

import pandas as pd
import csv
import datetime


class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
        

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class ClassicPizza(Pizza):
    def __init__(self):
     super().__init__("Classic Pizza Ingredients : Pizza Sauce, Mozzarella Cheese, Sausage, Mushroom, Green Pepper",
                       90)
     

class MargarithaPizza(Pizza):
    def __init__(self):
     super().__init__("Margaritha Pizza Ingredients : Pizza Sauce, Mozzarella Cheese, Tomato, Garden Rocket",
                       70)

class TurkishPizza(Pizza):
    def __init__(self):
     super().__init__("Turkish Pizza Ingredients : Pizza Sauce, Mozzarella Cheese, Pastrami, Onion, Roasted Peppers",
                       120)
     

class DominosPizza(Pizza):
    def __init__(self):
     super().__init__("Dominos Pizza Ingredients : Dominos Sauce, Mozzarella Cheese, Jambon, Corn, Sausage, Mushroom, Black Olive, Thyme",
                       110)

class Decorator(Pizza):
    
        def __init__(self, description, cost):
            super().__init__(description, cost)
    
        def get_cost(self):
            return self.Decorator.get_cost() + Pizza.get_cost(self)
    
        def get_description(self):
            return Pizza.get_description(self)
        
class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza.description + ", Olive", pizza.cost + 4.5)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 4.5

    def get_description(self):
        return self.pizza.get_description() + ", Olive"
    
class Mushroom(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza.description + ", Mushroom", pizza.cost + 6)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 6

    def get_description(self):
        return self.pizza.get_description() + ", Mushroom"

class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza.description + ", Goat Cheese", pizza.cost + 8)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 8

    def get_description(self):
        return self.pizza.get_description() + ", Goat Cheese"
    
class RoastBeef(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza.description + ", Roast Beef", pizza.cost + 14)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 14

    def get_description(self):
        return self.pizza.get_description() + ", Roast Beef"
    
class Onion(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza.description + ", Onion", pizza.cost + 3)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 3

    def get_description(self):
        return self.pizza.get_description() + ", Onion"
    
class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza.description + ", Corn", pizza.cost + 5)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 5

    def get_description(self):
        return self.pizza.get_description() + ", Corn"
    
class Cheddar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza.description + ", Cheddar", pizza.cost + 10)
        self.pizza = pizza

    def get_cost(self):
        return self.pizza.get_cost() + 10

    def get_description(self):
        return self.pizza.get_description() + ", Cheddar"


def main():
    file = """
    * Welcome to Hilal's pizza restaurant. Our pizza types:
     1: Classic Pizza
     2: Margaritha Pizza
     3: Turkish Pizza
     4: Dominos Pizza
    * and the sauces that you choose:
     11: Olive 
     12: Mushrooms
     13: GoatCheese
     14: RoastBeef
     15: Onion
     16: Corn
     17: Cheddar Cheese
    * Thanks!

    """

    myfile = open("menu_txt", "w", encoding="utf-8")
    myfile.write(file)

# main function
if __name__ == "__main__":
    main()

while True:
    PizzaChoice = int(input("Please choose a pizza base...:"))
    
    if PizzaChoice == 1:
        pizza = ClassicPizza()
    elif PizzaChoice == 2:
        pizza = MargarithaPizza()
    elif PizzaChoice == 3:
        pizza = TurkishPizza()
    elif PizzaChoice == 4:
        pizza = DominosPizza()
    else:
        print("Invalid choice")
        # go to the beginning of the loop
        continue

    SauceChoice = int(input("Please choose a pizza sauce...:"))    
    if SauceChoice == 11:
        Sauce = Olive(pizza)
    elif SauceChoice == 12:
        Sauce = Mushroom(pizza)
    elif SauceChoice == 13:
        Sauce = GoatCheese(pizza)
    elif SauceChoice == 14:
        Sauce = RoastBeef(pizza)
    elif SauceChoice == 15:
        Sauce = Onion(pizza)
    elif SauceChoice == 16:
        Sauce = Corn(pizza)
    elif SauceChoice == 17:
        Sauce = Cheddar(pizza)
    else:
        print("Sorry, you made wrong choice. Please try again...")
        # go to the beginning of the loop
        continue

    TotalCost = Sauce.get_cost() + pizza.get_cost()

    print("\nPlease enter your customer information...)")
    name = input("Please enter your name and surname...: ")
    identity = input("Please enter your identity number...: ")
    credit_card = input("Please enter your credit card number...: ")
    cvv_code = input("Please enter the three-digit security code that transmitted your phone...: ")
    

    flag = input("Do you want to continue? (Y/N): ")

    if flag == "Y" or flag =="y":
        print("Your order has been successfully confirmed, it will be ready soon... ")
        break
    else :
        print("See you soon")
        break

with open('Orders_Database.csv', 'a') as db:
    writer = csv.writer(db)
    writer.writerow([Sauce.get_description(), f"{Sauce.get_cost()}TL", name, identity, credit_card,
                     cvv_code, datetime.datetime.now()])



     





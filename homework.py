"""
Capital letters are class
Assignment: Shopping Cart  Implementation

Objective: Enhance your understanding of OOP by creating and integrating a shopping cart system using classes into a Jupyter Notebook.

Instructions:

1. Utilizing the Jupyter Notebook provided in today's session, design and develop a shopping cart system.

2. Once you've successfully developed the system, commit your assignment to your personal GitHub repository.

3. After committing, submit the link to your GitHub repository on the Google Assignment platform for review.

Classes:                            attributes:Items
Grocery_items                       name
Dairy                               category
Produce                             refridgerated [y]es or [n]o

"""
class Grocery_items:

    def __init__(self, name, amount, category, price, cold):
        self.name = name
        self.amount = amount
        self.category = category
        self.cold = cold
        self.price=price

    def add_amount_to_cart(self, addition_amount):
        self.amount += addition_amount
        print(f"adding, {addition_amount} to the cart. Total amount in cart:, {self.amount}")
        
    def what_kind(self):
        print(f'it is a {self.category}')

    def what_it_cost(self):
        print(f"how much we talkin? {self.price}")

    def fridge(self):
        friggy = input("Will this need to be refridgerated? [y]es or [n]o: ")
        if friggy.lower() == 'y':
            self.cold = "yes"
        else:
            self.cold = "no"

        # name, amount, category, price, cold):
mango = Grocery_items("mango", 3, "fruit", 2, "no")
milk = Grocery_items("milk", 1, "dairy", 4, "yes")


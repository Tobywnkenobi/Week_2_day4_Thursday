"""
OOP- Properties                     Behaviors
        name                        walk
        age                         talk
        address                     Breathe

    Classes create objects.         ESTANTIATE ESTANTIATE ESTANTIATE ESTANTIATE
Intance of a class.   The instance, class is blueprint.
G
"""
# some testers to cut and paste


# print(mango.add_amount_to_cart(2))
# print(mango.what_kind())
# print(mango.what_it_cost())
# print(mango.fridge())

# print(milk.add_amount_to_cart(2))
# print(milk.what_kind())
# print(milk.what_it_cost())
# print(milk.fridge())

# Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case¶

"""
two methods get_string  /       gets the string
print_string. / print the string

"""

class Stringy:
    def __init__(self):
        self.repeat_string = " "
                    
    def get_string(self):
        self.repeat_string = input("Enter whatever your heart's desire: ")
        
    def print_string(self):
        print(self.repeat_string.upper())
    
stringy_instance = Stringy()

stringy_instance.get.string()

stringy_instance.print.string()

  
# class Car(autom):
#     make = "Hyundai"
#     model = "Elantra"
#     Doors = 4
#     seats = 7

# honda = Car()
# toyota = Car()
# BMW = Car()
# hyundai = Car()
# Lamborghini = Car()



# print(toyota.color)
# print(BMW.make)
# print(honda.seats)



# class Vehicle:
#     def __init__(self, make, model,year, color, wheels, door,seats):
#         self.make = make
#         self.model = model
#         self.model = year
#         self.model = color
#         self.model = wheels
#         self.door = door
#         self.seats = seats
    
#     def __repr__(self):
#         return f"<Car:{self.make}{self.model}{self.year}{self.color}>"

#     def update_color(self, color):
#         self.color = color
#         print(self)

# vehicle = Vehicle('honda', 'civic', '2020', 'silver')

# vehicle.update_color('hot pink')



# class Vehicle:
#     def __init__(self, make, model,year, color, door,seats):
#         self.make = make
#         self.model = model
#         self.model = year
#         self.model = color
#         self.door = door
#         self.seats = seats
    
#     def __repr__(self):
#         return f"<Car:{self.make}{self.model}{self.year}{self.color}>"

#     def update_color(self, color):
#         self.color = color
#         print(self)

# vehicle = Vehicle('honda', 'civic', '2020', 'silver')

# vehicle.update_color('hot pink')
#
#
# Create class with 2 parameters inside of the __init__which are make and model

# Inside of the Car class create a method that has 4 parameter in total (self, year, door, seats)

# output: This car is from 2019 and is a ford explorer and has 4 doors and 5 seats


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def car_more(self, year, door, seats):
        print(f"This car is from {year} and is a {self.make} {self.model} and has a total of {door} doors and {seats} seats.")

my_car = Car("ford", "Explorer")  

answer = my_car.car_more(2019, 4, 5)
# print("car_info")

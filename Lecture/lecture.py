class Car(autom):
    make = "Hyundai"
    model = "Elantra"
    Doors = 4
    seats = 7

honda = Car()
toyota = Car()
BMW = Car()
hyundai = Car()
Lamborghini = Car()



# print(toyota.color)
# print(BMW.make)
# print(honda.seats)



class Car(autom):
    def __init__(self, make, model,door,seats):
        self.make = make
        self.model = model
        self.door = door
        self.seats = seats
    def get_make(self):
        return self.make
    
    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_doors(self):
        return self.doors
    
    def set_doors(self, doors):
        doors.self = doors

    def get_seats(self):
        return self.seats
    
    def set_seats(self, seats):
        seats.self = seats
        return Cars
        
    

print(f"This is a", {make},{model},". It has ",{door},"doors, and ",{seat}," seats.")


    

    
    







# class Car:
#     wheels = 5
    
#     def__init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.make = make
        
# car5 = Car('honda','fit',2008,'white')
# car6 = Car('chevy','impala',2008,'white')

# print(car5.make)
# print(car6.make)


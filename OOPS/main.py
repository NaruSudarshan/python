class Car:
    # class variable -> shared by all objects
    total_cars = 0
    
    def __init__(self,brand,model):
        # __brand is private
        self.__brand = brand
        self.__model = model
        
        # class variable that keeps count of no. of objects created 
        Car.total_cars += 1
        
    def full_name(self):
        print(f"{self.__brand} {self.__model}")
        
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol"
    
    # static methods belong to class
    @staticmethod # this is a decorator
    def general_desc():
        return "Cars are means of transport"
    
    @property # cannot write to model without setter
    def model(self):
        return self.__model

# inheritance
class ElectricCar(Car):   
    def __init__(self, brand, model ,battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(brand, model)
        
    def fuel_type(self):
        return "electric charge"


my_duster = Car("Renault","Duster")
my_duster.full_name()
# polymorphism
print(my_duster.fuel_type())

my_tesla = ElectricCar("Tesla","Model S","85kWh")
my_tesla.full_name()
# polymorphism
print(my_tesla.fuel_type())

# class variable
print(Car.total_cars)

# static method
print(Car.general_desc())

# encapsulation
print(my_tesla.get_brand()) 

# make model read only
# first should be private __ , create a model() and give property decorator
# print(my_duster.model())  --------> this is wrong
print(my_duster.model)

# check if instance belongs to a class
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass


# multiple inheritance
my_new_tesla = ElectricCarTwo("TEsla","Model A")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
#Classes are blueprints for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects.
class mode_of_transport:
    def __init__ (self, make, model, year):  # self is a reference to the current instance of the class, and is used to access variables that belong to the class. If we don't use self, Python will not know which variable we are referring to and will throw an error. 
        self.make = make
        self.model = model
        self.year = year   #You have to assign a variable to the parameters because the parameters you define as def __init__ (self, make, model, year) are limited to the init function, Once it's ended you can't access these parameters

    def move(self):
        print("My car moves")
    
    def make_model(self): #we mentioned self here because 
        print(f"My car is a {self.make} {self.model}")

     

my_car = mode_of_transport("Toyota corolla", "Grande", "2020")

print(my_car.make, my_car.model, my_car.year)

my_car.make_model()
my_car.move() 


#You can create multiple objects from the same class. These objects are called instances.
your_car = mode_of_transport("Honda", "Civic", "2025")

print(your_car.make, your_car.model, your_car.year)

your_car.make_model()
your_car.move() 

# Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. We can use inheritance to add more functionality to an existing class without modifying it.

class Airplane(mode_of_transport):
    def __init__(self, make, model, year, faa_id):
        super().__init__(make, model, year) #While making a init method in the derived class overwrites the init method of the base class. But we can super() function to keep the specific original init properties you need.
        self.faa_id = faa_id 

    def move(self):                     # This is called method overriding. We are overriding the move method of the base class mode_of_transport.
        print("My airplane flies")
    def make_model(self):
        print(f"My Airplane is a {self.make} {self.model} {self.year} {self.faa_id}")

class ship(mode_of_transport):
    def move(self):
        print("My ship sails")
    pass


my_plane = Airplane("Boeing", "747", "2005", "A12345")
my_plane.make_model()


my_ship = ship("Speedster", "5700", "2017")
my_ship.move()
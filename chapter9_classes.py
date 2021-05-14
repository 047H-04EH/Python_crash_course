"""
Creating a class
    When you create individual objects from the class, each object is automatically equipped with the general behavior; you 
    can then give each object whatever unique traits you desire. Making an object from a class is called instantiation, and you work with
    instances of a class.
"""

class Dog():
    """A simple attempt to model a dog."""
    def __init__(self,name,age):
        """Initialization name and age atrributes"""
        self.name=name
        self.age=age

    def sit(self):
         """Simulate a dog sitting in response to a command."""
         print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

"""
Notes on __init__()
    A function that's part of a class is a method. The only practical difference between a function and a class for now is
    the way we'll call methods. The __init__() method is a special method python runs automatically whenever we create a new instance
    based on the Dog class. We define the __init__() method to have three parameters: self, name, and age. The self parameter is required in
    the method definition, and it must come first before the other parameters. It must be included in the definition because when Python 
    calls this __init__() method later to create an instance of Dog, the method call will automatically pass the self argument. 
    Every method call associated with a class will automatically pass the self argument. Every method call associated with a class
    automatically passes self, which is a reference to the instance intself; it give the individual instance access to the attributes and
    methods in the class. 
"""

"""
Making an instance from a class
    Think of a class as a set of instructions for how to make an instance. The class Dog is a set of instructions that tells Python how to make individual
    instances representing specific dogs. Lets make an instance representing a specific dog. 
"""

my_dog=Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old")

"""Accessing attributes
    to access the attributes of an instance, you use dot notation. 
"""
my_dog.name

"""Calling methods
   after we create an instance from the class Dog, we can use dot notation to call any method defined in Dog. Lets make our dog roll over.
"""

my_dog.sit()
my_dog.roll_over()

"""Creating multiple instances
    you can create as many instances as your like. Each dog is a separate instance with its own set of attributes, capable of the same set of actions. 
"""

your_dog=Dog('lucy',3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("\nYour dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


"""Working with classes and instances
    You can use classes to represent many real-world situations.Once you write a class, youll spend
    most of your time working with instances created from that class. One of the first tasks youll 
    want to do is modify the attributes of an instance directly or write methods that update
    attributes in specific ways. 
"""

"""Modifying attribute values
    You can change an attributes value in three ways, you can change the value directly through an instance, 
    Set the value through a method, or increment the value through a method. Lets look at each of these.
"""

class Car():
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars mileage."""
        print("This car has " + str(self.odometer_reading)+ " miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading=mileage

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""Modifying an attributes value directly
    Here we set the odometer reading to 23 directly
"""
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


"""Modifying an attributes value through a method
    it can be helpful to have mthods that update certain attributes for you. 
    istead of accessing the attribute directly, you can pass the new value to a method
    that handles the updating internally. This is the 4th method in the Car class. 
"""

my_new_car.update_odometer(23)
my_new_car.read_odometer()

"""Inceementing an attributes value through a method
    Soetimes youll want to increment an attributes value by a certain amount rather than set an entirely new 
    value. Say we buy a used car and put 100 miles on it between the time we buy it and the time we
    register it. Heres a method that allows us to pass this incremental amount and add the value to the 
    odometer reading. Method 5 in the car class
"""

print("\n")

my_used_car=Car('subaru','outback',2003)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


"""Inheritance
    You dont always have to start from scratch when writing a class. If the class youre writing
    is a specialized version of another class you wrote, you can use inheritance. When one class
    inherits from another, it automatically takes on all the attributes and methods of the first
    class. The oroginal calss is called the aprent class, and the new class is the child class. 
    The child class inherits every attribute and method from its parent class but is also free 
    to define new attributes of its own. 
"""

class CarInheritance():
    """A simple attempt to represent a car and show inheritance"""

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year) + ' '+  self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(CarInheritance):
    """Represents aspects of car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery_size=70

    def describe_battery(self):
        """print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -KWh battery ")

    def fill_gas_tank(self):
        """Electric cars doent have gas tanks."""
        print("This car doesnt need a gas tank!")


my_tesla=ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


"""Defining attributes and methods for the child class
    see above for code example... Once you have a child class that inherits from a parent class, you can
    add any new attributes and methods necessary to diffeentiate the child class from the parent class. 
    Lets add an attribute thats specific to electric cars and a method to report on this attribute. 
    well store the batery size and write a method that prints a description of the battery. 
"""

"""Overriding methods from the parent class. 
    see above for code example... You can override any method from the parent class that doesnt fit what youre trying
    to model with the child class. To do this, you define a method in teh child class with the same name as the method
    you want to override in the parent class. Python will disregard the parent class method and only pay attention to 
    the method you define in the child class. Now if someone tries to call fill_gas_tank() with an electric car, Python
    will ignore the method fill_gas_tank() in Car and run this code instead."""

"""Instances as attributes.
    When modeling something from the real world in code, you may find that youre adding more and more detail to a class. 
    Youll find that you have a growing list of attributes and methods and that youre files are becoming lengthy. In 
    these situations, you might recognize that part of one class can be written as a separate class. You can break your
    large class into smaller classes that work together.
"""

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self,battery_size=70):
        """Initialize the batterys attributes."""
        self.battery_size=battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -KWh battery.")

class ElectricCar(CarInheritance):
    """Represents aspects of car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery=Battery()

    def describe_battery(self):
        """print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -KWh battery ")

    def fill_gas_tank(self):
        """Electric cars doent have gas tanks."""
        print("This car doesnt need a gas tank!")

my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()






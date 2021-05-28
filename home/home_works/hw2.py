# 1. Create a Vehicle class with max_speed and mileage instance attributes
import math


class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_vehicle(self):
        print(f'bus edet so skorostiu: {self.max_speed}, na rasstoyanie: {self.mileage}')

a = Vehicle(100, 16)
a.print_vehicle()
# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        self.seating_capacity = seating_capacity
        super().__init__(max_speed, mileage)

    def __str__(self):
        return f'{self.seating_capacity}'


bus = Bus(100, 501, 30)
print(bus)
bus.print_vehicle()
# 3. Determine which class a given Bus object belongs to (Check type of an object)
print(type(Bus))
print(issubclass(Bus, Vehicle))
# 4. Determine if School_bus is also an instance of the Vehicle class
print(isinstance(bus, Vehicle))
# 5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, get_school_id, number_of_sdudents):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_sdudents

    def __str__(self):
        return f'{self.get_school_id} {self.number_of_students}'

#6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color


class SchoolBus(School, Bus):

    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color: str):
        self.bus_school_color = bus_school_color
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)

    def print_schoolbus(self):
        print(f'color of Bus: {self.bus_school_color}')


schoolbus = SchoolBus(71, 13, 70, 153, 36, 'Red')
schoolbus.print_schoolbus()
schoolbus.print_school()
schoolbus.print_capacity()
print(isinstance(schoolbus, Bus))
#7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances,
# one of Bear and one of Wolf, make a tuple of it and by using for call their action using the same method.


class Bear:

    def make_sound(self):
        print(f'Bear')


class Wolf:
    def make_sound(self):
        print(f'Wolf')

bear = Bear()
wolf = Wolf()

animals = (bear, wolf)
for animal in animals:
    animal.make_sound()

#Magic methods:
#8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
#otherwise return message: "Your city is too small".

class City:

    def __init__(self, population):
        self.population = population

    def __new__(cls, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        return 'Your city is too small'

    def __str__(self):
        return f'{self.population}'

city = City(1500)
print(city)

#9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}


class City2:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City2, cls).__new__(cls)
        if population > 1500:
            return instance
        return 'Your city is too small'

    def __str__(self):
        return f'The population of the city {self.name} is {self.population}'


city = City2('New York', 15001)
print(city)

#10*. Override magic method add() to perform the additional action as 'multiply' (*)
# the value which is greater than 10. And perform this add (+) of two instances.


class New:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if self.number > 10:
            number1 = self.number * other.number
        else:
            number1 = self.number + other.number
        return New(number1)

    def __str__(self):
        return f'{self.number}'


new1 = New(11)
new2 = New(15)
new3 = new1 + new2
print(new3)

#11. The __call__ method enables Python programmers to write classes where the instances behave like functions
# and can be called like a function. Create a new class with call method and define this call to return sum.


class Call:

    def __call__(self, *args):
        return sum(args)

call = Call()
print(call(6, 7, 9, 11, 58))

#12*. Making Your Objects Truthy or Falsey Using bool().
#Create class MyOrder with cart and customer instance attributes.
#Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.


class MyOrder:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(order_1)
print(order_2)



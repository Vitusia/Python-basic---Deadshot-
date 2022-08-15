# 1 Create a class Vehicle with Attributes: name, max_speed, and total_capacity.
# Method: fare. It should calculate the price of the trip. Formula: total_capacity * 100.
# Example, total_capacity = 50 => fare = 5000
class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity
    def fare(self):
        return self.total_capacity * 100

# 2 Create classes Bus and Car that inherit Vehicle.
class Bus(Vehicle):
    def __int__(self, name, max_speed, total_capacity):
        super().__int__(name,max_speed, total_capacity)
class Car(Vehicle):
    def __int__(self, name, max_speed, total_capacity):
        super().__int__(name,max_speed, total_capacity)

# 3 Create 3 car objects and 2 bus objects
folkswagen = Car('Folkswagen', 220, 8)
mercedes = Car('Mercedes', 210, 6)
volvo = Car('Volvo', 190,5)
bohdan = Bus('Bohdan', 90, 44)
ruta = Bus('Ruta', 120, 97)
# 4 check: if car_1 is instance of Car.  if car_2 is instance of Vehicle.
# if bus_1 is instance of Car. if bus_1 is instance of Vehicle.
print(f'Folkswagen is instance of Car - {isinstance(folkswagen, Car)}')
print(f'Mercedes is instance of Vehicle - {isinstance(mercedes, Vehicle)}' )
print(f'Bohdan is instance of Car - {isinstance(bohdan, Car)}')
print(f'Bohdan is instance of Vehicle - {isinstance(bohdan, Vehicle)}')
# 5 Override fare method for Bus class. Here we need to add an extra 10% to the fare.
# Formula: total_fare + 10% of total_fare. Example, fare = 50 => total_fare = 5500
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name,max_speed, total_capacity)
    def fare(self):
        return total_capacity * 100 * 1.1

# 6 Add used_capacity attribute for Bus. It means how many people are on the bus.
# If used_capacity > total_capacity raise an error.
class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity, used_capacity):
        super().__init__(name,max_speed, total_capacity)
        self.used_capacity = used_capacity
        if used_capacity > total_capacity :
            raise "Error"
    def fare(self):
        return total_capacity * 100 * 1.1
# 7 Write a magic method to Bus that would be triggered when len() function is called.
# To figure out what magic method you should implement
    def __len__(self):
        return len(self.name)
# 8 and 9 and 10 Create class Engine with attribute volume and method get_volume() that will return volume.9 Inherit Engine by Car class. 10 Check what is inheritance order of the Car class
class Engine:
    def __init__(self, volume):
        self.volume = volume

    def get_volume(self):
        return self.volume

class Car(Vehicle, Engine):
    def __int__(self, name, max_speed, total_capacity):
        super().__int__(name, max_speed, total_capacity)


print(Car.mro())
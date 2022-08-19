## 1.Make the class with composition.
class Laptop:
    def __init__(self, model, color, battery_capacity):
        self.model = model
        self.color = color
        self.battery = Battery(battery_capacity)
    def __str__(self):
        return f' Laptop {self.model} \n {self.battery}'
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
    def __str__(self):
        return f'Battery capasity - {self.capacity}'

asus = Laptop('Aspire 2000', 'Black', '25 000')
print(asus)
# 2.
class Guitar:
    def __init__(self, string):
        self.string = string
class GuitarString:
    def __init__(self, lenth ):
        self.lenth = lenth
string = GuitarString(56)
guitar_1 = Guitar(string)
print(f'The lenth of any guitar string is {string.lenth}')
# 3   Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static
#     """
class Calc:
    @staticmethod
    def add_sums(first, second, third):
        add_sum = [first, second, third]
        return  sum(add_sum)
print(Calc.add_sums(1,4,5))
# 4*.Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        ingredients = ['forcemeat', 'tomatoes']
        return cls(ingredients)

    @classmethod
    def bolognaise(cls):
        ingredients = ['bacon', 'parmesan', 'eggs']
        return cls(ingredients)

pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)
# 5*.Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
class Concert:
    max_visitors_num = 0
    def __init__(self):
        self.__visitors_count = 0
    @property
    def visitors_count(self):
        return self.__visitors_count
    @visitors_count.setter
    def visitors_count(self, value):
        if value > Concert.max_visitors_num:
            self.__visitors_count = Concert.max_visitors_num
        else:
            self.__visitors_count = value
Concert.max_visitors_num = 99
concert = Concert()
concert.visitors_count = 999
print(concert.visitors_count)
print(Concert.max_visitors_num)
# 6. Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
import dataclasses
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    adress: str
    email: str
    birthday: str
    age: int
# 7. Create the same class (6) but using NamedTuple
from collections import namedtuple

AddressBookDataClass = namedtuple('AddressBookDataClass', ["key", "name", "phone_number", "address", "email", "birthday", "age"])

addressbook_1 = AddressBookDataClass('7', 'Vita','+380767234754', 'Kyiv, Ukraine', 'Vita@gmail.com', '10.02.2002', 20)
print(str(addressbook_1))
# 8. class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
#     """
class AddressBook(AddressBookDataClass):
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        super().__init__()

    def __str__(self):
        return f'Key: {self.key} \nName: {self.name} \nPhone: {self.phone_number} \nAddress: {self.address} ' \
               f'\nMail: {self.email} \nBirtday: {self.birthday} \nAge: {self.age}'


addressbook_2 = AddressBook('7', 'Vita','+380767234754', 'Kyiv, Ukraine', 'Vita@gmail.com', '10.02.2002', 20)
print(addressbook_2)
# 9.#     Change the value of the age property of the person object
class Person:

    name = "John"
    age = 36
    country = "USA"
setattr(Person, 'age', 20)
print(Person.age)
# 10.Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
class Student:
    id = 0
    name = ""
    def __init__(self, id, name):
        self.id = id
        self.name = name
setattr(Student, 'email', 'anna1999@gmail.com')
student_email = getattr(Student, 'email')
print(student_email)
# 11*. By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature
    @property
    def temperature(self):
        temperature_f = (self._temperature * 1.8) + 32
        return temperature_f
temperature_today = Celsius(18)
print(temperature_today.temperature)
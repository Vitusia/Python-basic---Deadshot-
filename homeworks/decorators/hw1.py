""""""
""" Task 1 
написати декоратор exception_wrapper - його задача подавити всі ексепшини які можуть згенеруватись в функції, і видати якийсь прінт
@exception_wrapper
def some_func(*args, **kwargs):
    pass   
Приклад використання якщо в some_func згенеровано ексепшн
>>> some_func()
Internal Error
* можна додатково зробити конкретні прінти для певних ексепшинів
наприклад функція генерує NoAccess
>>> some_func()
You hasn't access
"""
from random import randint
def exception_wrapper(func):
    def my_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except StopIteration:
            return "Iteration is done"
        except ZeroDivisionError:
            return'Can not be divided by zero'
        except IndexError:
            return 'list index out of range'
        except PermissionError:
            return 'You do not have access'
        except TypeError:
            return "Function is applied to an object of inappropriate type"

    return my_func

Exception_list = [StopIteration, ZeroDivisionError, TypeError]

@exception_wrapper
def rand_exc_func():
    raise Exception_list[randint(0,8)]
    return 'Here is your exception'

for i in range (5):
    print(rand_exc_func())

""" Task 2
Написати декоратор expect, його завдання перевірити на відповідність певній моделі, аргумент що передається в функцію
Приклад"""
class ValidationError(Exception):
    def __init__(self, data_to_check, expected, message='provided dict does not have the structure that we expect'):
        self.data_to_check = data_to_check
        self.expected = expected
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} \n expected: {self.expected} \n got: {self.data_to_check}'

def expect(data_dictionary: dict):
    def big_wrap(func):
        def wrap(data: dict):
            for key, value in data_dictionary.items():
                if value['required'] == True and key not in data:
                    raise ValidationError(data, data_dictionary)
                elif value['type'] != type(data.get(key)) and key in data:
                    raise ValidationError(data, data_dictionary)
                return func(data)
                return wrap
            return big_wrap

@expect
def send_user_data(data: dict):
    return data

my_dict = {
    "id": 76564,
    "name": "Mykhailo",
    "age": 55,
    "city": "Kyiv"
}


"""це означає що в словнику data, повинна бути обовязково пара з ключем id і name (тому що required=True),
додатково можуть бути пари з ключами age, city
якщо валідація даних не пройдена, згенерувати ексепшин ValidationError (ексепшин створити)

"""

""" Task 3
Написати декоратор marshal, його завдання перевірити на відповідність певній моделі, те що повертає функція

"""
def marshal(model: dict):
    def big_wrap(func):
        def wrap( **kwargs):
            res = func( **kwargs)
            for key, value in model.items():
                if key not in res and value['required'] == True:
                    res[key] = value['default']
                elif value.get('required') == True and res.get(key) == None:
                    raise ValidationError(res, model)
                elif value.get('type') != type(res.get(key)) and key in res:
                    raise ValidationError(res, model)
            return res
            return wrap
        return big_wrap
def create_profile(**kwargs):
    profile = {}
    for key , value in kwargs.items():
        profile[key] = value
    return profile

print(create_profile(
    id=80067,
    name='Victor',
    age=56,
    city='Kyiv'))

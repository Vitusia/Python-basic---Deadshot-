
# +Створіть клас робота пилососа
# +Робот пилосос має класові атрибути - обєм баку для сміття, обєм баку води
# +self атрибути - заповненість баку для сміття, заповненість баку для води, заряд батареї, серія/номер (ідентифікатор)
# Заряд батареї у відсотках
# заповнення баків для води і сміття - число
# наприклад
# Обєм баку для сміття - 1500
# заповнений обєм - 340
import logging
import random
from random import randint

class VacuumCleaner:
    volume_trash_tank = 500
    volume_water_tank = 600
    def __init__(self, fullness_trash_tank, fullness_water_tank, battery_charge, serial_number):
        self.fullness_trash_tank = int(fullness_trash_tank)
        self.fullness_water_tank = int(fullness_water_tank)
        self.battery_charge = battery_charge
        self.serial_number = str(serial_number)

        if 0 <= fullness_trash_tank <=self.fullness_trash_tank:
            self.fullness_trash_tank
        else:
            raise ValueError
        if 0 <= fullness_water_tank <= self.fullness_water_tank:
            self.fullness_water_tank
        else:
            raise ValueError
        if 0 <= battery_charge <=100:
            self.battery_charge
        else:
            raise ValueError
    @property
    def info(self):
        return f"{self.serial_number}; power - {self.battery_charge}%;" \
               f" water tank - {round(self.fullness_water_tank*100/self.fullness_water_tank)}%; " \
               f"trash tank - {round(self.fullness_trash_tank*100/self.fullness_trash_tank)}%  "

class LowBattery(BaseException):
    pass
class FullTrashTank(BaseException):
    pass
class EmptyWatterTank(BaseException):
    pass

    def battery_check(self):
        if self.battery_charge <=5:
            raise LowBattery
            print('Sorry, I need time to recharge')
        else:
            self.battery_charge -= 2

    def trash_check(self):
        add_trash = random.randint(0,20)
        if self.fullness_trash_tank == volume_trash_tank:
            raise FullTrashTank
        elif self.fullness_trash_tank != volume_trash_tank and self.fullness_trash_tank + add_trash >= volume_trash_tank:
            self.fullness_trash_tank = self.volume_trash_tank
        else:
            self.fullness_trash_tank += add_trash

    def wet_cleaning(self):
        if self.fullness_water_tank == 0:
            raise EmptyWatterTank
        elif self.fullness_water_tank > 0:
            self.fullness_water_tank -=20
            if self.fullness_water_tank < 0:
                self.fullness_water_tank = 0
                raise EmptyWatterTank

# 3. -----
# Реалізуйте функцію start_cleaning, функція може приймати параметр wet_cleaning: bool і time: int
#
# функція запускає прибирання
# прибирання це по суті цикл на time ітерацій
# на кожній ітерації циклу - може викликатись 2 чи 3 функції
    def start_cleaning(self, time, wet_cleaning):
        logging.info(f"{self.info} STARTED CLEANING")
        for i in range(time):
            try:
                self.battery_charge()
                self.fullness_trash_tank()
            except LowBattery:
                logging.error("LowBattery")
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            except FullTrashTank:
                logging.error("FullTrashTank")
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            if wet_cleaning:
                try:
                    self.wet_cleaning()
                except EmptyWaterTank:
                    logging.error("EmptyWaterTank")
                    return False
        logging.info(f"{self.info} FINISHED CLEANING")
        return True

My_Robot = VacuumCleaner(300, 300, 78, '76583587')
print(VacuumCleaner.info)
print(VacuumCleaner.fullness_water_tank(200))
print(VacuumCleaner.wet_cleaning())
#
#
# в циклі в якому викликаються дані 3 функції повинна бути конструкція try except для опрацювання ексепшинів
# ексепшини LowBattery, FullTrashTank - зупиняють прибирання
# ексепшин EmptyWatterTank - зупиняє тільки вологе прибирання
# якщо прибирання закінчилось достроково функція start_cleaning - повертає False
# якщо прибирання достроково не закінчувалось функуція start_cleaning - повертає True
# -----
#
# 4. -----
# добавте логи в start_cleaning
# лог - "VR-1234183; power - 95%; water tank - 60%; trash tank - 2% STARTED CLEANING"
# лог - згенеровано певний ексепшн
# лог - "VR-1234183; power - 0%; water tank - 2%; trash tank - 76% FINISHED CLEANING"
#
# -----
#
# ТЕСТИ!
# використовуючи бібліотеки unittest або pytest напишіть тести для робота
#
# тест-кейси які потрібно перевірити
# 1. повне прибирання на яке вистачає ресурсів
# 2. прибирання без вологого прибирання на яке вистачає ресурсів
# 3. прибирання під час якого не вистачило заряду батареї (перевірити що start_cleaning повернула False і що заряд батареї 0%)
# 4. прибирання під час якого заповнився сміттє бак (перевірити що start_cleaning повернула False і що сміттєбак повний)
# 5. прибирання під час якого не вистачило води (перевірити що start_cleaning повернула False і що бак з водою пустий)
# 6. проперті info повертає правильне значення
#
# бонус завдання і тест кейси які можна перевірити (не обовязкові)
# 1. при створенні обєкта робота, заряд батареї не може бути меншим ніж 0 і більшим ніж 100
# якщо в конструктор передали значення яке не не входить в діапазон 0-100 - кинути ексепшн ValueError
# написати тести які перевірить що при правильно переданих значеннях обєкт створюється, при не правильних - кидається ексепшин
#
# те ж саме можна опрацювати і перевірити для значення баків для сміття і води - (заповненість баку не повинна бути більша ніж обєм і менша ніж 0)
#
# 2. створіть обєкт робота, але при тестуванні викликайте на пряму функція_1, функція_2, функція_3
# створіть тести які перевірять що при певних значеннях буде кидатись ексепшн
#

#

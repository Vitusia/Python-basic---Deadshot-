# реалізувати класи ексепшинів LowBattery, FullTrashTank, EmptyWatterTank
from myErrors import LowBattery, FullTrashTank, EmptyWaterTank
from unittest import TestCase
import random
import logging

# self атрибути - заповненість баку для сміття, заповненість баку для води, заряд батареї, серія/номер (ідентифікатор)
# Заряд батареї у відсотках
# заповнення баків для води і сміття - число
# наприклад
# Обєм баку для сміття - 1500
# заповнений обєм - 340

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

#  Реалізувати проперті - info, яке повертає інформацію про поточний стан робота
# Приклад
# "VR-1234183; power - 95%; water tank - 35%; trash tank - 76%
# де VR-1234183 - серія/номер
    @property
    def info(self):
        return f"{self.serial_number}; power - {self.battery_charge}%;" \
               f" water tank - {round(self.fullness_water_tank*100/self.fullness_water_tank)}%; " \
               f"trash tank - {round(self.fullness_trash_tank*100/self.fullness_trash_tank)}%  "

    # функція_1 - зменшення заряду батареї
    def battery_check(self):
        if self.battery_charge <=5:
            raise LowBattery
            print('Sorry, I need time to recharge')
        else:
            self.battery_charge -= 2
    # функція_2 - заповнення сміттєбака
    def the_trash_check(self, volume_trash_tank):
        add_trash = random.randint(0,20)
        if self.fullness_trash_tank == volume_trash_tank:
            raise FullTrashTank
        elif self.fullness_trash_tank != volume_trash_tank and self.fullness_trash_tank + add_trash >= self.volume_trash_tank:
            self.fullness_trash_tank = self.volume_trash_tank
        else:
            self.fullness_trash_tank += add_trash
    # функція_3 - вологе прибирання
    def wet_cleaning(self):
        if self.fullness_water_tank == 0:
            raise EmptyWatterTank
        elif self.fullness_water_tank > 0:
            self.fullness_water_tank -=20
            if self.fullness_water_tank < 0:
                self.fullness_water_tank = 0
                raise EmptyWatterTank

# 3. -----
# # Реалізуйте функцію start_cleaning, функція може приймати параметр wet_cleaning: bool і time: int
# #
# # функція запускає прибирання
# # прибирання це по суті цикл на time ітерацій
# # на кожній ітерації циклу - може викликатись 2 чи 3 функції
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

robot = VacuumCleaner(300, 300, 78, 'Roborock')
print(robot.info)
print(robot.the_trash_check(200))
print(robot.wet_cleaning())

class TestRobotVacuumCleaner(TestCase):

    def setUp(self) -> None:
        self.test_cleaner = VacuumCleaner(0, 100, 100, "test_series")
        print(self.test_cleaner.info)

    def test_tearDown(self) -> None:
        self.test_cleaner = None

    def test_full_cleaning(self):
        self.assertTrue(self.test_cleaner.start_cleaning(True, 20))

    def test_dry_cleaning(self):
        self.assertTrue(self.test_cleaner.start_cleaning(False, 20))

    def test_battery_low(self):
        self.test_cleaner.battery_charge = 20
        self.assertFalse(self.test_cleaner.start_cleaning(False, 25))
        self.assertEqual(self.test_cleaner.battery_charge, 0)

    def test_full_waster(self):
        self.test_cleaner.filling_waste_tank = self.test_cleaner.volume_trash_tank - 500
        self.assertFalse(self.test_cleaner.start_cleaning(False, 25))
        self.assertEqual(self.test_cleaner.fullness_trash_tank, self.test_cleaner.volume_trash_tank)

    def test_no_water(self):
        self.test_cleaner.fullness_water_tank = 300
        self.assertFalse(self.test_cleaner.start_cleaning(True, 25))
        self.assertEqual(self.test_cleaner.fullness_water_tank, 0)

    def test_info(self):
        info = "identifier; power - 100%; water tank - 100%; waste tank - 0%"
        self.assertEqual(self.test_cleaner.info, info)


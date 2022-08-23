import random
import logging
logging.basicConfig(level=logging.INFO)
from unittest import TestCase


class LowBatteryError(Exception):
    def __init__(self):
        self.message = "Sorry, I need time to recharge!"

class FullTrashTankError(Exception):
    def __init__(self):
        self.message = "The Trash Tank is full, please, change it!"

class EmptyWatterTankError(Exception):
    def __init__(self):
        self.message = "Empty Watter Tank, please, add some water!"



class VacuumCleaner:
    volume_trash_tank = 1500
    volume_water_tank = 800

    def __init__(self, trash_tank: int, water_tank: int, battery_charge: int, serial_number):
        self.trash_tank = trash_tank
        if trash_tank < 0 or trash_tank > self.volume_trash_tank:
            raise ValueError
        self.water_tank = water_tank
        if water_tank < 0 or water_tank > self.volume_water_tank:
            raise ValueError
        self.battery_charge = battery_charge
        if battery_charge < 0 or battery_charge > 100:
            raise ValueError
        self.serial_number = serial_number

    @property
    def info(self):
        return {
            "sn": self.serial_number,
            "power": f"{self.battery_charge / 100 :.0%}",
            "water_tank": f"{self.water_tank / self.volume_water_tank:.0%}",
            "trash_tank": f"{self.trash_tank / self.volume_trash_tank:.0%}"}

    def status_battery(self):
        if self.battery_charge < 5:
            self.battery_charge = 0
            raise LowBatteryError
        else:
            self.battery_charge -= 2

    def status_trash_tank(self):
        add_trash = random.randint(0, 20)
        if self.trash_tank == self.volume_trash_tank:
            raise FullTrashTankError
        elif self.trash_tank != self.volume_trash_tank \
                and self.trash_tank + add_trash >= self.volume_trash_tank:
            self.trash_tank = self.volume_trash_tank
        else:
            self.trash_tank += add_trash

    def wet_cleaning(self):
        if self.water_tank == 0:
            raise EmptyWatterTankError
        elif self.water_tank > 0:
            self.water_tank -= 20
            if self.water_tank < 0:
                self.water_tank = 0
                raise EmptyWatterTankError

    def start_cleaning(self, wet_cleaning: bool, time: int):
        logging.info(f"{self.info} STARTED CLEANING")
        try:
            for i in range(time):
                self.status_battery()
                self.status_trash_tank()
            if wet_cleaning:
                self.wet_cleaning()
        except LowBatteryError:
            logging.error("LowBatteryError")
            logging.info(f"{self.info} STOPPED CLEANING")
            return False
        except FullTrashTankError:
            logging.error("FullTrashTankError")
            logging.info(f"{self.info} STOPPED CLEANING")
            return False
        except EmptyWatterTankError:
            logging.error("EmptyWatterTank")
            return False
        logging.info(f"{self.info} FINISHED CLEANING")
        return True

robot = VacuumCleaner(serial_number="VR-12345",
                       battery_charge=64,
                       water_tank=45,
                       trash_tank=935)
print(f"Info robot: {robot.info}")
print(robot.start_cleaning(True, 20))


# Tests
class TestVacuumCleaner(TestCase):
    """тест-кейси які потрібно перевірити"""
    def setUp(self) -> None:
        self.test_robot = VacuumCleaner(serial_number="VR-12345",
                                         battery_charge=54,
                                         water_tank=350,
                                         trash_tank=1050)
        print(f"Info test_robot: {self.test_robot.info}")

#1. повне прибирання на яке вистачає ресурсів
    def test_maximum_cleaning(self):
        self.assertTrue(self.test_robot.start_cleaning(wet_cleaning=True, time=25))

# 2. прибирання без вологого прибирання на яке вистачає ресурсів
    def test_dry_cleaning(self):
        self.assertTrue(self.test_robot.start_cleaning(wet_cleaning=False, time=25))

# 3. прибирання під час якого не вистачило заряду батареї
    def test_low_battery(self):
        self.test_robot.battery_charge = 30
        self.assertFalse(self.test_robot.start_cleaning(wet_cleaning=True, time=25))
        self.assertEqual(self.test_robot.battery_charge, 0)

# 4. прибирання під час якого заповнився сміттє бак
    def test_full_trash_tank(self):
        self.test_robot.trash_tank = self.test_robot.volume_trash_tank - 100
        self.assertFalse(self.test_robot.start_cleaning(wet_cleaning=True, time=25))
        self.assertEqual(self.test_robot.trash_tank, self.test_robot.volume_trash_tank)

 # 5. прибирання під час якого не вистачило води
    def test_empty_water_tank(self):
        self.test_robot.water_tank = 10
        self.assertFalse(self.test_robot.start_cleaning(wet_cleaning=True, time=25))
        self.assertEqual(self.test_robot.water_tank, 0)

# 6. проперті info повертає правильне значення
    def test_info_property(self):
        res = {'sn': 'VR-12345', 'power': '54%', 'water_tank': '44%', 'trash_tank': '70%'}
        self.assertEqual(self.test_robot.info, res)

class TestCreateObj(TestCase):
    def test_trash_tank_field(self):
        with self.assertRaises(ValueError):
            test_robot = VacuumCleaner(serial_number="VR-12345",
                                        battery_charge=54,
                                        water_tank=350,
                                        trash_tank=1501)
            print(test_robot.info)

    def test_water_tank_field(self):
        with self.assertRaises(ValueError):
            test_robot = VacuumCleaner(serial_number="VR-12345",
                                        battery_charge=54,
                                        water_tank=801,
                                        trash_tank=1050)
            print(test_robot.info)

    def test_battery_field(self):
        with self.assertRaises(ValueError):
            test_robot = VacuumCleaner(serial_number="VR-12345",
                                        battery_charge=101,
                                        water_tank=350,
                                        trash_tank=1050)
            print(test_robot.info)
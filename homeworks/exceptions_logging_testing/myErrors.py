class BatteryFailedException(Exception):
    def __init__(self, message='Battery cannot be more then 100'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class LowBattery(Exception):
    def __init__(self, message='Low battery, can not to continue cleaning, please charge!'):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message


class FullTrashTank(Exception):
    def __init__(self, message='The trash container is full, please clean it up!'):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message


class EmptyWaterTank(Exception):
    def __init__(self, message='The water tank is empty, wet cleaning mode is disabled'):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message
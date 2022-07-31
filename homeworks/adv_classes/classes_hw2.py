# Implement abstract class Figure with abc method check_cell
from abc import ABC , abstractmethod
class Figure(ABC):
    def __init__(self, name, coordinate, team):
        self.name = name
        self.coordinate = coordinate
        self.team = team
    @abstractmethod
    def check_cell(self):
        pass

    @property
    def display_name(self):
        return f'{self.name} ({self.team}) - {self.coordinate}'

    @classmethod
    def create_from_dict(cls, f_dict1: dict):
         return cls(name = f_dict1.get('FNAME'), coordinate=f_dict1.get('FCOORDINATE'), team = f_dict1.get('FTEAM'))
f_dict1 = {
    "FNAME": "Horse 1",
    "FCOORDINATE": (2, 2),
    "FTEAM": "black"
}
f_dict2 = {
    "FNAME": "Pawn 1",
    "FCOORDINATE": (8, 0),
    "FTEAM": "white"
}
class Horse(Figure):

    @property
    def check_cell(self):
        return f'{self.name} ({self.team}) is currently on {self.coordinate}'
    @check_cell.setter
    def check_cell(self, new_coordinate: tuple):
        self.coordinate = new_coordinate

horse1 = Horse.create_from_dict(f_dict1)
print(horse1.display_name)
# Horse 1 (black) - (2, 2)
horse1.check_cell = f_dict2.get("FCOORDINATE")
print(f'Horse 1 is successfully moved from {f_dict1.get("FCOORDINATE")} to {f_dict2.get("FCOORDINATE")}' )
# Horse 1 is successfully moved from (2, 2) to (8, 0)
class Pawn(Figure):

    @property
    def check_cell(self):
        return f'{self.name} ({self.team}) is currently on {self.coordinate}'
    @check_cell.setter
    def check_cell(self, new_coordinate: tuple):
        self.coordinate = new_coordinate

pawn_1 = Pawn.create_from_dict(f_dict2)
print(pawn_1.display_name)
# Pawn 1 (white) - (8, 0)
pawn_1.check_cell = f_dict1.get("FCOORDINATE")
print(f'Pawn 1 is successfully moved from {f_dict2.get("FCOORDINATE")} to {f_dict1.get("FCOORDINATE")}' )
# Pawn 1 is successfully moved from (8, 0) to (2, 2)

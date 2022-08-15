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

    def can_not_move(self, new_coordinate):
        print(f"{self.name} ({self.team}) - can't move on {new_coordinate}")

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
    def check_cell(self, new_coordinate: tuple):
        if self.team == 'white':
            if new_coordinate == (self.coordinate[0] + 1, self.coordinate[1]) and self.coordinate[0] < 8:
                self.move(new_coordinate)
            elif new_coordinate == (self.coordinate[0] + 2, self.coordinate[1]) and self.coordinate[0] == 2:
                self.move(new_coordinate)
            else:
                self.can_not_move(new_coordinate)
        else:
            if new_coordinate == (self.coordinate[0] - 1, self.coordinate[1]) and self.coordinate[0] > 1:
                self.move(new_coordinate)
            elif new_coordinate == (self.coordinate[0] - 2, self.coordinate[1]) and self.coordinate[0] == 7:
                self.move(new_coordinate)
            else:
                self.can_not_move(new_coordinate)

class Pawn(Figure):
    def check_cell(self, new_coordinate):
        x_abs = abs(self.coordinate[0] - new_coordinate[0])
        y_abs = abs(self.coordinate[1] - new_coordinate[1])
        if x_abs == 2 and y_abs == 1 or x_abs == 1 and y_abs == 2:
            self.move(new_coordinate)
        else:
            self.can_not_move(new_coordinate)

horse1 = Horse.create_from_dict(f_dict1)
print(horse1.display_name)
# Horse 1 (black) - (2, 2)
horse1.check_cell = f_dict2.get("FCOORDINATE")
print(f'Horse 1 is successfully moved from {f_dict1.get("FCOORDINATE")} to {f_dict2.get("FCOORDINATE")}' )
# Horse 1 is successfully moved from (2, 2) to (8, 0)

pawn_1 = Pawn.create_from_dict(f_dict2)
print(pawn_1.display_name)
# Pawn 1 (white) - (8, 0)
pawn_1.check_cell = f_dict1.get("FCOORDINATE")
print(f'Pawn 1 is successfully moved from {f_dict2.get("FCOORDINATE")} to {f_dict1.get("FCOORDINATE")}' )
# Pawn 1 is successfully moved from (8, 0) to (2, 2)
pawn_2 = Pawn('Pawn 2', (3, 4), 'white')
print(pawn_2.display_name)
pawn_2.check_cell((7,8))




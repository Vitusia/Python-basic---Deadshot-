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
    def create_from_dict(cls, data_dict):
        return cls(name=data_dict.get('FNAME'), coordinate=data_dict.get('FCOORDINATE'), team=data_dict.get('FTEAM'))


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

horse1 = Horse('Horse 1', (1, 2), 'white')
print(horse1.display_name)
# Horse 1 (white) - (1, 2)
horse1.check_cell((3, 3))
# Horse 1 (white) - can't move on (3, 3)


horse2 = Horse('Horse 2', (7, 5), 'black')
# Horse 2 (black) - (7, 5)
print(horse2.display_name)
horse2.check_cell((7,7))
# Horse 2 (black) - can't move on (7, 7)


pawn_1 = Pawn('Pawn 1', (6, 6), 'white')
print(pawn_1.display_name)
# Pawn 1 (white) - (6, 6)
pawn_1.check_cell((4,6))
# Pawn 1 (white) - can't move on (4, 6)


pawn_2 = Pawn('Pawn 2', (3, 4), 'white')
print(pawn_2.display_name)
# Pawn 2 (white) - (3, 4)
pawn_2.check_cell((7,8))
# Pawn 2 (white) - can't move on (7, 8)





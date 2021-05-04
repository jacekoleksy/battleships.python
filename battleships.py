import enum
class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def next(self):
        return Direction((self.value+1)%4)

class Ship:
    def __init__(self, xx, yy, direction, length):
        self.x = xx
        self.y = yy
        self.d = direction
        self.l = length

    @property
    def ship_coordinates(self):
        if self.d == Direction.NORTH:
            return [(self.x, self.y-i) for i in range(self.length)]
        if self.d == Direction.EAST:
            return [(self.x+i, self.y) for i in range(self.length)]
        if self.d == Direction.SOUTH:
            return [(self.x, self.y+i) for i in range(self.length)]
        if self.d == Direction.WEST:
            return [(self.x-i, self.y) for i in range(self.length)]

    def rotate(self):
        self.d = self.d.next

class Board:
    def __init__(self, size = 10, ship_list = [(4,1),(3,2),(2,3),(1,4)]):
        self.size = size
        self.ship_list = ship_list


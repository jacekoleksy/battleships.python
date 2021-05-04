import enum
import random

class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def next(self):
        return Direction((self.value + 1) % 4)

class Ship:
    def __init__(self, xx, yy, direction, length):
        self.x = xx
        self.y = yy
        self.direction = direction
        self.length = length

    @property
    def ship_fields(self):
        if self.direction == Direction.WEST:
            return [(self.x, self.y - i) for i in range(self.length)]
        if self.direction == Direction.SOUTH:
            return [(self.x + i, self.y) for i in range(self.length)]
        if self.direction == Direction.EAST:
            return [(self.x, self.y + i) for i in range(self.length)]
        if self.direction == Direction.NORTH:
            return [(self.x - i, self.y) for i in range(self.length)]

    @property
    def ship_overlay_fields(self):
        if self.direction == Direction.WEST:
            return [(self.x - 1, self.y - i) for i in range(-1, self.length + 1)] + [(self.x + 1, self.y - i) for i in range(-1, self.length + 1)] + [(self.x, self.y + 1), (self.x, self.y - self.length)]
        if self.direction == Direction.SOUTH:
            return [(self.x + i, self.y - 1) for i in range(-1, self.length + 1)] + [(self.x + i, self.y + 1) for i in range(-1, self.length + 1)] + [(self.x - 1, self.y), (self.x + self.length, self.y)]
        if self.direction == Direction.EAST:
            return [(self.x - 1, self.y + i) for i in range(-1, self.length + 1)] + [(self.x + 1, self.y + i) for i in range(-1, self.length + 1)] + [(self.x, self.y - 1), (self.x, self.y + self.length)]
        if self.direction == Direction.NORTH:
            return [(self.x - i, self.y - 1) for i in range(-1, self.length + 1)] + [(self.x - i, self.y + 1) for i in range(-1, self.length + 1)] + [(self.x + 1, self.y), (self.x - self.length, self.y)]

    @property
    def ship_overlay_fields_clear(self, size=10):
        return [row for idx, row in enumerate(self.ship_overlay_fields) if all(n >= 0 and n < size for n in row)]

    def rotate(self):
        self.direction = self.direction.next


class Board:
    def __init__(self, size=10, ship_list=[[1, 4], [2, 3], [3, 2], [4, 1]]):
        self.board = [['o' for i in range(10)] for j in range(10)]
        self.size = size
        self.available_ship_list = ship_list
        self.ship_list = []
        self.hits = 0
        self.hits_left = sum([x * y for [x, y] in self.available_ship_list])

    def is_available(self, ship):
        for x, y in ship.ship_fields:
            if x < 0 or y < 0 or x > self.size-1 or y > self.size-1 or self.board[x][y] != 'o':
                return False
        return True

    def add_ship(self, ship):
        for ship_length, num in self.available_ship_list:
            if ship_length == ship.length and num > 0:
                if self.is_available(ship):
                    #self.available_ship_list[ship_length - 1][1] -= 1
                    self.ship_list.append(ship)
                    for x, y in ship.ship_fields:
                        self.board[x][y] = str(ship.length)
                    for x, y in ship.ship_overlay_fields_clear:
                        self.board[x][y] = 'x'
                    return self.board
        print("Nie ma miejsca dla tego statku")
        return False

    def get_ship(self, x, y):
        for ship in self.ship_list:
            if (x, y) in ship.ship_fields:
                return ship
        return None

    def correct_target(self, x, y):
        if x not in range(self.size) or y not in range(self.size) or self.board[x][y] == '.' or self.board[x][y] == '^':
            return False
        return True

    def shoot(self, x, y):
        if not self.correct_target(x, y):
            return False
        if self.get_ship(x, y) is not None:
            self.board[x][y] = '^'
            self.hits += 1
            print("Gratulacje trafiles! \t Zostalo", self.hits_left-self.hits, "pol do trafienia!")
        else:
            self.board[x][y] = '.'
            print("Niestety, spróbuj jeszcze raz! \t Zostalo", self.hits_left-self.hits, "pol do trafienia!")
        return True

    def gameover(self):
        if self.hits_left == 0:
            return True
        return False

class RandomBoard(Board):
    def __init__(self, size=10, ship_list=[[1, 4], [2, 3], [3, 2], [4, 1]]):
        super().__init__(size, ship_list)
        for index in range(0, len(self.available_ship_list)):
            for i in range(0, self.available_ship_list[index-1][1]):
                ship_added = False
                while not ship_added:
                    x = random.randint(0, self.size-1)
                    y = random.randint(0, self.size-1)
                    ship_direction = random.choice(list(Direction))
                    ship = Ship(x, y, ship_direction, self.available_ship_list[index-1][0])
                    while self.is_available(ship):
                        self.add_ship(ship)
                        ship_added = True

class PlayerBoard(Board):
    def __init__(self, size=10, ship_list=[[1, 4], [2, 3], [3, 2], [4, 1]]):
        super().__init__(size, ship_list)
        for index in range(0, len(self.available_ship_list)):
            for i in range(0, self.available_ship_list[index][1]):
                ship_added = False
                while not ship_added:
                    print("Wielkosc statku:", self.available_ship_list[index][0])
                    x, y = input('Podaj x i y\t').split()
                    x = int(x)
                    y = int(y)
                    ship = Ship(x, y, Direction.NORTH, self.available_ship_list[index][0])
                    while self.is_available(ship):
                        self.add_ship(ship)
                        ship_added = True
                        print('\n'.join(str(p) for p in self.board))

board1 = RandomBoard()
print('\n'.join(str(p) for p in board1.board))
board2 = PlayerBoard()
print('\n'.join(str(p) for p in board2.board))


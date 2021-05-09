import enum
import random

global ship_added


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def next(self):
        return Direction((self.value + 1) % 4)


class Ship:
    def __init__(self, x, y, direction, length):
        self.x = x
        self.y = y
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
            return [(self.x - 1, self.y - i) for i in range(-1, self.length + 1)] + [(self.x + 1, self.y - i) for i in
                                                                                     range(-1, self.length + 1)] + [
                       (self.x, self.y + 1), (self.x, self.y - self.length)]
        if self.direction == Direction.SOUTH:
            return [(self.x + i, self.y - 1) for i in range(-1, self.length + 1)] + [(self.x + i, self.y + 1) for i in
                                                                                     range(-1, self.length + 1)] + [
                       (self.x - 1, self.y), (self.x + self.length, self.y)]
        if self.direction == Direction.EAST:
            return [(self.x - 1, self.y + i) for i in range(-1, self.length + 1)] + [(self.x + 1, self.y + i) for i in
                                                                                     range(-1, self.length + 1)] + [
                       (self.x, self.y - 1), (self.x, self.y + self.length)]
        if self.direction == Direction.NORTH:
            return [(self.x - i, self.y - 1) for i in range(-1, self.length + 1)] + [(self.x - i, self.y + 1) for i in
                                                                                     range(-1, self.length + 1)] + [
                       (self.x + 1, self.y), (self.x - self.length, self.y)]

    @property
    def ship_overlay_fields_clear(self, size=10):
        return [row for idx, row in enumerate(self.ship_overlay_fields) if all(0 <= n < size for n in row)]

    def rotate(self):
        self.direction = self.direction.next


class Board:
    def __init__(self, size=10):
        self.board = [['o' for i in range(size)] for j in range(size)]
        self.__size = size
        self.available_ship_list = [[1, 4], [2, 3], [3, 2], [4, 1]]
        self.ship_list = []
        self.hits = 0
        self.hits_left = sum([x * y for [x, y] in self.available_ship_list])

    def is_available(self, ship):
        for x, y in ship.ship_fields:
            if x < 0 or y < 0 or x > self.__size - 1 or y > self.__size - 1 or self.board[x][y] != 'o':
                return False
        return True

    def add_ship(self, ship):
        for ship_length, num in self.available_ship_list:
            if ship_length == ship.length and num > 0:
                if self.is_available(ship):
                    self.ship_list.append(ship)
                    for x, y in ship.ship_fields:
                        self.board[x][y] = str(ship.length)
                    for x, y in ship.ship_overlay_fields_clear:
                        self.board[x][y] = 'x'
                    return True
        return False

    def get_ship(self, x, y):
        for ship in self.ship_list:
            if (x, y) in ship.ship_fields:
                return ship
        return None

    def correct_target(self, x, y):
        if x not in range(self.__size) or y not in range(self.__size) or self.board[x][y] == '.' or self.board[x][y] == '^':
            return False
        return True

    def shoot(self, x, y):
        if not self.correct_target(x, y):
            return False
        if self.get_ship(x, y) is not None:
            self.board[x][y] = '^'
            self.hits += 1
            print("Gratulacje trafiles! \t Zostalo", self.hits_left - self.hits, "pol do trafienia!")
        else:
            self.board[x][y] = '.'
            print("Niestety, spróbuj jeszcze raz! \t Zostalo", self.hits_left - self.hits, "pol do trafienia!")
        return True

    def gameover(self):
        if self.hits == self.hits_left:
            return True
        return False


class RandomBoard(Board):
    def __init__(self, size=10):
        super().__init__(size)
        for index in range(0, len(self.available_ship_list)):
            for i in range(0, self.available_ship_list[index - 1][1]):
                ship_add = False
                while not ship_add:
                    x = random.randint(0, size - 1)
                    y = random.randint(0, size - 1)
                    ship_direction = random.choice(list(Direction))
                    ship = Ship(x, y, ship_direction, self.available_ship_list[index - 1][0])
                    while self.is_available(ship):
                        self.add_ship(ship)
                        ship_add = True


# class PlayerBoard(Board):
#     def __init__(self, size=10):
#         super().__init__(size)
#         for index in range(0, len(self.available_ship_list)):
#             for i in range(0, self.available_ship_list[index][1]):
#                 ship_add = False
#                 while not ship_add:
#                     pass
#                     print("Wielkosc statku:", self.available_ship_list[index][0])
#                     x, y = input('Podaj x i y\t').split()
#                     x = int(x)
#                     y = int(y)
#                     ship = Ship(x, y, Direction.NORTH, self.available_ship_list[index][0])
#                     while self.is_available(ship):
#                         self.add_ship(ship)
#                         ship_add = True


class Game:
    def __init__(self, size=10):
        self.player_board = Board(size)
        self.ai_board = RandomBoard(size)

    @staticmethod
    def player_shoot(ai_board, x, y):
        if ai_board.correct_target(x, y):
            ai_board.shoot(x, y)
            return True
        else:
            return False

    @staticmethod
    def random_shoot(player_board):
        x, y = -1, -1
        while not player_board.correct_target(x, y):
            x = random.randint(0, player_board._Board__size - 1)
            y = random.randint(0, player_board._Board__size - 1)
        player_board.shoot(x, y)
        return x, y

    def gameover(self):
        if self.ai_board.gameover():
            print("You Won")
            return True
        elif self.player_board.gameover():
            print("AI won")
            return True
        return False


class Error(Exception):
    pass


class NoShipThatSizeAvailable(Error):
    """You cant add a ship with that size"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class NoShipThatSizeAvailableException(Error):
    """You cant add a ship with that size"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        pass

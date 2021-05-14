import enum
import random

############## JACEK OLEKSY 134138 ################
###################################################
######## File responsible for functionality #######
###################################################

global ship_added  # Variable checks if ship was added


class Direction(enum.Enum):
    """
    Class Direction stores enum value for direction
    """
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def next(self):
        """Change direction to next (in order NESW)"""
        return Direction((self.value + 1) % 4)


class Ship:
    """
    Class Ship -> Stores ship object with important values
    ...
    Attributes
    ----------
    x : int
        x coordinate
    y : int
        y coordinate
    direction : Direction
        direction of the ship
    length : int
        length of the ship
    """
    def __init__(self, x, y, direction, length):
        """Initialize Ship object using class variables"""
        self.x = x
        self.y = y
        self.direction = direction
        self.length = length

    @property
    def ship_fields(self):
        """Returns list of ship fields"""
        if self.direction == Direction.WEST:
            return reversed([(self.x, self.y - i) for i in range(
                self.length)])  # Im using reversed to get the same order as EAST - just for displaying parts of the ship
        if self.direction == Direction.SOUTH:
            return reversed([(self.x + i, self.y) for i in range(
                self.length)])  # Im using reversed to get the same order as NORTH - just for displaying parts of the ship
        if self.direction == Direction.EAST:
            return [(self.x, self.y + i) for i in range(self.length)]
        if self.direction == Direction.NORTH:
            return [(self.x - i, self.y) for i in range(self.length)]

    @property
    def ship_overlay_fields(self):
        """Returns list of ship overlay fields"""
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
        """Returns list of fields around the ship minus fields out of range"""
        return [row for idx, row in enumerate(self.ship_overlay_fields) if all(0 <= n < size for n in row)]

    def rotate(self):
        """Change direction of a ship to next (in order NESW)"""
        self.direction = self.direction.next


class Board:
    """
    Class Board -> Stores board and important values for both players
    ...
    Attributes
    ----------
    board : [[char]]
         board stores ship and shot values
    size : int
         size of the board
    available_ship_list : [[int, int]]
        list of ships that you can use on this board: [x, y] -> x = ship length, y = number of ships
    ship_list : [Ship]
        list of ship objects that are placed on this board
    hits : int
        number of connected shots - hits
    hits_left : int
        sum of ship_length * number_of_ships to get number of fields to hit
    ai_hits : [[int, int]]
        list of coordinates used in AI_shot algorithm
    """
    def __init__(self, size=10):
        """Initialize Board object using class variables"""
        self.board = [['o' for i in range(size)] for j in range(size)]
        self.__size = size
        self.available_ship_list = [[1, 4], [2, 3], [3, 2], [4, 1]]
        self.ship_list = []
        self.hits = 0
        self.hits_left = sum([x * y for [x, y] in self.available_ship_list])
        self.ai_hits = []

    def is_available(self, ship):
        """Checks if its possible to place a ship"""
        for x, y in ship.ship_fields:
            if x < 0 or y < 0 or x > self.__size - 1 or y > self.__size - 1 or self.board[x][y] != 'o':
                return False
        return True

    def add_ship(self, ship):
        """Adds a ship to board and changes the values of the array fields"""
        for ship_length, num in self.available_ship_list:
            if ship_length == ship.length and num > 0:
                if self.is_available(ship):
                    self.ship_list.append(ship)
                    iter = 0
                    for x, y in ship.ship_fields:
                        iter += 1
                        if ship.length == 1:
                            self.board[x][y] = str(0)  # For 1-field ship, the value on index where its placed = '0'
                            break
                        if iter == 1:
                            self.board[x][y] = str(1)  # For the rest of a ships, stern index = '1'
                        elif iter == ship.length:
                            self.board[x][y] = str(3)  # For the rest of a ships, bow index = '3'
                        else:
                            self.board[x][y] = str(2)  # For the rest of a ships, center fields indexes = '2'
                    for x, y in ship.ship_overlay_fields_clear:
                        self.board[x][y] = 'x'  # Fields around the ships, are marked with 'x'
                    return True
        return False

    def get_ship(self, x, y):
        """Returns ship object which is placed on these coordinates"""
        for ship in self.ship_list:
            if (x, y) in ship.ship_fields:
                return ship
        return None

    def hit_and_sink(self, x, y):
        """Checks if ship on these coordinates is hit and sink, and if so - marks them as misses"""  # Because it isnt possible to hit another ship on those
        ship = self.get_ship(x, y)
        for (x, y) in ship.ship_fields:
            if self.board[x][y][-1] != '^':
                return False
        for (x, y) in ship.ship_overlay_fields_clear:
            self.board[x][y] = '.'
        return True

    def correct_target(self, x, y):
        """Checks if player can shot these coordinates"""  # Because player might try to shoot it earlier or coordinates are wrong
        if x not in range(self.__size) or y not in range(self.__size) or self.board[x][y][-1] == '.' or \
                self.board[x][y][-1] == '^':
            return False
        return True

    def shoot(self, x, y):
        """Shot at the field with these coordinates"""
        if not self.correct_target(x, y):
            return False
        if self.get_ship(x, y) is not None:
            self.board[x][y] += '^'
            self.hits += 1
        else:
            self.board[x][y] = '.'
        return True

    def gameover(self):
        """Checks if enemy destroyed every one of your ships"""
        if self.hits == self.hits_left:
            return True
        return False


class RandomBoard(Board):
    """
    Class Board -> Stores board and important values for RandomGenerated Board
    ...
    Attributes
    ----------
    Same as for the Board
    """
    def __init__(self, size=10):
        """Initialize RandomBoard object using Board __init__ but extended by random placed ships"""
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


class Game:
    """
    Class Game -> Stores boards for both players, responsible for shot validation
    ...
    Attributes
    ----------
    player_board : Board
        stores Board object for player
    ai_board : RandomBoard
        stores Board object for enemy (AI)
    """
    def __init__(self, size=10):
        """Initialize Game object using two Board objects - for player1 and player2"""
        self.player_board = Board(size)
        self.ai_board = RandomBoard(size)

    @staticmethod
    def player_shoot(ai_board, x, y):
        """Shoots field [x,y] on board passed as argument"""
        if ai_board.correct_target(x, y):
            ai_board.shoot(x, y)
            return True
        else:
            return False

    @staticmethod
    def random_shoot(player_board):
        """Shoots random field on board passed as argument"""
        x, y = -1, -1
        while not player_board.correct_target(x, y):
            x = random.randint(0, player_board._Board__size - 1)
            y = random.randint(0, player_board._Board__size - 1)
        player_board.shoot(x, y)
        return x, y

    @staticmethod
    def ai_shoot(player_board):
        """Shot on random field extended by AI"""
        if not len(player_board.ai_hits):
            x, y = -1, -1
            while not player_board.correct_target(x, y):
                x = random.randint(0, player_board._Board__size - 1)
                y = random.randint(0, player_board._Board__size - 1)
        elif len(player_board.ai_hits) == 1:
            x, y = -1, -1
            while not player_board.correct_target(x, y):
                y = player_board.ai_hits[0][1]
                x = random.randint(player_board.ai_hits[0][0] - 1, player_board.ai_hits[0][0] + 1)
                if x == player_board.ai_hits[0][0]:
                    y = random.randint(player_board.ai_hits[0][1] - 1, player_board.ai_hits[0][1] + 1)
        else:
            x, y = player_board.ai_hits[0]
            if not x == player_board.ai_hits[1][0]:
                while not player_board.correct_target(x, y):
                    x = random.randint(min(x[0] for x in player_board.ai_hits) - 1,
                                       max(x[0] for x in player_board.ai_hits) + 1)
            else:
                while not player_board.correct_target(x, y):
                    y = random.randint(min(y[1] for y in player_board.ai_hits) - 1,
                                       max(y[1] for y in player_board.ai_hits) + 1)
        if player_board.get_ship(x, y) is not None:
            player_board.board[x][y] += '^'
            player_board.hits += 1
            player_board.ai_hits.append([x, y])
            if player_board.hit_and_sink(x, y):
                player_board.ai_hits = []
        else:
            player_board.board[x][y] = '.'
        return True

    def gameover(self):
        """Checks which player has lost by number of fields"""
        if self.ai_board.gameover():
            return True
        elif self.player_board.gameover():
            return True
        return False

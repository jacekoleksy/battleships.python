import tkinter as tk
import time
import random

import battleships as bs


############## JACEK OLEKSY 134138 ################
###################################################
######### File responsible for interface ##########
###################################################

class Application(tk.Frame):
    def __init__(self, _root, _canvas):
        super().__init__(_root)
        self.__root = _root
        self.__root.geometry("1300x770")
        self.__root.title("Battleships.PY")
        self.__root.iconbitmap('images/icon.ico')
        self.__root.resizable(0, 0)

        self.__canvas = _canvas
        self.__canvas.pack(fill='both', expand=True)

        self.__background = tk.PhotoImage(file="images/background.png")
        self.__battleships = tk.PhotoImage(file="images/battleships.png")
        self.__canvas.create_image(0, 0, image=self.__background, anchor='nw')
        self.__canvas.create_image(145, 20, image=self.__battleships, anchor='nw')
        self.__canvas.image = self.__battleships
        self.__canvas.image = self.__background

        self.__img_win = tk.PhotoImage(file='images/win.png')
        self.__img_lose = tk.PhotoImage(file='images/x.png')
        self.__final_img_1 = None
        self.__final_img_2 = None
        self.__img_sea1 = tk.PhotoImage(file='images/sea1.png')
        self.__img_sea2 = tk.PhotoImage(file='images/sea2.png')
        self.__img_miss = tk.PhotoImage(file='images/miss.png')
        self.__img_hit = tk.PhotoImage(file='images/hit.png')

        self.__img_ship_we_dict = {'0': tk.PhotoImage(file='images/s0.png'), '1': tk.PhotoImage(file='images/s1.png'),
                                   '2': tk.PhotoImage(file='images/s2.png'), '3': tk.PhotoImage(file='images/s3.png')}
        self.__img_ship_ns_dict = {'0': tk.PhotoImage(file='images/s0.png'), '1': tk.PhotoImage(file='images/s4.png'),
                                   '2': tk.PhotoImage(file='images/s5.png'), '3': tk.PhotoImage(file='images/s6.png')}
        self.__img_hit_we_dict = {'0': tk.PhotoImage(file='images/h0.png'), '1': tk.PhotoImage(file='images/h1.png'),
                                  '2': tk.PhotoImage(file='images/h2.png'), '3': tk.PhotoImage(file='images/h3.png')}
        self.__img_hit_ns_dict = {'0': tk.PhotoImage(file='images/h0.png'), '1': tk.PhotoImage(file='images/h4.png'),
                                  '2': tk.PhotoImage(file='images/h5.png'), '3': tk.PhotoImage(file='images/h6.png')}

        self.create_widgets()

        self.__ship_direction = bs.Direction.NORTH
        self.__ship_length = 4
        self.__size = 10
        self.__reset_activate = False

    def create_widgets(self):
        self.__start = tk.Button(self.__root, text="Start game", fg="white", bg='#376f9f',
                                 font='WarHeliosCondCBold 25 bold', width=15, command=self.start_action)
        self.__canvas.create_window(140, 150, anchor='nw', window=self.__start)

        self.__quit = tk.Button(self.__root, text="Quit", fg="black", bg='#ffd545', font='WarHeliosCondCBold 25 bold',
                                width=15, command=self.__root.destroy)
        self.__canvas.create_window(920, 150, anchor='nw', window=self.__quit)

    def start_action(self):
        self.__start.destroy()

        self.__text_ship = tk.Label(self.__root, fg="white", bg='#00325b', width=30)
        self.__canvas.create_window(100, 442, anchor='nw', window=self.__text_ship)

        self.__image_ship = tk.PhotoImage(
            file="images/ship" + str(self.__ship_length) + str(self.__ship_direction.value + 1) + ".png")
        self.__image_ship_pick = self.__canvas.create_image(115, 480, image=self.__image_ship, anchor='nw')
        self.__canvas.image = self.__image_ship

        self.__text_command = tk.Label(self.__root, text="Set up your ships", fg="white", width=30, bg='#00325b',
                                       font='WarHeliosCondCBold 25 bold')
        self.__canvas.create_window(470, 660, anchor='nw', window=self.__text_command)

        self.__reset = tk.Button(self.__root, text="Reset", fg="white", bg='#376f9f', font='WarHeliosCondCBold 25 bold',
                                 width=15, command=self.reset_action)
        self.__canvas.create_window(660, 150, anchor='nw', window=self.__reset)

        self.__random = tk.Button(self.__root, text="Random board", fg="white", bg='#376f9f',
                                  font='WarHeliosCondCBold 25 bold', width=15, command=self.random_board)
        self.__canvas.create_window(400, 150, anchor='nw', window=self.__random)

        self.draw_player_board(self.__size)
        self.__game = bs.Game()

        self.__ship_type_buttons = []
        for i in range(len(self.__game.player_board.available_ship_list)):
            self.__ship_type_buttons.append(tk.Button(self.__root, fg="white", bg='#00325b', text=str(
                self.__game.player_board.available_ship_list[i][1]) + ' x ' + str(i + 1) + '-field ship',
                                                      command=lambda length=i: self.change_ship_length(length + 1),
                                                      width=13))
            self.__canvas.create_window(100, 320 + i * 30, anchor='nw', window=self.__ship_type_buttons[-1])

        self.__direction_buttons = []
        for i in bs.Direction:
            self.__direction_buttons.append(
                tk.Button(self.__root, fg="white", bg='#00325b', text='Direction ' + str(i.name),
                          command=lambda direction=i: self.change_direction(direction),
                          width=13))
            self.__canvas.create_window(220, 320 + i.value * 30, anchor='nw', window=self.__direction_buttons[-1])

    def reset_action(self):
        self.__start.destroy()
        self.draw_player_board(self.__size)
        self.__game.player_board = bs.Board(self.__game.player_board._Board__size)
        self.__text_command.configure(text="Set up your ships", width=30)

    def reset_action_ingame(self):
        for i in range(len(self.__enemy_fields_buttons)):
            self.__enemy_fields_buttons[i].destroy()
        self.__text_command.destroy()
        self.__canvas.delete(self.__legend_title)
        for i in range(len(self.__legend_x)):
            self.__canvas.delete(self.__legend_x[i])
            self.__canvas.delete(self.__legend_y[i])
        self.__canvas.delete(self.__final_img_1)
        self.__canvas.delete(self.__final_img_2)

        self.start_action()
        for i in bs.Direction:
            self.__canvas.create_window(220, 320 + i.value * 30, anchor='nw', window=self.__direction_buttons[-1])
        for i in range(len(self.__game.player_board.available_ship_list)):
            self.__canvas.create_window(100, 320 + i * 30, anchor='nw', window=self.__ship_type_buttons[-1])

        self.__reset_activate = True

    def random_board(self):
        self.draw_player_board(self.__size)
        self.__game.player_board = bs.RandomBoard(self.__size)
        self.change_colors_before_start(self.__game.player_board, self.__fields_buttons)
        self.__text_command.configure(text="Your board is ready! Press Play to start game", width=42)
        self.__start.destroy()
        self.__start = tk.Button(self.__root, text="Play", fg="white", bg='#376f9f',
                                 font='WarHeliosCondCBold 25 bold', width=15, command=self.play)
        self.__canvas.create_window(140, 150, anchor='nw', window=self.__start)

    def draw_player_board(self, size):
        self.__text_ship.configure(
            text="Current ship: " + str(self.__ship_length) + "-field, direction: " + str(self.__ship_direction.name))
        self.__canvas.create_text(490, 260, text="Your board:", font='WarHeliosCondCBold 25 bold', fill='#376f9f')
        self.__fields_buttons = []
        for num, i in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']):
            self.__canvas.create_text(470 + num * 32, 300, text=i, font='WarHeliosCondCBold 20 bold', fill='#376f9f')
        for i in range(10):
            self.__canvas.create_text(435, 303 + (i + 1) * 31.6, text=i + 1, font='WarHeliosCondCBold 20 bold',
                                      fill='#376f9f')
        for i in range(size):
            for j in range(size):
                self.__fields_buttons.append(
                    tk.Button(self.__root, fg="white", bg='#648cad', command=lambda x=i, y=j: self.add_ship(
                        bs.Ship(x, y, self.__ship_direction, self.__ship_length))))
                self.__fields_buttons[-1].configure(width='20px', height='20px', image=self.__img_sea1)
                self.__canvas.create_window(455 + j * 32, 318 + i / 10 * 320, anchor='nw',
                                            window=self.__fields_buttons[-1])

    def draw_enemy_board(self, size):
        self.__enemy_fields_buttons = []
        self.__legend_title = self.__canvas.create_text(890, 260, text="Enemy board:",
                                                        font='WarHeliosCondCBold 25 bold', fill='#ffd545')
        self.__legend_x = []
        self.__legend_y = []
        for num, i in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']):
            self.__legend_x.append(
                self.__canvas.create_text(855 + num * 32, 300, text=i, font='WarHeliosCondCBold 20 bold',
                                          fill='#ffd545'))
            self.__legend_y.append(
                self.__canvas.create_text(820, 303 + (num + 1) * 31.6, text=num + 1, font='WarHeliosCondCBold 20 bold',
                                          fill='#ffd545'))
        for i in range(size):
            for j in range(size):
                self.__enemy_fields_buttons.append(
                    tk.Button(self.__root, fg="white", bg="#254a5f", command=lambda x=i, y=j: self.shoot(x, y)))
                self.__enemy_fields_buttons[-1].configure(width='20px', height='20px', image=self.__img_sea2)
                self.__canvas.create_window(840 + j * 32, 318 + i / 10 * 320, anchor='nw',
                                            window=self.__enemy_fields_buttons[-1])
        print('\n'.join(str(p) for p in self.__game.ai_board.board))

    def add_ship(self, ship):
        if self.__game.player_board.add_ship(ship):
            self.__game.player_board.available_ship_list[ship.length - 1][1] -= 1
            for x, y in ship.ship_fields:
                if self.__game.player_board.get_ship(x,
                                                     y).direction == bs.Direction.WEST or self.__game.player_board.get_ship(
                        x, y).direction == bs.Direction.EAST:
                    self.__fields_buttons[x * 10 + y].configure(
                        image=self.__img_ship_we_dict[self.__game.player_board.board[x][y]])
                if self.__game.player_board.get_ship(x,
                                                     y).direction == bs.Direction.NORTH or self.__game.player_board.get_ship(
                        x, y).direction == bs.Direction.SOUTH:
                    self.__fields_buttons[x * 10 + y].configure(
                        image=self.__img_ship_ns_dict[self.__game.player_board.board[x][y]])
            for x, y in ship.ship_overlay_fields_clear:
                self.__fields_buttons[x * 10 + y].configure(image=self.__img_sea2)
            self.__ship_type_buttons[ship.length - 1].configure(
                text=str(self.__game.player_board.available_ship_list[ship.length - 1][1]) + ' x ' + str(
                    ship.length) + '-field ship')
        else:
            try:
                raise CannotPlaceThisShipException("CannotPlaceThisShipException",
                                                   "You cant place this ship o those coordinates")
            except CannotPlaceThisShipException as error:
                try:
                    print(error.args)
                    string = self.__text_command['text']
                    self.__text_command.configure(text="You cant place this ship here")
                    self.__root.update()
                    time.sleep(1)
                    self.__text_command.configure(text=string)
                except tk.TclError as error:
                    print("TclError", "You cant place this ship o those coordinates")
                    return False
        if sum([y for x, y in self.__game.player_board.available_ship_list]) == 0:
            self.__text_command.configure(text="Your board is ready! Press Play to start game", width=42)
            self.__start = tk.Button(self.__root, text="Play", fg="white", bg='#376f9f',
                                     font='WarHeliosCondCBold 25 bold', width=15, command=self.play)
            self.__canvas.create_window(140, 150, anchor='nw', window=self.__start)

    def play(self):
        self.__reset_activate = False
        self.__start.destroy()
        self.__random.destroy()
        self.__text_ship.destroy()
        for i in range(len(self.__ship_type_buttons)):
            self.__ship_type_buttons[i].destroy()
        for i in range(len(self.__direction_buttons)):
            self.__direction_buttons[i].destroy()
        self.__canvas.delete(self.__image_ship_pick)

        self.__reset.configure(command=self.reset_action_ingame)

        self.change_colors_before_start(self.__game.player_board, self.__fields_buttons)
        self.draw_enemy_board(self.__size)

        if random.randint(0, 1) == 0:
            self.__text_command.configure(text="Opponents turn")

            self.__root.update()
            time.sleep(0.5)

            self.__game.ai_shoot(self.__game.player_board)
            self.change_colors_ingame(self.__game.player_board, self.__fields_buttons)

        self.__text_command.configure(text='Your turn')

    def not_reset(self):
        if self.__reset_activate:
            raise ButtonErrorAfterClickException("ButtonErrorAfterClickException",
                                                 "You reset/finished the game - It isnt possible to shoot")

    def shoot(self, x, y):
        if not self.__game.gameover():
            self.__root.update()
            time.sleep(0.5)
            self.__root.update()
            try:
                self.not_reset()
            except (ButtonErrorAfterClickException, tk.TclError) as error:
                print(error.args)
                return False
            if self.__game.ai_board.shoot(x, y):
                self.change_colors_ingame(self.__game.ai_board, self.__enemy_fields_buttons)
                self.__text_command.configure(text='Opponents turn')

                self.gameover_print()
                self.__root.update()
                time.sleep(0.5)
                try:
                    self.not_reset()
                except (ButtonErrorAfterClickException, tk.TclError) as error:
                    print(error.args)
                    return False

                self.__game.ai_shoot(self.__game.player_board)
                self.change_colors_ingame(self.__game.player_board, self.__fields_buttons)
                self.__text_command.configure(text='Your turn')
        self.gameover_print()

    def gameover_print(self):
        if self.__game.ai_board.gameover():
            self.__text_command.destroy()
            self.__text_final = tk.Label(self.__root, text="You won", fg="white", width=10, bg='#00325b',
                                         font='WarHeliosCondCBold 25 bold')
            self.__canvas.create_window(700, 660, anchor='nw', window=self.__text_final)

            self.__final_img_1 = self.__canvas.create_image(625, 661, anchor='nw', image=self.__img_win)
            self.__final_img_2 = self.__canvas.create_image(880, 661, anchor='nw', image=self.__img_win)
            self.__canvas.image = self.__img_win

            self.__reset_activate = True

        elif self.__game.player_board.gameover():
            self.__text_command.destroy()
            self.__text_final = tk.Label(self.__root, text="AI won", fg="white", width=10, bg='#00325b',
                                         font='WarHeliosCondCBold 25 bold')
            self.__canvas.create_window(700, 660, anchor='nw', window=self.__text_final)

            self.__final_img_1 = self.__canvas.create_image(620, 657, anchor='nw', image=self.__img_lose)
            self.__final_img_2 = self.__canvas.create_image(890, 657, anchor='nw', image=self.__img_lose)
            self.__canvas.image = self.__img_lose

            self.__reset_activate = True
        try:
            self.not_reset()
        except (ButtonErrorAfterClickException, tk.TclError) as error:
            print(error.args)
            return False

    def change_colors_ingame(self, board, buttons):
        """Changes colors of board ingame"""
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                if board.board[i][j][-1] == '^':
                    if board.hit_and_sink(i, j) or board != self.__game.ai_board:
                        if board.get_ship(i, j).direction == bs.Direction.WEST or board.get_ship(i,
                                                                                                 j).direction == bs.Direction.EAST:
                            buttons[i * 10 + j].configure(image=self.__img_hit_we_dict[board.board[i][j][0]])
                        if board.get_ship(i, j).direction == bs.Direction.NORTH or board.get_ship(i,
                                                                                                  j).direction == bs.Direction.SOUTH:
                            buttons[i * 10 + j].configure(image=self.__img_hit_ns_dict[board.board[i][j][0]])
                    elif board == self.__game.ai_board:
                        buttons[i * 10 + j].configure(image=self.__img_hit)
                if not board.board[i][j].find('.'):
                    buttons[i * 10 + j].configure(image=self.__img_miss)

    def change_colors_before_start(self, board, buttons):
        """Changes colors of board before game starts"""
        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                if board.board[i][j] != 'o' and board.board[i][j] != 'x':
                    if board.get_ship(i, j).direction == bs.Direction.WEST or board.get_ship(i,
                                                                                             j).direction == bs.Direction.EAST:
                        buttons[i * 10 + j].configure(image=self.__img_ship_we_dict[board.board[i][j]])
                    if board.get_ship(i, j).direction == bs.Direction.NORTH or board.get_ship(i,
                                                                                              j).direction == bs.Direction.SOUTH:
                        buttons[i * 10 + j].configure(image=self.__img_ship_ns_dict[board.board[i][j]])
                else:
                    buttons[i * 10 + j].configure(image=self.__img_sea2)

    def change_ship_length(self, i):
        """Changes the length of current ship that you want to place"""
        self.__ship_length = i
        self.__text_ship.configure(
            text="Current ship: " + str(self.__ship_length) + "-field, direction: " + str(self.__ship_direction.name))
        self.__image_ship = tk.PhotoImage(
            file="images/ship" + str(self.__ship_length) + str(self.__ship_direction.value + 1) + ".png")
        self.__image_ship_pick = self.__canvas.create_image(115, 480, image=self.__image_ship, anchor='nw')
        self.__canvas.image = self.__image_ship

    def change_direction(self, i):
        """Changes the direction of current ship that you want to place"""
        self.__ship_direction = i
        self.__text_ship.configure(
            text="Current ship: " + str(self.__ship_length) + "-field, direction: " + str(self.__ship_direction.name))
        self.__image_ship = tk.PhotoImage(
            file="images/ship" + str(self.__ship_length) + str(self.__ship_direction.value + 1) + ".png")
        self.__image_ship_pick = self.__canvas.create_image(115, 480, image=self.__image_ship, anchor='nw')
        self.__canvas.image = self.__image_ship


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ButtonErrorAfterClickException(Error):
    """Exception raises when you queue up shots and during the shot you Reset the game"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class CannotPlaceThisShipException(Error):
    """Exception riases when you pick the wrong fields or you pick it during the game"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1300, height=700)

    app = Application(root, canvas)
    root.mainloop()
    # print('\n'.join(str(p) for p in self._game.player_board.board))
    # print('\n'.join(str(p) for p in self._game.ai_board.board))

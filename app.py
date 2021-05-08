import tkinter as tk
import time
import random
from tkinter import font

import battleships as bs



class Application(tk.Frame):
    def __init__(self, root, canvas):
        self.root = root
        self.root.geometry("1300x700")
        #self.root.resizable(0, 0)
        self.root.title("Battleships")

        self.canvas = canvas
        # self.canvas.create_image(0, 0, image=bg1, anchor='nw')
        # self.start = tk.Button(self.master, text="Start game", command=self.start)
        # self.my_button = self.root.create_window(10, 10, anchor='nw', window=self.start)
        # self.frame_menu = tk.Frame(self.master, width=200, height=100, padx=20, pady=40)
        # self.frame_menu.grid(row=0, column=0)
        #
        # self.frame_player1_text = tk.Frame(self.root,  width=400, height=100)
        # self.frame_player1_text.grid(row=0, column=1)
        # self.frame_player1_text.columnconfigure(0, weight=1)
        #
        # self.frame_player2_text = tk.Frame(self.root, width=400, height=100)
        # self.frame_player2_text.grid(row=0, column=2)
        # self.frame_player2_text.columnconfigure(0, weight=1)
        #
        # self.frame_ships = tk.Frame(self.root, width=200, height=400, padx=50, pady=50)
        # self.frame_ships.grid(row=1, column=0)
        #
        # self.frame_player1_board = tk.Frame(self.root, width=400, height=400)
        # self.frame_player1_board.grid(row=1, column=1)
        #
        # self.frame_player2_board = tk.Frame(self.root, width=400, height=400)
        # self.frame_player2_board.grid(row=1, column=2)
        #
        # for frame in [self.frame_menu, self.frame_ships, self.frame_player1_board, self.frame_player2_board, self.frame_player1_text, self.frame_player2_text]:
        #     frame.grid_propagate(0)
        #     frame.grid(sticky="nswe")
        #
        self.create_widgets()

        self.ship_direction = bs.Direction.NORTH
        self.ship_length = 4
        self.size = 10

    def create_widgets(self):
        self.start = tk.Button(self.root, text="Start game", command=self.start_action, width=11)
        # self.start.grid(row=0, column=0, pady=40)
        self.canvas.create_window(10, 10, anchor='nw', window=self.start)

        self.quit = tk.Button(self.root, text="Quit", fg="red", command=self.root.destroy, width=11)
        # self.quit.grid(row=0, column=0, pady=40)
        self.canvas.create_window(105, 10, anchor='nw', window=self.quit)

    def start_action(self):
        self.start.destroy()

        self.text1 = tk.Label(self.root, text="Welcome to Battleships", fg="white", bg='#20445a', width=30)
        # self.text1.grid(row=0, column=0, pady=40)
        self.canvas.create_window(10, 472, anchor='nw', window=self.text1)

        self.text2 = tk.Label(self.root, text="Set up your ships", fg="white", width=30, bg='#20445a', font='WarHeliosCondCBold 25 bold')
        # self.text2.grid(row=0, column=0, pady=40)
        self.canvas.create_window(470, 600, anchor='nw', window=self.text2)

        self.reset = tk.Button(self.root, text="Reset", fg="blue", command=self.reset_action, width=11)
        # self.reset.pack(side="left")
        # self.reset.place(relx=0.49)
        self.canvas.create_window(10, 45, anchor='nw', window=self.reset)

        self.random = tk.Button(self.root, text="Random board", fg="blue", command=self.random_board, width=11)
        # self.random.pack(side="top")
        # self.random.place(rely=0.69)
        self.canvas.create_window(105, 45, anchor='nw', window=self.random)

        self.draw_player_board(self.size)
        self.game = bs.Game()

        self.ship_type_buttons = []
        for i in range(len(self.game.player_board.available_ship_list)):
            self.ship_type_buttons.append(tk.Button(self.root, text=str(i+1) + '-field ship', command=lambda i=i: self.change_ship_length(i+1), width=13))
            #self.ship_type_buttons[-1].grid(row=i, column=1)
            self.canvas.create_window(70, 350 + i * 30, anchor='nw', window=self.ship_type_buttons[-1])

        self.direction_buttons = []
        for i in bs.Direction:
            self.direction_buttons.append(tk.Button(self.root, text='Direction '+str(i.name), command=lambda i=i: self.change_direction(i), width=13))
            #self.direction_buttons[-1].grid(row=4+i.value, column=1)
            self.canvas.create_window(70, 500 + i.value * 30, anchor='nw', window=self.direction_buttons[-1])

        print('\n'.join(str(p) for p in self.game.ai_board.board))
        print('\n')
        print('\n'.join(str(p) for p in self.game.player_board.board))

    def random_board(self):
        self.draw_player_board(self.size)
        self.game.player_board = bs.RandomBoard(self.size)
        self.change_colors_player(self.game.player_board.board, self.fields_buttons)
        print('\n'.join(str(p) for p in self.game.player_board.board))
        self.text2.configure(text="Your board is ready! Press Play to start game", width=42)
        self.start = tk.Button(self.root, text="Play", command=self.start_game, width=11)
        self.canvas.create_window(10, 10, anchor='nw', window=self.start)

    def reset_action(self):
        self.start.destroy()
        self.draw_player_board(self.size)
        self.game.player_board = bs.Board(self.game.player_board.size)
        self.text2.configure(text="Set up your ships", width=30)
        self.start = tk.Button(self.root, text="Start game", command=self.start_action, width=11)
        # self.start.grid(row=0, column=0, pady=40)
        self.canvas.create_window(10, 10, anchor='nw', window=self.start)

    def reset_action_ingame(self):
        for i in range(len(self.enemy_fields_buttons)):
            self.enemy_fields_buttons[i].destroy()
        self.text2.destroy()
        self.start_action()
        #self.game.ai_board = bs.RandomBoard(self.size)
        #self.start.configure()

    def draw_player_board(self, size):
        self.text1.configure(text="Current ship: "+str(self.ship_length)+"-field, direction: " + str(self.ship_direction.name))
        self.canvas.create_text(650, 250, text="YOUR BOARD", font='WarHeliosCondCBold 25 bold', fill='white')
        self.fields_buttons = []
        for num, i in enumerate(['A','B','C','D','E','F','G','H','I','J']):
            letter = tk.Label(self.root, text=i, height=2, width=4)
            #letter.grid(row=0, column=num+1)
            self.canvas.create_text(505 + num * 30, 300, text=i, font='WarHeliosCondCBold 15 bold')
        for i in range(10):
            number = tk.Label(self.root, text=str(i), height=2, width=4)
            #number.grid(row=i+1, column=0)
            self.canvas.create_text(470, 305 + (i + 1) * 25, text=i+1, font='WarHeliosCondCBold 15 bold')
        for i in range(size):
            for j in range(size):
                self.fields_buttons.append(tk.Button(self.root, text=str(chr(65+i))+' '+str(j+1), fg="white", bg='#648cad', height=1, width=3, command=lambda i=i, j=j: self.add_ship(bs.Ship(i, j, self.ship_direction, self.ship_length))))
                #self.fields_buttons[-1].grid(row=i+1, column=j+1)
                self.canvas.create_window(490 + j * 30, 318 + i/10 * 250, anchor='nw', window=self.fields_buttons[-1])

    def add_ship(self, ship):
        if self.game.player_board.add_ship(ship):
            self.game.player_board.available_ship_list[ship.length-1][1] -= 1
            for x, y in ship.ship_fields:
                self.fields_buttons[x*10+y].configure(background='#022107')
            for x, y in ship.ship_overlay_fields_clear:
                self.fields_buttons[x * 10 + y].configure(background='#1a405c')
        if sum([y for x, y in self.game.player_board.available_ship_list]) == 0:
            self.text2.configure(text="Your board is ready! Press Play to start game", width=42)
            print('\n'.join(str(p) for p in self.game.player_board.board))
            print('\n'.join(str(p) for p in self.game.ai_board.board))
            self.start = tk.Button(self.root, text="Start game", command=self.start_game, width=11)
            self.canvas.create_window(10, 10, anchor='nw', window=self.start)

    def start_game(self):
        self.random.destroy()
        self.reset.configure(command=self.reset_action_ingame)
        self.change_colors_player(self.game.player_board.board, self.fields_buttons)
        self.draw_enemy_board(self.size)
        self.play()

    def draw_enemy_board(self, size):
        self.enemy_fields_buttons = []
        self.canvas.create_text(990, 250, text="ENEMY BOARD", font='WarHeliosCondCBold 25 bold', fill='white')
        for num, i in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']):
            letter = tk.Label(self.root, text=i, height=2, width=4)
            #letter.grid(row=0, column=num + 1)
            self.canvas.create_text(855 + num * 30, 300, text=i, font='WarHeliosCondCBold 15 bold')
        for i in range(10):
            number = tk.Label(self.root, text=str(i), height=2, width=4)
            #number.grid(row=i + 1, column=0)
            self.canvas.create_text(820, 305 + (i + 1) * 25, text=i + 1, font='WarHeliosCondCBold 15 bold')
        for i in range(size):
            for j in range(size):
                self.enemy_fields_buttons.append(tk.Button(self.root, text=str(chr(65+i))+' '+str(j+1), fg="white", bg="#254a5f", height=1, width=3, command=lambda i=i, j=j: self.shoot(i, j)))
                #self.enemy_fields_buttons[-1].grid(row=i + 1, column=j + 1)
                self.canvas.create_window(840 + j * 30, 318 + i / 10 * 250, anchor='nw', window=self.enemy_fields_buttons[-1])

    def shoot(self, x, y):
        self.root.update()
        time.sleep(0.5)
        self.root.update()
        if not self.game.gameover():
            if self.game.ai_board.shoot(x, y):
                self.change_colors_battle(self.game.ai_board.board, self.enemy_fields_buttons)
                self.text2.configure(text='Opponents turn')

                self.root.update()
                time.sleep(0.5)

                self.game.random_shoot(self.game.player_board)
                self.change_colors_battle(self.game.player_board.board, self.fields_buttons)
                self.text2.configure(text='Your turn')
        if self.game.ai_board.gameover():
            self.text2.destroy()
            self.textfinal = tk.Label(self.root, text="You won", fg="white", width=10, bg='#20445a', font='WarHeliosCondCBold 25 bold')
            self.canvas.create_window(700, 600, anchor='nw', window=self.textfinal)
            self.img_win = tk.PhotoImage(file='images/win.png')
            self.canvas.create_image(625, 601, anchor='nw', image=self.img_win)
            self.canvas.create_image(880, 601, anchor='nw', image=self.img_win)
            self.canvas.image = self.img_win
        elif self.game.player_board.gameover():
            self.text2.destroy()
            self.textfinal = tk.Label(self.root, text="You won", fg="white", width=10, bg='#20445a', font='WarHeliosCondCBold 25 bold')
            self.canvas.create_window(700, 600, anchor='nw', window=self.textfinal)
            self.img_win = tk.PhotoImage(file='images/win.png')
            self.canvas.create_image(630, 601, anchor='nw', image=self.img_win)
            self.canvas.create_image(890, 601, anchor='nw', image=self.img_win)
            self.canvas.image = self.img_win


    def play(self):
        self.start.destroy()
        if random.randint(0, 1) == 0:
            self.text2.configure(text="Opponents turn")
            self.root.update()
            time.sleep(0.5)
            self.game.random_shoot(self.game.player_board)
            self.change_colors_battle(self.game.player_board.board, self.fields_buttons)
        self.text2.configure(text='Your turn')

    def change_colors_battle(self, board, buttons):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '^':
                    buttons[i*10+j].configure(background="green")
                if board[i][j] == '.':
                    buttons[i*10+j].configure(background="#760000")

    def change_colors_player(self, board, buttons):
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(len(buttons), i*10+j)
                if board[i][j] != 'o' and board[i][j] != 'x':
                    buttons[i * 10 + j].configure(background="#022107")
                else:
                    buttons[i * 10 + j].configure(background="#254a5f")

    def change_ship_length(self, i):
        self.ship_length = i
        print(self.ship_length)
        self.text1.configure(text="Current ship: "+str(self.ship_length)+"-field, direction: " + str(self.ship_direction.name))

    def change_direction(self, i):
        self.ship_direction = i
        print(self.ship_direction.name)
        self.text1.configure(text="Current ship: "+str(self.ship_length)+"-field, direction: " + str(self.ship_direction.name))

if __name__ == "__main__":
    root = tk.Tk()
    print(tk.font.families())
    canvas = tk.Canvas(root, width=1300, height=700)
    canvas.pack(fill='both', expand=True)
    background = tk.PhotoImage(file="images/background.png")
    canvas.create_image(0, 0, image=background, anchor='nw')
    battleships = tk.PhotoImage(file="images/battleships.png")
    canvas.create_image(230, 20, image=battleships, anchor='nw')
    app = Application(root, canvas)
    # my_canvas = tk.Canvas(root, width=1000, height=500)
    # my_canvas.grid(row=0, column=0)
    # bg1 = tk.PhotoImage(file="images/2.png")
    # #bg2 = tk.PhotoImage(file="images/2.jpg")
    # my_canvas.create_image(0,0, image=bg1, anchor='nw')
    # root.mainloop()
    root.mainloop()
import tkinter as tk
import time
import random
import battleships as bs


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.master.geometry("1000x500")
        self.master.resizable(0, 0)
        self.master.title("Battleships")

        self.frame_menu = tk.Frame(self, bg="black", width=200, height=100, padx=20, pady=40)
        self.frame_menu.grid(row=0, column=0)

        self.frame_player1_text = tk.Frame(self, bg="orange", width=400, height=100)
        self.frame_player1_text.grid(row=0, column=1)
        self.frame_player1_text.columnconfigure(0, weight=1)

        self.frame_player2_text = tk.Frame(self, bg="pink", width=400, height=100)
        self.frame_player2_text.grid(row=0, column=2)
        self.frame_player2_text.columnconfigure(0, weight=1)

        self.frame_ships = tk.Frame(self, bg="yellow", width=200, height=400, padx=50, pady=50)
        self.frame_ships.grid(row=1, column=0)

        self.frame_player1_board = tk.Frame(self, bg="green", width=400, height=400)
        self.frame_player1_board.grid(row=1, column=1)

        self.frame_player2_board = tk.Frame(self, bg="blue", width=400, height=400)
        self.frame_player2_board.grid(row=1, column=2)

        for frame in [self.frame_menu, self.frame_ships, self.frame_player1_board, self.frame_player2_board, self.frame_player1_text, self.frame_player2_text]:
            frame.grid_propagate(0)
            frame.grid(sticky="nswe")

        self.create_widgets()

        self.ship_direction = bs.Direction.NORTH
        self.ship_length = 4


    def create_widgets(self):
        self.start = tk.Button(self.frame_menu, text="Start game", command=self.start)
        self.start.pack(side="left")

        self.quit = tk.Button(self.frame_menu, text="Quit", fg="red", command=self.master.destroy)
        self.quit.pack(side="right")

        self.text1 = tk.Label(self.frame_player1_text, text="Welcome to Battleships", fg="red")
        self.text1.grid(row=0, column=0, pady=40)

        self.text2 = tk.Label(self.frame_player2_text, text="Created by: Jacek Oleksy PK 2021", fg="red")
        self.text2.grid(row=0, column=0, pady=40)

    def start(self):
        self.reset = tk.Button(self.frame_menu, text="Reset", fg="blue", command=self.reset_action)
        self.reset.pack(side="left")
        self.reset.place(relx=0.49)
        self.draw_Player_Board(10)
        self.game = bs.Game()

        self.ship_type_buttons = []
        for i in range(len(self.game.player_board.available_ship_list)):
            self.ship_type_buttons.append(tk.Button(self.frame_ships, text=str(i+1) + '-field ship', command=lambda i=i: self.change_ship_length(i+1)))
            self.ship_type_buttons[-1].grid(row=i, column=1)

        self.direction_buttons = []
        for i in bs.Direction:
            self.direction_buttons.append(tk.Button(self.frame_ships, text='Direction'+str(i.name), command=lambda i=i: self.change_direction(i)))
            self.direction_buttons[-1].grid(row=4+i.value, column=1)

        print('\n'.join(str(p) for p in self.game.ai_board.board))
        print('\n')
        print('\n'.join(str(p) for p in self.game.player_board.board))


    def reset_action(self):
        self.draw_Player_Board(10)
        self.game.player_board = bs.Board(self.game.player_board.size)

    def draw_Player_Board(self, size):
        self.text1.configure(text="Current ship: "+str(self.ship_length)+"-field, direction: " + str(self.ship_direction.name))
        self.fields_buttons = []
        for num, i in enumerate(['A','B','C','D','E','F','G','H','I','J']):
            letter = tk.Label(self.frame_player1_board, text=i, height=2, width=4)
            letter.grid(row=0, column=num+1)
        for i in range(10):
            number = tk.Label(self.frame_player1_board, text=str(i), height=2, width=4)
            number.grid(row=i+1, column=0)
        for i in range(size):
            for j in range(size):
                self.fields_buttons.append(tk.Button(self.frame_player1_board, text='['+str(i)+' '+str(j)+']', fg="blue", height=1, width=3, command=lambda i=i, j=j: self.add_ship(bs.Ship(i, j, self.ship_direction, self.ship_length))))
                self.fields_buttons[-1].grid(row=i+1, column=j+1)

    def add_ship(self, ship):
        if self.game.player_board.add_ship(ship):
            self.game.player_board.available_ship_list[ship.length-1][1] -= 1
            for x, y in ship.ship_fields:
                self.fields_buttons[x*10+y].configure(background='pink')
            for x, y in ship.ship_overlay_fields_clear:
                self.fields_buttons[x * 10 + y].configure(background='orange')
        if sum([y for x, y in self.game.player_board.available_ship_list]) == 0:
            self.text1.configure(text="Your board is ready! Press Play to start game")
            self.start.configure(text="Play")

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
    app = Application(root)
    app.mainloop()

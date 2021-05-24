import random
import unittest
import tkinter as tk
import time
import battleships as bs
import app as ap


class Test(unittest.TestCase):
    def test1(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test1 - Trying to place ship incorrectly", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.add_ship(bs.Ship(0, 0, bs.Direction.SOUTH, 4))
        root.update()
        time.sleep(1)

        self.assertFalse(app.add_ship(bs.Ship(1, 0, bs.Direction.EAST, 3)))
        root.update()
        time.sleep(1)

        root.destroy()
        root.mainloop()

    def test2(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test2 - Place all ships correctly and start Play", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(2)

        root.destroy()
        root.mainloop()

    def test3(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test3 - Miss enemy board", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        while 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if app._Application__game.ai_board.board[x][y] == "x":
                app.shoot(x, y)
                root.update()
                time.sleep(1)
                break

        root.destroy()
        root.mainloop()

    def test4(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test4 - Hit enemy board", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        while 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if app._Application__game.ai_board.board[x][y] == "1":
                app.shoot(x, y)
                root.update()
                time.sleep(1)
                break

        root.destroy()
        root.mainloop()

    def test5(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test5 - Trying to place ship on player board", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        while 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if app._Application__game.player_board.board[x][y] == "1":
                app.add_ship(bs.Ship(x, y, bs.Direction.SOUTH,
                                     1))  # I execute add_ship command, because on player board there is still that command during the game
                root.update()
                time.sleep(1)
                break

        root.destroy()
        root.mainloop()

    def test6(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test6 - Trying to shot empty field twice", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        while 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if app._Application__game.ai_board.board[x][y] == "x":
                app.shoot(x, y)
                root.update()
                time.sleep(1)

                app.shoot(x, y)
                root.update()
                time.sleep(1)
                break

        root.destroy()
        root.mainloop()

    def test7(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test7 - Trying to shot same ship field twice", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        while 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if app._Application__game.ai_board.board[x][y] == "1":
                app.shoot(x, y)
                root.update()
                time.sleep(1)

                app.shoot(x, y)
                root.update()
                time.sleep(1)
                break

        root.destroy()
        root.mainloop()

    def test8(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test8 - Place some ships and reset board", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.add_ship(bs.Ship(0, 0, bs.Direction.SOUTH, 4))
        root.update()
        time.sleep(1)

        app.add_ship(bs.Ship(5, 0, bs.Direction.EAST, 3))
        root.update()
        time.sleep(1)

        app.add_ship(bs.Ship(5, 5, bs.Direction.EAST, 3))
        root.update()
        time.sleep(1)

        app.reset_action()
        root.update()
        time.sleep(1)

        root.destroy()
        root.mainloop()

    def test9(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test9 - Trying to shot same fields after reset", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        for i in range(0, 9, 2):
            app.shoot(i, i)
            root.update()
            time.sleep(1)

        app.reset_action_ingame()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        for i in range(0, 9, 2):
            app.shoot(i, i)
            root.update()
            time.sleep(1)

        root.destroy()
        root.mainloop()

    def test90(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test10 - Win, then reset without quitting the game", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        while not app._Application__game.ai_board.gameover():
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if app._Application__game.ai_board.board[x][y] in ["1", "2", "3", "0"]:
                app.shoot(x, y)
                root.update()
                time.sleep(1)

        app.reset_action_ingame()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        app.shoot(4, 4)
        root.update()
        time.sleep(1)

        root.destroy()
        root.mainloop()

    def test91(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1300, height=700)
        app = ap.Application(root, canvas)

        text = tk.Label(root, text="Test11 - Lose, then reset without quitting the game", fg="red", width=42, bg='black',
                        font='WarHeliosCondCBold 25 bold')
        canvas.create_window(470, 710, anchor='nw', window=text)

        root.update()
        time.sleep(1)

        app.start_action()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        for x in range(9):
            for y in range(9):
                if app._Application__game.player_board.gameover():
                    break
                if app._Application__game.ai_board.board[x][y] not in ["1", "2", "3", "0"]:
                    app.shoot(x, y)
                    root.update()
                    time.sleep(1)

        app.reset_action_ingame()
        root.update()
        time.sleep(1)

        app.random_board()
        root.update()
        time.sleep(1)

        app.play()
        root.update()
        time.sleep(1)

        app.shoot(4, 4)
        root.update()
        time.sleep(1)

        root.destroy()
        root.mainloop()


if __name__ == "__main__":
    unittest.main()

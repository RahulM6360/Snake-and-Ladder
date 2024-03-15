import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
# import os

class SnakeAndLadderGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake and Ladder Game")

        self.board_size = 10
        self.snakes_and_ladders = {
            16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
            64: 60, 87: 24, 93: 73, 95: 75, 98: 78
        }

        self.load_images()
        # self.load_sounds()
        self.create_widgets()

    def load_images(self):
        self.board_image = Image.open("a-snake-ladder-board-game-vector-23991720.jpg")
        self.board_image = ImageTk.PhotoImage(self.board_image)

        self.snake_image = Image.open("Snakes-and-Ladders-Free-Board-Games-by-IDZ-Digital-Private-Limited-1536x1536.webp")
        self.snake_image = ImageTk.PhotoImage(self.snake_image)

        self.ladder_image = Image.open("OIP.jpg")
        self.ladder_image = ImageTk.PhotoImage(self.ladder_image)

        self.player1_image = Image.open("aps,504x498,small,transparent-pad,600x600,f8f8f8.jpg")
        self.player1_image = ImageTk.PhotoImage(self.player1_image)

        self.player2_image = Image.open("player-2-game-iron-on-decals.jpg")
        self.player2_image = ImageTk.PhotoImage(self.player2_image)

        self.dice_images = [Image.open(f"dice{i}.png") for i in range(1, 7)]
        self.dice_images = [ImageTk.PhotoImage(img) for img in self.dice_images]

    def load_sounds(self):
        # self.dice_sound_path = "dice_roll.wav"
        self.snake_sound_path = "snake_hiss.wav"
        self.ladder_sound_path = "ladder_climb.wav"

    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=700, height=700)
        self.canvas.pack()

        self.canvas.create_image(0, 700, anchor=tk.SW, image=self.board_image)

        self.roll_button = tk.Button(self.master, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        self.current_player = 1
        self.player1_position = 1
        self.player2_position = 1

        self.update_player_positions()

    def roll_dice(self):
        dice_value = random.randint(1, 6)
        # self.play_dice_sound()
        self.update_dice_image(dice_value)
        messagebox.showinfo("Dice Roll", f"Player {self.current_player} rolled a {dice_value}")

        if self.current_player == 1:
            self.move_player(self.player1_position, dice_value)
            self.current_player = 2
        else:
            self.move_player(self.player2_position, dice_value)
            self.current_player = 1

    # def play_dice_sound(self):
    #     os.system(f"start afplay {self.dice_sound_path} &" if os.name == 'posix' else f"start {self.dice_sound_path}")

    def move_player(self, player_position, steps):
        player_position += steps

        if player_position in self.snakes_and_ladders:
            new_position = self.snakes_and_ladders[player_position]
            # self.play_snake_or_ladder_sound()
            messagebox.showinfo("Snake or Ladder", f"Player {self.current_player} found a Snake or Ladder!")
            player_position = new_position

        if player_position > self.board_size**2:
            messagebox.showinfo("Game Over", f"Player {self.current_player} reached the end! Congratulations!")
            self.reset_game()
        else:
            if self.current_player == 1:
                self.player1_position = player_position
            else:
                self.player2_position = player_position

            self.update_player_positions()

    # def play_snake_or_ladder_sound(self):
    #     if self.current_player == 1:
    #         os.system(f"start afplay {self.snake_sound_path} &" if os.name == 'posix' else f"start {self.snake_sound_path}")
    #     else:
    #         os.system(f"start afplay {self.ladder_sound_path} &" if os.name == 'posix' else f"start {self.ladder_sound_path}")

    def update_player_positions(self):
        self.canvas.delete("players")

        row1, col1 = divmod(self.player1_position - 1, self.board_size)
        x1 = col1 * 50+20
        y1 = 700 - row1 * 50-40

        row2, col2 = divmod(self.player2_position - 1, self.board_size)
        x2 = col2 * 50+ 35
        y2 = 700 - row2 * 60 - 30

        self.canvas.create_image(x1, y1, image=self.player1_image, tags="players")
        self.canvas.create_image(x2, y2, image=self.player2_image, tags="players")

    def update_dice_image(self, result):
        self.canvas.delete("dice")
        x = 500
        y = 500
        self.canvas.create_image(x, y, image=self.dice_images[result - 1], tags="dice")

    def reset_game(self):
        self.current_player = 1
        self.player1_position = 1
        self.player2_position = 1
        self.update_player_positions()


if __name__ == "__main__":
    root = tk.Tk() 

    game = SnakeAndLadderGame(root)
    root.mainloop()

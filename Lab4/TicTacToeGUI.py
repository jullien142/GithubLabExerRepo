import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        b = self.board
        wins = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
        for i, j, k in wins:
            if b[i] == b[j] == b[k] != " ":
                return b[i]
        return None

    def is_draw(self):
        return " " not in self.board and self.check_winner() is None

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = TicTacToe()
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_click(self, index):
        if self.game.board[index] == " ":
            self.game.make_move(index)
            self.buttons[index].config(text=self.game.current_player)
            winner = self.game.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif self.game.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.game.switch_player()

    def reset_game(self):
        self.game.reset()
        for button in self.buttons:
            button.config(text=" ")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

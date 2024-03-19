import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = [[tk.Button(self.window, text="", font=("Arial", 20), width=5, height=2,
                                   command=lambda row=row, col=col: self.on_click(row, col))
                         for col in range(3)] for row in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)
    
    def on_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]["text"] = ""

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

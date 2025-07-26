import tkinter as tk
from tkinter import messagebox
from game import TicTacToeGame
from constants import *

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - AI (Minimax)")
        self.game = TicTacToeGame()
        
        # Create buttons
        self.buttons = []
        for i in range(BOARD_SIZE):
            button = tk.Button(
                root, text=EMPTY, font=('Arial', 20), 
                height=2, width=5, command=lambda idx=i: self.on_click(idx)
            )
            button.grid(row=i // GRID_SIZE, column=i % GRID_SIZE)
            self.buttons.append(button)
        
        # Status label
        self.status_label = tk.Label(root, text="Your turn (X)", font=('Arial', 12))
        self.status_label.grid(row=GRID_SIZE, column=0, columnspan=GRID_SIZE)
        
        # Restart button
        restart_btn = tk.Button(root, text="Restart", command=self.reset_game)
        restart_btn.grid(row=GRID_SIZE + 1, column=0, columnspan=GRID_SIZE, sticky="we")

    def on_click(self, position):
        if not self.game.game_over and self.game.current_player == HUMAN and self.game.board[position] == EMPTY:
            self.update_board(position, HUMAN)
            
            if winner := self.game.check_winner(self.game.board):
                self.end_game(winner)
            elif self.game.is_board_full():
                self.end_game(None)
            else:
                self.game.current_player = AI
                self.status_label.config(text="AI is thinking...")
                self.root.after(500, self.ai_turn)  # Delay for better UX

    def ai_turn(self):
        ai_position = self.game.ai_move()
        self.update_board(ai_position, AI)
        
        if winner := self.game.check_winner(self.game.board):
            self.end_game(winner)
        elif self.game.is_board_full():
            self.end_game(None)
        else:
            self.game.current_player = HUMAN
            self.status_label.config(text="Your turn (X)")

    def update_board(self, position, player):
        self.game.board[position] = player
        self.buttons[position].config(text=player, state=tk.DISABLED)

    def end_game(self, winner):
        self.game.game_over = True
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        
        if winner == HUMAN:
            messagebox.showinfo("Game Over", "You win! 🎉")
        elif winner == AI:
            messagebox.showinfo("Game Over", "AI wins! 🤖")
        else:
            messagebox.showinfo("Game Over", "It's a tie! 🏳️")

    def reset_game(self):
        self.game.reset()
        for i in range(BOARD_SIZE):
            self.buttons[i].config(text=EMPTY, state=tk.NORMAL)
        self.status_label.config(text="Your turn (X)")
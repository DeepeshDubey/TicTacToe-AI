from constants import *

class TicTacToeGame:
    def __init__(self):
        self.board = [EMPTY] * BOARD_SIZE
        self.current_player = HUMAN
        self.game_over = False

    def reset(self):
        self.board = [EMPTY] * BOARD_SIZE
        self.current_player = HUMAN
        self.game_over = False

    def check_winner(self, board):
        # Check rows, columns, and diagonals
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != EMPTY:
                return board[line[0]]  # Returns 'X' or 'O'
        return None

    def is_board_full(self):
        return EMPTY not in self.board

    def minimax(self, board, is_maximizing):
        winner = self.check_winner(board)
        if winner == AI:
            return WIN
        elif winner == HUMAN:
            return LOSE
        elif self.is_board_full():
            return DRAW

        if is_maximizing:  # AI's turn (maximize score)
            best_score = -float('inf')
            for i in range(BOARD_SIZE):
                if board[i] == EMPTY:
                    board[i] = AI
                    score = self.minimax(board, False)
                    board[i] = EMPTY
                    best_score = max(score, best_score)
            return best_score
        else:  # Human's turn (minimize score)
            best_score = float('inf')
            for i in range(BOARD_SIZE):
                if board[i] == EMPTY:
                    board[i] = HUMAN
                    score = self.minimax(board, True)
                    board[i] = EMPTY
                    best_score = min(score, best_score)
            return best_score

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(BOARD_SIZE):
            if self.board[i] == EMPTY:
                self.board[i] = AI
                score = self.minimax(self.board, False)
                self.board[i] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move
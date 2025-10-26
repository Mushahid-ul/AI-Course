import tkinter as tk
from tkinter import messagebox


# Constants
PLAYER = "X"
AI = "O"

# Initialize empty board
board = [["" for _ in range(3)] for _ in range(3)]

# Create main window
root = tk.Tk()
root.title("Tic Tac toe")


# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif is_full(board):
        return 0

    
   

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def best_move():

    
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        make_move(move[0], move[1], AI)

# Check for winner
def check_winner(b):
    # Rows, columns, diagonals
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != "":
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != "":
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != "":
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != "":
        return b[0][2]
    return None

def is_full(b):
    for row in b:
        for cell in row:
            if cell == "":
                return False
    return True

# Make a move
def make_move(i, j, player):
    if board[i][j] == "":
        board[i][j] = player
        buttons[i][j]["text"] = player
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
            reset_board()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        elif player == PLAYER:
            root.after(100, best_move)

# Reset board
def reset_board():
    global board
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# Create buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                                  command=lambda i=i, j=j: make_move(i, j, PLAYER))
        buttons[i][j].grid(row=i, column=j)     
root.mainloop()

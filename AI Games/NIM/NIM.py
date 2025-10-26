import tkinter as tk
import math
from functools import partial

# ---------- Minimax Logic ----------
def is_terminal(state):
    return all(pile == 0 for pile in state)

def evaluate(state, maximizing_player):
    return -1 if maximizing_player else 1

def get_children(state):
    children = []
    for i, pile in enumerate(state):
        for remove in range(1, pile + 1):
            new_state = state.copy()
            new_state[i] -= remove
            children.append(new_state)
    return children

def minimax(state, maximizing_player):
    if is_terminal(state):
        return evaluate(state, maximizing_player), None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for child in get_children(state):
            eval, _ = minimax(child, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for child in get_children(state):
            eval, _ = minimax(child, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child
        return min_eval, best_move

# ---------- GUI Logic ----------
class NimGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NIM Game🎮")

        # Starting piles
        self.state = [3, 4, 5,]
        self.player_turn = True

        # Info label
        self.info_label = tk.Label(root, text="Your turn", font=("Helvetica", 14, "bold"))
        self.info_label.pack(pady=10)

        # Frame for piles
        self.pile_frames = []
        self.update_board()

    def update_board(self):
        # Remove old frames
        for frame in self.pile_frames:
            frame.destroy()
        self.pile_frames = []

        # Draw piles
        for i, pile in enumerate(self.state):
            frame = tk.Frame(self.root)
            frame.pack(pady=5)
            self.pile_frames.append(frame)

            label = tk.Label(frame, text=f"Pile {i}: {pile} stones", font=("Helvetica", 12))
            label.pack(side="left", padx=10)

            # Buttons to remove stones
            for r in range(1, pile + 1):
                btn = tk.Button(frame, text=f"-{r}", command=partial(self.player_move, i, r))
                btn.pack(side="left")

    def player_move(self, pile, remove):
        if not self.player_turn:
            return
        if remove <= 0 or remove > self.state[pile]:
            return

        self.state[pile] -= remove
        self.check_winner()

        if not is_terminal(self.state):
            self.player_turn = False
            self.info_label.config(text="AI thinking... ")
            self.root.after(500, self.ai_move)

    def ai_move(self):
        _, best_move = minimax(self.state, True)
        self.state = best_move
        self.update_board()
        self.check_winner()
        self.player_turn = True
        if not is_terminal(self.state):
            self.info_label.config(text="Your turn")

    def check_winner(self):
        self.update_board()
        if is_terminal(self.state):
            if self.player_turn:
                self.info_label.config(text="🎉 You Win!")
            else:
                self.info_label.config(text="🤖 AI Wins!")
            for frame in self.pile_frames:
                for widget in frame.winfo_children():
                    widget.config(state="disabled")

# ---------- Run Game ----------
if __name__ == "__main__":
    root = tk.Tk()
    game = NimGameGUI(root)
    root.geometry("400x300")
    root.mainloop()

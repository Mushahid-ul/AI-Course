import tkinter as tk
from tkinter import messagebox, simpledialog
import chess

# ===================== AI Minimax =====================
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 1000
}

def evaluate_board(board):
    value = 0
    for piece_type, val in piece_values.items():
        value += len(board.pieces(piece_type, chess.WHITE)) * val
        value -= len(board.pieces(piece_type, chess.BLACK)) * val
    return value

def minimax(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

# ===================== GUI PART =====================
SQUARE_SIZE = 60
COLORS = ["#EEEED2", "#769656"]  # light / dark
HIGHLIGHT_MOVE = "#F7D154"       # yellow for legal moves
HIGHLIGHT_CAPTURE = "#E74C3C"    # red for capture squares
CHECK_HIGHLIGHT = "#FF7B7B"      # light red for check signal
CHECKMATE_BLINK_COLOR = "#FF3333"  # strong red blink

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game (Human vs AI)")

        self.canvas = tk.Canvas(root, width=8*SQUARE_SIZE, height=8*SQUARE_SIZE)
        self.canvas.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.restart_button = tk.Button(self.button_frame, text="♻ Restart", command=self.restart_game)
        self.restart_button.grid(row=0, column=0, padx=5)

        self.pause_button = tk.Button(self.button_frame, text="⏸ Pause", command=self.toggle_pause)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.level_button = tk.Button(self.button_frame, text="🎯 Level: Medium", command=self.change_level)
        self.level_button.grid(row=0, column=2, padx=5)

        self.board = chess.Board()
        self.selected_square = None
        self.legal_moves_from_selected = []
        self.paused = False

        self.ai_level = "Medium"
        self.ai_depth = 2

        self.blinking = False
        self.blink_rect_id = None

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    # ============== DRAWING BOARD ==============
    def draw_board(self):
        self.canvas.delete("all")
        check_square_white = None
        check_square_black = None

        # check signals
        if self.board.is_check():
            king_square = self.board.king(self.board.turn)
            if king_square is not None:
                # current turn is in check
                if self.board.turn == chess.WHITE:
                    check_square_white = king_square
                else:
                    check_square_black = king_square

        for row in range(8):
            for col in range(8):
                square = chess.square(col, 7 - row)
                color = COLORS[(row + col) % 2]

                # legal move highlight
                for move in self.legal_moves_from_selected:
                    if move.to_square == square:
                        if self.board.piece_at(square):
                            color = HIGHLIGHT_CAPTURE
                        else:
                            color = HIGHLIGHT_MOVE

                # check highlight
                if square == check_square_white or square == check_square_black:
                    color = CHECK_HIGHLIGHT

                x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

                piece = self.board.piece_at(square)
                if piece:
                    self.canvas.create_text(
                        x1 + SQUARE_SIZE / 2,
                        y1 + SQUARE_SIZE / 2,
                        text=self.get_piece_unicode(piece),
                        font=("Arial", 30)
                    )

    def get_piece_unicode(self, piece):
        symbols = {
            "P": "♙", "N": "♘", "B": "♗", "R": "♖", "Q": "♕", "K": "♔",
            "p": "♟", "n": "♞", "b": "♝", "r": "♜", "q": "♛", "k": "♚"
        }
        return symbols[piece.symbol()]

    # ============== HANDLE CLICK (USER MOVE) ==============
    def on_click(self, event):
        if self.blinking:
            return
        if self.paused or self.board.is_game_over():
            return

        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE
        square = chess.square(col, 7 - row)

        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == chess.WHITE:
                self.selected_square = square
                self.legal_moves_from_selected = [m for m in self.board.legal_moves if m.from_square == square]
        else:
            move = chess.Move(self.selected_square, square)

            # Pawn promotion
            piece = self.board.piece_at(self.selected_square)
            if piece and piece.piece_type == chess.PAWN and chess.square_rank(square) == 7:
                promotion_choice = self.ask_promotion()
                move = chess.Move(self.selected_square, square, promotion=promotion_choice)

            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.legal_moves_from_selected = []
                self.draw_board()
                self.check_game_over_and_signal()
                if not self.board.is_game_over():
                    self.root.after(400, self.ai_move)
            else:
                self.selected_square = None
                self.legal_moves_from_selected = []

        self.draw_board()

    # ============== AI MOVE ==============
    def ai_move(self):
        if self.paused or self.board.is_game_over():
            return

        _, best_move = minimax(self.board, self.ai_depth, False)
        if best_move:
            # handle pawn promotion for AI
            if self.board.piece_type_at(best_move.from_square) == chess.PAWN and chess.square_rank(best_move.to_square) == 0:
                best_move = chess.Move(best_move.from_square, best_move.to_square, promotion=chess.QUEEN)
            self.board.push(best_move)
        self.draw_board()
        self.check_game_over_and_signal()

    # ============== GAME OVER CHECK + SIGNAL ==============
    def check_game_over_and_signal(self):
        if self.board.is_game_over():
            if self.board.is_checkmate():
                # blink signal for checkmated king
                checkmated_color = self.board.turn
                king_square = self.board.king(checkmated_color)
                if king_square is not None:
                    self.signal_checkmate_on_square(king_square)

            result = self.board.result()
            if result == "1-0":
                winner = "White Wins!"
            elif result == "0-1":
                winner = "Black (AI) Wins!"
            else:
                winner = "Draw Game!"
            self.root.after(100, lambda: messagebox.showinfo("Game Over", f"Game Over!\nResult: {winner}"))

    # ============== CHECKMATE BLINKING ==============
    def signal_checkmate_on_square(self, square):
        self.blinking = True
        blink_times = 8
        interval = 300

        file = chess.square_file(square)
        rank = chess.square_rank(square)
        col = file
        row = 7 - rank
        x1, y1 = col * SQUARE_SIZE, row * SQUARE_SIZE
        x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE

        def do_blink(count, show):
            if count <= 0:
                if self.blink_rect_id is not None:
                    self.canvas.delete(self.blink_rect_id)
                    self.blink_rect_id = None
                self.blinking = False
                self.draw_board()
                return
            if show:
                self.blink_rect_id = self.canvas.create_rectangle(
                    x1+2, y1+2, x2-2, y2-2, fill=CHECKMATE_BLINK_COLOR, outline=""
                )
            else:
                if self.blink_rect_id is not None:
                    self.canvas.delete(self.blink_rect_id)
                    self.blink_rect_id = None
            self.root.after(interval, lambda: do_blink(count-1, not show))

        do_blink(blink_times, True)

    # ============== PROMOTION ==============
    def ask_promotion(self):
        choice = simpledialog.askstring("Promotion", "Choose piece: Q/R/B/N (default Q)")
        if not choice:
            return chess.QUEEN
        choice = choice.strip().upper()
        return {
            "Q": chess.QUEEN,
            "R": chess.ROOK,
            "B": chess.BISHOP,
            "N": chess.KNIGHT
        }.get(choice, chess.QUEEN)

    def restart_game(self):
        if self.blinking:
            return
        self.board.reset()
        self.selected_square = None
        self.legal_moves_from_selected = []
        self.paused = False
        self.pause_button.config(text="⏸ Pause")
        self.draw_board()

    def toggle_pause(self):
        if self.blinking:
            return
        self.paused = not self.paused
        self.pause_button.config(text="▶️ Resume" if self.paused else "⏸ Pause")

    def change_level(self):
        if self.ai_level == "Easy":
            self.ai_level = "Medium"
            self.ai_depth = 2
        elif self.ai_level == "Medium":
            self.ai_level = "Hard"
            self.ai_depth = 3
        else:
            self.ai_level = "Easy"
            self.ai_depth = 1
        self.level_button.config(text=f"🎯 Level: {self.ai_level}")

# ===================== MAIN =====================
if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    root.mainloop()
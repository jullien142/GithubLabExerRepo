class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print("|".join(row))
            print("-" * 5)

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


def play_cli():
    game = TicTacToe()
    while True:
        game.print_board()
        try:
            move = int(input(f"Player {game.current_player}, enter your move (0-8): "))
            if move < 0 or move > 8:
                print("Invalid input. Enter a number between 0 and 8.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not game.make_move(move):
            print("Cell already taken. Try again.")
            continue

        winner = game.check_winner()
        if winner:
            game.print_board()
            print(f"Player {winner} wins!")
            break
        elif game.is_draw():
            game.print_board()
            print("It's a draw!")
            break
        else:
            game.switch_player()


if __name__ == "__main__":
    play_cli()

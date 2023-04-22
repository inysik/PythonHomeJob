from operation import *

class Controller:
    def __init__(self):
        self.board = init_board()

    def get_board(self):
        return self.board

    def make_move(self, row, col, player):
        if is_valid_move(self.board, row, col):
            make_move(self.board, row, col, player)
            return True
        return False

    def get_winner(self):
        return get_winner(self.board)

    def is_board_full(self):
        return is_board_full(self.board)

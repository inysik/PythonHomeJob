def init_board():
    return [[-1 for j in range(3)] for i in range(3)]

def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != -1:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != -1:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != -1:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != -1:
        return board[2][0]

    return -1

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                return False
    return True

def is_valid_move(board, row, col):
    if board[row][col] == -1:
        return True
    return False

def make_move(board, row, col, player):
    board[row][col] = player

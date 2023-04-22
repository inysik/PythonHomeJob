import pygame
from controller import *
from logger import *

def draw_board(screen, board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                pygame.draw.circle(screen, (255, 255, 255), (j * 200 + 100, i * 200 + 100), 80, 10)
            elif board[i][j] == 1:
                pygame.draw.line(screen, (255, 255, 255), (j * 200 + 55, i * 200 + 55), (j * 200 + 145, i * 200 + 145), 10)
                pygame.draw.line(screen, (255, 255, 255), (j * 200 + 145, i * 200 + 55), (j * 200 + 55, i * 200 + 145), 10)

def main():
    controller = Controller()
    player = 0

    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic Tac Toe")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player == 0:
                    row = int(event.pos[1] // 200)
                    col = int(event.pos[0] // 200)
                    if controller.make_move(row, col, player):
                        player = 1
                elif player == 1:
                    row = int(event.pos[1] // 200)
                    col = int(event.pos[0] // 200)
                    if controller.make_move(row, col, player):
                        player = 0

        screen.fill((0, 0, 0))
        draw_board(screen, controller.get_board())
        pygame.display.flip()

        winner = controller.get_winner()
        if winner != -1:
            log("Player " + str(winner) + " wins!")
            running = False

        if controller.is_board
        if controller.is_board_full():
            log("It's a tie!")
            running = False

    pygame.quit()

if __name__ == '__main__':
    main()

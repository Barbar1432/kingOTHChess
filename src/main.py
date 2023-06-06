import time
import multiprocessing as mp
import pygame
from board import board
from visuals import drag_n_drop_visual, background
from aibot import bot
from timer import timer, visualizeTimers
from tests import FENtoBoard
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def screen():
    global deneme_screen
    deneme_screen = pygame.display.set_mode((1024,712))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    board = board()
    """boardd, color, kingWhite, kingBlack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, \
    (enPassentSquareRow, enPassentSquareCol), halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard(
    "1n1qkbnr/2pppppp/p7/p2P4/6Q1/8/PPPP1PPP/R1B1K1NR b KQk - 0 6")
    board.board = boardd"""
    pygame.init()
    pygame.font.init()
    screen()
    pygame.display.set_caption("King of the Hill")
    clock = pygame.time.Clock()
    running = True
    visuals = drag_n_drop_visual()
    player_turn = 1  # 1 == WHITE PLAYING ||  -1 == BLACK PLAYING
    processChecker = 1  # 1 == Can start processing || -1 Can not start
    wtimer = timer()
    btimer = timer()

    dummy = bot(True, 'black')  # Welcome to life dummy
    board.botplaying = (dummy.ai_bool, dummy.color)
    event_type = 0
    board.positions()
    while running:
        # Bot playing
        if dummy.ai_bool and processChecker == 1:
            if dummy.color == 'black' and board.Anzahlmoves % 2 == 1:
                dummy.random_move(dummy.ai_bool, board)
            elif dummy.color == 'white' and board.Anzahlmoves % 2 == 0:
                dummy.random_move(dummy.ai_bool, board)
        # Player playing
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            # ONLY ALLOW CLICKS INSIDE THE PLAYING AREA
            if (board.dislocation_count_col <= x <= 512 + board.dislocation_count_col) \
                    and (board.dislocation_count_row <= y <= 512 + board.dislocation_count_row):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and len(visuals.sec) == 0:
                    event_type = 1
                    visuals.visualize(event_type, board, deneme_screen)
                    event_type = -1
                if event.type == pygame.MOUSEBUTTONUP and len(visuals.sec) == 1:
                    event_type = 0
                    visuals.visualize(event_type, board, deneme_screen)
                    event_type = -1
            if event.type == pygame.QUIT:
                running = False
        background(deneme_screen, board)
        visualizeTimers(deneme_screen, wtimer, btimer, board)
        visuals.visualize(event_type, board, deneme_screen)
        pygame.display.flip()
        clock.tick(60)




    pygame.quit()

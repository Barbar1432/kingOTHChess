import time

import pygame
from board import board
from visuals import drag_n_drop_visual, background, timer_white, timer_black, timer
from aibot import bot
from tests import FENtoBoard
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
 board = board()
 #boardd, color, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
 #enPassentSquareRow, enPassentSquareCol), \
 #   halfMoveClock, fullMoveClock = FENtoBoard("8/2p2R2/1p2p1Np/1P5k/3nr3/8/P7/2K5 w - - 0 34")
 #board.board = boardd
pygame.init()
pygame.font.init()
deneme_screen = pygame.display.set_mode((1024,712))
pygame.display.set_caption("King of the Hill")
clock = pygame.time.Clock()
running = True
visuals = drag_n_drop_visual()
player_turn = 1  # 1 == WHITE PLAYING ||  -1 == BLACK PLAYING

wtimer = timer()
btimer = timer()
btimer.turn = False

dummy = bot() # Welcome to life dummy
dummy.ai_bool = True # Decide if you want to play against a bot
dummy.color = 'black'  # Decide bots color

event_type = 0
board.positions()
while running:
    if dummy.ai_bool and board.Anzahlmoves % 2 == 1:
        dummy.random_move(dummy.ai_bool, board)

    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        # ONLY ALLOW CLICKS INSIDE THE PLAYING AREA
        if (board.dislocation_count_col <= x <= 512 + board.dislocation_count_col) \
                and (board.dislocation_count_row <= y <= 512 + board.dislocation_count_row):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and len(visuals.sec) == 0:
                event_type = 1
                visuals.visualize(event_type, board)
                event_type = -1
            if event.type == pygame.MOUSEBUTTONUP and len(visuals.sec) == 1:
                event_type = 0
                # TODO: TEST IF THIS IS POSSIBLE MOVE IF NOT - NOT ALLOWED TO MOVE, RETURN BACK TO OLD POS
                # TODO: Change the value of player_turn when one of the opponent makes the move
                visuals.visualize(event_type, board)
                event_type = -1
        if event.type == pygame.QUIT:
            running = False
    background(deneme_screen, board)
    timer_white(deneme_screen, wtimer, board)
    if board.Anzahlmoves % 2 == 0:  # DECREASE WHITE PLAYERS TIME WHILE PLAYING
        wtimer.time -= 1
    timer_black(deneme_screen, btimer, board)
    if board.Anzahlmoves % 2 == 1:   # DECREASE BLACK PLAYERS TIME WHILE PLAYING
        btimer.time -= 1
    visuals.visualize(event_type, board)
    pygame.display.flip()
    clock.tick(60)




pygame.quit()

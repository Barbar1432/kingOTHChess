import time

import pygame
from board import board
from visuals import drag_n_drop_visual, background, timer_white, timer_black, timer
from aibot import bot
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
 board = board()
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
dummy.ai_bool = False # Decide if you want to play against a bot
dummy.color = 'black' # Decide bots color

event_type = 0
board.positions() #KALDIR
while running:
    if player_turn == -1 and dummy.ai_bool:
        dummy.random_move(dummy.ai_bool, board)
        player_turn *= -1
        btimer.turn = not btimer.turn
        wtimer.turn = not wtimer.turn


    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        # ONLY ALLOW CLICKS INSIDE THE PLAYING AREA
        if (board.dislocation_count_col <= x <= 512 + board.dislocation_count_col) \
                and (board.dislocation_count_row <= y <= 512 + board.dislocation_count_row):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and len(visuals.sec) == 0:
                event_type = 1
                # TODO: TEST IF WE ARE THE PLAYING PLAYER, IF NOT - NOT ALLOWED TO CLICK OR MOVE
                # TODO: TEST IF WE ARE TRYING TO MOVE OUR COLORED PIECE, IF NOT - NOT ALLOWED TO CLICK OR MOVE
                visuals.visualize(event_type, board)
                event_type = -1
            if event.type == pygame.MOUSEBUTTONUP and len(visuals.sec) == 1:
                event_type = 0
                # TODO: TEST IF THIS IS POSSIBLE MOVE IF NOT - NOT ALLOWED TO MOVE, RETURN BACK TO OLD POS
                # TODO: Change the value of player_turn when one of the opponent makes the move

                visuals.visualize(event_type, board)
                player_turn *= -1
                btimer.turn = not btimer.turn
                wtimer.turn = not wtimer.turn
                event_type = -1
        if event.type == pygame.QUIT:
            running = False
    background(deneme_screen, board)
    timer_white(deneme_screen, wtimer)
    if wtimer.turn:  # DECREASE WHITE PLAYERS TIME WHILE PLAYING
        wtimer.time -= 1
    timer_black(deneme_screen, btimer)
    if btimer.turn:   # DECREASE BLACK PLAYERS TIME WHILE PLAYING
        btimer.time -= 1
    visuals.visualize(event_type, board)
    pygame.display.flip()
    clock.tick(60)




pygame.quit()

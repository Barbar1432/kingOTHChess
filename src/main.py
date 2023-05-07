
import pygame
from board import board
from visuals import drag_n_drop_visual
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
 board = board()
pygame.init()
pygame.display.set_caption("King of the Hill")
clock = pygame.time.Clock()
running = True
visuals = drag_n_drop_visual()
event_type = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and len(visuals.sec) == 0: # Left Click is pushed
            event_type = 1
            visuals.visualize(event_type, board)
            event_type = 0
        if event.type == pygame.MOUSEBUTTONUP and len(visuals.sec) == 1:
            event_type = -1
            visuals.visualize(event_type, board)
            event_type = 0
        if event.type == pygame.QUIT:
            running = False
    visuals.visualize(event_type, board)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

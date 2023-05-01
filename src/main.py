import pygame
from board import board
#deneme branch

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
sqSelected=()
sec=[]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row,col = mouse_pos
            row= row//board.square_size
            col=col//board.square_size
            sqSelected= (col,row)
            sec.append(sqSelected)

        if (len(sec)==2):
            board.move(sec[0],sec[1])
            board.draw()
            sec = []
    board.draw()






    clock.tick(60)

pygame.quit()

import pygame
from board import board

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
draggedPieceCoordinates = ()  # Clicked Piece
clicked = False
clickedName = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left Click is pushed
            # print("Clicked")
            mouse_pos = pygame.mouse.get_pos()
            row, col = mouse_pos
            draggedPieceCoordinates = (col, row)
            row = row//board.square_size
            col = col//board.square_size
            if len(sec) == 0 and board.board[col][row] is not None:  # If the clicked tile is not empty:
                sqSelected = (col, row)
                sec.append(sqSelected)
                clicked = True
                clickedName = board.board[col][row].name
        if event.type == pygame.MOUSEBUTTONUP and len(sec) == 1:
            # print("Stopped Clicking")
            # len(sec) == 1 : If a piece was not already clicked, do nothing
            row, col = pygame.mouse.get_pos()
            dest_row = row//board.square_size
            dest_col = col//board.square_size
            sqSelected = (dest_col, dest_row)
            sec.append(sqSelected)
            clicked = False
        if len(sec) == 2:
            board.move(sec[0], sec[1])
            board.draw(clicked, draggedPieceCoordinates, clickedName)
            sec = []
        if event.type == pygame.QUIT:
            running = False
    row, col = pygame.mouse.get_pos()
    draggedPieceCoordinates = (col, row)
    board.draw(clicked, draggedPieceCoordinates, clickedName)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

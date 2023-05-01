import pygame
from board import board, get_piece

#branch deneme 6
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
new_cursor = None  # Clicked Piece
while running:
    if new_cursor is not None:
        cursor_position = pygame.mouse.get_pos()
        board.screen.blit(new_cursor, cursor_position)
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row,col = mouse_pos
            row= row//board.square_size
            col=col//board.square_size
            sqSelected= (col,row)
            if board.board[col][row] is not None:  # If the clicked tile is not empty:
                print(board.board[col][row].name)
                new_cursor = pygame.image.load('images/'+ board.board[col][row].name +'.png').convert_alpha()
                new_cursor = pygame.transform.scale(new_cursor,(40,40))
            if not (len(sec) == 0 and board.board[col][row] is None):  # can't move an empty tile
                sec.append(sqSelected)
        if (len(sec)==2):
            board.move(sec[0],sec[1])
            board.draw()
            sec = []
            new_cursor = None
    board.draw()






    clock.tick(60)

pygame.quit()
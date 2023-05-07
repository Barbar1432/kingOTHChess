import pygame
from board import board
class drag_n_drop_visual:
    def __init__(self):
        self.sec = []
        self.dragged = ()
        self.clicked = False
        self.clickedName = None
        self.clickedPos = ()

    def visualize(self, event_type, b_board):
        if event_type == 1:  # MOUSEBUTTONDOWN equals 1
            mouse_pos = pygame.mouse.get_pos()
            row, col = mouse_pos
            self.dragged = (col, row)
            row = row // b_board.square_size
            col = col // b_board.square_size
            if b_board.board[col][row] is not None:
                sq_selected = (col, row)
                self.sec.append(sq_selected)
                self.clicked = True
                self.clickedName = b_board.board[col][row].name
                self.clickedPos = (col, row)
                print("Got here!")
        if event_type == -1:  # MOUSEBUTTONUP equals -1
            mouse_pos = pygame.mouse.get_pos()
            row, col = mouse_pos
            row = row // b_board.square_size
            col = col // b_board.square_size
            if len(self.sec) == 1:
                dest_selected = (col, row)
                self.sec.append(dest_selected)
                self.clicked = False
        if len(self.sec) == 2:
            b_board.move(self.sec[0], self.sec[1])
            b_board.draw(self.clicked, self.dragged, self.clickedName, self.clickedPos)
            self.sec = []
            self.clickedPos = ()
        row, col = pygame.mouse.get_pos()
        self.dragged = (col, row)
        b_board.draw(self.clicked, self.dragged, self.clickedName, self.clickedPos)


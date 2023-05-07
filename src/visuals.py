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
            col, row = mouse_pos
            print("Coordinates: ", row, ",", col)
            self.dragged = (row - b_board.dislocation_count_row, col - b_board.dislocation_count_col)
            row = (row - b_board.dislocation_count_row)// b_board.square_size
            col = (col - b_board.dislocation_count_col)// b_board.square_size
            if b_board.board[row][col] is not None:
                sq_selected = (row, col)
                self.sec.append(sq_selected)
                self.clicked = True
                self.clickedName = b_board.board[row][col].name
                self.clickedPos = (row, col)
                print("Just Clicked:"+ self.clickedName + "!")
                print("Coordinates: ", row, ",", col)
        if event_type == 0:  # MOUSEBUTTONUP equals 0
            mouse_pos = pygame.mouse.get_pos()
            col, row = mouse_pos
            row = (row - b_board.dislocation_count_row)// b_board.square_size
            col = (col - b_board.dislocation_count_col)// b_board.square_size
            if len(self.sec) == 1:
                dest_selected = (row, col)
                self.sec.append(dest_selected)
                self.clicked = False
        if len(self.sec) == 2:
            b_board.move(self.sec[0], self.sec[1])
            b_board.draw(self.clicked, self.dragged, self.clickedName, self.clickedPos)
            self.sec = []
            self.clickedPos = ()
        col, row = pygame.mouse.get_pos()
        self.dragged = (row - b_board.dislocation_count_row, col - b_board.dislocation_count_col)
        b_board.draw(self.clicked, self.dragged, self.clickedName, self.clickedPos)
def background(screen, b_board):
    background_color = (241, 222, 201)
    outline_color = (141, 123, 104)
    outline_color2 = (164, 144, 124)
    screen.fill(background_color)
    pygame.draw.rect(screen, outline_color,
                     pygame.Rect(b_board.dislocation_count_col - 20,
                                 b_board.dislocation_count_row - 20,
                                 552, 552))
    pygame.draw.rect(screen, outline_color2,
                     pygame.Rect(b_board.dislocation_count_col - 10,
                                 b_board.dislocation_count_row - 10,
                                 532, 532))




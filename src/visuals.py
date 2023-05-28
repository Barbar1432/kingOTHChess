import string
from colors import get_color
import pygame
from board import board
from piece import Rook, Knight, Bishop, Queen, King, Pawn
class drag_n_drop_visual:
    def __init__(self):
        self.sec = []
        #self.dragged = () # removed
        self.clicked = False
        self.clickedName = None
        self.clickedPos = ()

    def visualize(self, event_type, b_board):
        if event_type == 1:  # MOUSEBUTTONDOWN equals 1
            mouse_pos = pygame.mouse.get_pos()
            col, row = mouse_pos
            print("Coordinates: ", row, ",", col)
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
            b_board.moveZa(self.sec[0], self.sec[1])
            b_board.draw(self.clicked, self.clickedName, self.clickedPos)
            self.sec = []
            self.clickedPos = ()
        b_board.draw(self.clicked, self.clickedName, self.clickedPos)


def background(screen, b_board):
    dist_between = 3
    dislocator = 3
    font = pygame.font.SysFont("fonts/PokemonGB.ttf", 25)
    screen.fill(get_color("background"))
    # ------ Main Board Frame ------- #
    pygame.draw.rect(screen, get_color("outline1"),
                     pygame.Rect(b_board.dislocation_count_col - 30,
                                 b_board.dislocation_count_row - 30,
                                 572, 572))
    pygame.draw.rect(screen, get_color("outline2"),
                     pygame.Rect(b_board.dislocation_count_col - 15,
                                 b_board.dislocation_count_row - 15,
                                 542, 542))
    # ------ Timer Frame Black ------- #
    pygame.draw.rect(screen, get_color("outline1"),
                     pygame.Rect(b_board.dislocation_count_col, b_board.dislocation_count_row - 70 , 512, 50))
    pygame.draw.rect(screen, get_color("outline2"),
                     pygame.Rect(b_board.dislocation_count_col + 15 , b_board.dislocation_count_row - 55, 512 - 30, 35))
    # ------ Timer Frame White ------- #
    pygame.draw.rect(screen, get_color("outline1"),
                     pygame.Rect(b_board.dislocation_count_col, b_board.dislocation_count_row + b_board.square_size * 8 + 20,
                                 512, 50))
    pygame.draw.rect(screen, get_color("outline2"),
                     pygame.Rect(b_board.dislocation_count_col + 15, b_board.dislocation_count_row + b_board.square_size * 8 + 20,
                                 512 - 30, 35))

    # Print a - b - c
    abc_surface = font.render("a           b           c           d           "
                              "e           f           g           h", False, get_color("text"))
    screen.blit(abc_surface, (b_board.dislocation_count_col + dist_between, b_board.dislocation_count_row + b_board.square_size * 8))

    # Print 1 - 2 - 3 --> Lack of '\n' printing with for loop
    for i in range(8,0,-1):
        number = i
        number_surface = font.render(str(number), False, get_color("text"))
        screen.blit(number_surface, (b_board.dislocation_count_col + b_board.square_size * 8 + dislocator,
                                     b_board.dislocation_count_row + dist_between + (8-i) * b_board.square_size))
    # ------ Player Frame ------- #
    pygame.draw.rect(screen, get_color("outline1"),
                     pygame.Rect(b_board.dislocation_count_col + b_board.square_size * 8 + 30,
                                 b_board.dislocation_count_row + b_board.square_size - 40,
                                 4 * b_board.square_size, 4 * b_board.square_size))
    pygame.draw.rect(screen, get_color("outline2"),
                     pygame.Rect(b_board.dislocation_count_col + b_board.square_size * 8 + 23,
                                 b_board.dislocation_count_row + b_board.square_size - 30,
                                 4 * b_board.square_size - 2, 4 * b_board.square_size - 20))
    # ------ Points Frame ------- #
    pygame.draw.rect(screen, get_color("outline1"),
                     pygame.Rect(b_board.dislocation_count_col + b_board.square_size * 8 + 30,
                                 b_board.dislocation_count_row + b_board.square_size - 40 + 4 * b_board.square_size - 10,
                                 4 * b_board.square_size, 2 * b_board.square_size + 32))
    pygame.draw.rect(screen, get_color("outline2"),
                     pygame.Rect(b_board.dislocation_count_col + b_board.square_size * 8 + 23,
                                 b_board.dislocation_count_row + b_board.square_size - 30 + 4 * b_board.square_size - 10,
                                 4 * b_board.square_size - 2, 2 * b_board.square_size + 12))
    pygame.draw.rect(screen, get_color("outline1"),
                     pygame.Rect(b_board.dislocation_count_col + b_board.square_size * 8 + 2 * b_board.square_size + 17,
                                b_board.dislocation_count_row + b_board.square_size - 30 + 4 * b_board.square_size - 10,
                                 10, 2 * b_board.square_size + 16))


def timer_black(screen, timer_b, board):
    font = pygame.font.Font("fonts/PublicPixel.ttf", 15)
    # milliseconds = timer.time % 60
    seconds = (int(timer_b.time / 60)) % 60
    minutes = int(timer_b.time / 3600)
    if board.Anzahlmoves % 2 == 1:
        # Light this when turn == player
        pygame.draw.rect(screen, get_color("background"),
                         pygame.Rect(128 + 15,
                                     100 - 55,
                                     512 - 30, 35))
    text_surface = font.render("Player Black  ", False, get_color("text"))
    screen.blit(text_surface, (155, 55))
    timer_surface = font.render(f"00:{minutes:02}:{seconds:02}", False, get_color("text"))
    screen.blit(timer_surface, (355, 55))


def timer_white(screen, timer_w, board):
    font = pygame.font.Font("fonts/PublicPixel.ttf", 15)
    # milliseconds = timer.time % 60
    seconds = (int(timer_w.time / 60)) % 60
    minutes = int(timer_w.time / 3600)
    if board.Anzahlmoves % 2 == 0:
        # Light this when turn == player
        pygame.draw.rect(screen, get_color("background"),
                         pygame.Rect(128 + 15,
                                     100 + 64 * 8 + 20,
                                     512 - 30, 35))
    text_surface = font.render("Player White  ", False, get_color("text"))
    screen.blit(text_surface, (155, 128 + 64 * 8))
    timer_surface = font.render(f"00:{minutes:02}:{seconds:02}", False, get_color("text"))
    screen.blit(timer_surface, (355, 128 + 64 * 8))
class timer:
    def __init__(self):
        self.time = 72000  # 20 Minutes

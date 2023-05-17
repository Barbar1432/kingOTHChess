import string

import pygame
from board import board
from piece import Rook, Knight, Bishop, Queen, King, Pawn
def get_color(color):
    if color == "background":
        return (241, 222, 201)
    elif color == "outline1":
        return (141, 123, 104)
    elif color == "outline2":
        return (164, 144, 124)
    elif color == "text":
        return (121, 102, 81)
    else:
        return
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
            b_board.move(self.sec[0], self.sec[1])
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


def timer_black(screen, timer_b):
    font = pygame.font.Font("fonts/PublicPixel.ttf", 15)
    # milliseconds = timer.time % 60
    seconds = (int(timer_b.time / 60)) % 60
    minutes = int(timer_b.time / 3600)
    if timer_b.turn:
        # Light this when turn == player
        pygame.draw.rect(screen, get_color("background"),
                         pygame.Rect(128 + 15,
                                     100 - 55,
                                     512 - 30, 35))
    text_surface = font.render("Player Black  ", False, get_color("text"))
    screen.blit(text_surface, (155, 55))
    timer_surface = font.render(f"00:{minutes:02}:{seconds:02}", False, get_color("text"))
    screen.blit(timer_surface, (355, 55))


def timer_white(screen, timer_w):
    font = pygame.font.Font("fonts/PublicPixel.ttf", 15)
    # milliseconds = timer.time % 60
    seconds = (int(timer_w.time / 60)) % 60
    minutes = int(timer_w.time / 3600)
    if timer_w.turn:
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
        self.turn = True

#def FENtoBoard(FEN):
#    board = [[None for _ in range(8)] for _ in range(8)]
#    i = 0
#    j = 0
#    color = 'non-colored'
#    while FEN != "":
#        char = FEN[0]
#        FEN = ''.join(FEN.split(char, 1))
#        if char == '/':
#            i += 1
#            j = 0
#        elif char == 'p':
#            board[i][j] = Pawn('black',"sPion")
#            j += 1
#        elif char == 'n':
#            board[i][j] = Knight('black',"sAt")
#            j += 1
#        elif char == 'b':
#            board[i][j] = (Bishop('black',"sFil"))
#            j += 1
#        elif char == 'r':
#            board[i][j] = (Rook('black',"sK"))
#            j += 1
#        elif char == 'q':
#            board[i][j] = (Queen('black',"sV"))
#            j += 1
#        elif char == 'k':
#            board[i][j] = (King('black', "sSah"))
#            j += 1
#        elif char == 'N':
#            board[i][j] = (Knight('white', "bAt"))
#            j += 1
#        elif char == 'B':
#            board[i][j] = (Bishop('white', "bFil"))
#            j += 1
#        elif char == 'R':
#            board[i][j] = (Rook('white', "bK"))
#            j += 1
#        elif char == 'Q':
#            board[i][j] = (Queen('white', "bV"))
#            j += 1
#        elif char == 'K':
#            board[i][j] = (King('white', "bSah"))
#            j += 1
#        elif char == 'P':
#            board[i][j] = (Pawn('white', "bPion"))
#            j += 1
#        elif char.isdigit():
#            j += int(char)
#        elif char == ' ':
#            char = FEN[0]
#            FEN = ''.join(FEN.split(char, 1))
#            if char == 'w':
#                color = 'white'
#            elif char == 'b':
#                color = 'black'
#            print("Kalan FEN:", FEN)
#            FEN = ""
#        else:
#            print("There is a problem!", char)
#            # Board is done
#    return board, color

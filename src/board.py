import pygame
import pygame.gfxdraw
from piece import piece
from piece import Rook, Knight, Bishop, Queen, King,Pawn
class board :
    def __init__(self):
         self.Anzahlmoves = 0
         self.whiteKing =King('white', "bSah")
         self.blackKing = King('black', "sSah")

         self.board = [
            [Rook('black',"sK"), Knight('black',"sAt"), Bishop('black',"sFil"), Queen('black',"sV"), King('black',"sSah"), Bishop('black',"sFil"),
             Knight('black',"sAt"), Rook('black',"sK")],
            [Pawn('black',"sPion") for _ in range(8)],
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [Pawn('white',"bPion") for _ in range(8)],
            [Rook('white', "bK"), Knight('white', "bAt"), Bishop('white', "bFil"), Queen('white',"bV"),
             King('white',"bSah"), Bishop('white',"bFil"),
             Knight('white', "bAt"), Rook('white', "bK")] ]
         self.square_size = 64
         self.screen_size = (self.square_size * 8, self.square_size * 8)
         self.screen = pygame.display.set_mode(self.screen_size)
         self.dislocation_count_row = 100  # Dikey
         self.dislocation_count_col = 128  # Yatay

    def draw_board(self, booly, name, clickedpos):
         colors = [(255, 206, 158), (209, 139, 71)]

         for row in range(8):
             for col in range(8):

                 color = colors[(row + col) % 2]
                 rect = pygame.Rect(col * self.square_size + self.dislocation_count_col, row * self.square_size + self.dislocation_count_row, self.square_size, self.square_size)
                 pygame.draw.rect(self.screen, color, rect)
                 if self.board[row][col] != None:  # Print the piece on the board
                     piece_image = pygame.image.load('images/' + self.board[row][col].name + '.png')
                     piece_image = pygame.transform.scale(piece_image, (self.square_size, self.square_size))
                     self.screen.blit(piece_image, rect)
         #DRAW THE HILL SHADOW
         trans_color = (129, 133, 137, 50)
         #UP
         pygame.gfxdraw.box(self.screen, pygame.Rect(3 * self.square_size - 10 + self.dislocation_count_col,
                                                     3 * self.square_size - 10 + self.dislocation_count_row,
                                                     2 * self.square_size + 20, 10), trans_color)
         #DOWN
         pygame.gfxdraw.box(self.screen, pygame.Rect(3 * self.square_size - 10 + self.dislocation_count_col,
                                                     5 * self.square_size + self.dislocation_count_row,
                                                     2 * self.square_size + 20, 10), trans_color)
         #LEFT
         pygame.gfxdraw.box(self.screen, pygame.Rect(3 * self.square_size - 10 + self.dislocation_count_col,
                                                     3 * self.square_size + self.dislocation_count_row,
                                                     10, 2 * self.square_size), trans_color)
         #RIGHT
         pygame.gfxdraw.box(self.screen, pygame.Rect(5 * self.square_size + self.dislocation_count_col,
                                                     3 * self.square_size + self.dislocation_count_row,
                                                     10, 2 * self.square_size), trans_color)
         if booly: # Drag and drop booly

             clicked_image = pygame.image.load('images/' + name + '.png')
             (row,col) = clickedpos
             transparent_screen = pygame.Surface((self.square_size, self.square_size))
             transparent_screen.set_alpha(120)
             transparent_screen.fill((144, 238, 144))
             pos1, pos2 = pygame.mouse.get_pos()
             pos1 = pos1 - self.dislocation_count_row
             pos2 = pos2 - self.dislocation_count_col
            # Clicked tile lit green
             self.screen.blit(transparent_screen, (col * self.square_size + self.dislocation_count_col, row * self.square_size + self.dislocation_count_row))
             self.screen.blit(clicked_image, (pos1-30 + self.dislocation_count_row, pos2-30 + self.dislocation_count_col))


    def draw(self, booly, name, clickedpos):
        self.draw_board(booly, name, clickedpos)
        pygame.display.flip()


    def move(self, sqSelected, sqDest):

        row, col = sqSelected
        piece = self.board[row][col]
        if self.board[row][col]!= None:
             piece.clear_list()
        if isinstance(piece,Pawn):
            piece.possible_moves_pawn(self.board)
        elif isinstance(piece,King):
            piece.possible_moves_king(self.board)
        elif isinstance(piece, Knight):
            piece.possible_moves_knight(self.board)
        elif isinstance(piece, Bishop):
            piece.possible_moves_bishop(self.board)
        elif isinstance(piece, Rook):
            piece.possible_moves_rook(self.board)
        elif isinstance(piece, Queen):
            piece.possible_moves_queen(self.board)



        print(self.board[row][col].possible_moves_list)

        row_dest, col_dest = sqDest
        if self.isLegal(sqSelected,sqDest): #(row_dest, col_dest) in self.board[row][col].possible_moves_list and
            self.board[row][col] = None
            self.board[row_dest][col_dest] = piece
            piece.position = (row_dest, col_dest)
        self.Anzahlmoves += 1
        print(self.bewertungsFunktion())


    def positions(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if (self.board[row][column] != None):
                    self.board[row][column].position = (row, column)

    def get_Kingsposition(self, king):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] == king:
                    return (row, column)



    def is_king_checked(self, king): #gpt
        kingPos = self.get_Kingsposition(king)
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] is None:
                    continue
                if king.color == self.board[row][column].color:
                    continue
                if king in self.board[row][column].possible_moves_list:
                    return True
        return False

    def isLegal(self, start_pos, dest_pos):
        start_row, start_col = start_pos
        dest_row, dest_col = dest_pos
        start = self.board[start_row][start_col] # start is a piece

        dest = self.board[dest_row][dest_col] # dest can either be a square (None) or a piece
        if self.Anzahlmoves % 2 == 0:
            if start is not None:
                if start.color == "black":
                    return False
        if self.Anzahlmoves % 2 == 1:
            if start is not None:
                if start.color == "white":
                    return False
        if start is None : # look if there actually is a piece on the start square
            return False
        if not start.possible_moves_list.__contains__(dest_pos) : # look if the destination is a possible move for the piece
            return False
        if start.possible_moves_list.__contains__(dest_pos) and dest !=None:
            if dest.color == start.color:
                return False
        else :
            return True

    def bewertungsFunktion(self):
        whiteCurrentPieces = []
        blackCurrentPieces = []
        whitePoints = 0
        blackPoints = 0
        center = [self.board[3][4], self.board[4][4], self.board[3][3], self.board[4][3]]
        aroundCenter =[self.board[2][3], self.board[2][4], self.board[3][2], self.board[3][5],self.board[4][2], self.board[4][5], self.board[5][3], self.board[5][4]]
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                piece = self.board[row][column]
                if (piece is not None):
                   if piece.color == "white":
                      whiteCurrentPieces.append(piece)
                      whitePoints += piece.point
                   if piece.color == "black":
                       blackCurrentPieces.append(piece)
                       blackPoints += piece.point
        for piece in center:
            if piece is not None:
               if piece.color == "white":
                   whitePoints += 1
               if piece.color == "black":
                   blackPoints += 1
        for piece in aroundCenter:
            if piece is not None:
               if piece.name == "bSah":
                   whitePoints += 2.2
               if piece.color == "s.sah":
                   blackPoints += 2.2

        bewertung = (whitePoints - blackPoints)*0.10
        return bewertung

    def get_playingSide_pieces(self):
        positions = []
        if (self.Anzahlmoves % 2 ==0 ):
            for row in range(len(self.board)):
                for column in range(len(self.board[0])):
                    if self.board[row][column] is piece:
                        if self.board[row][column].color!="black":
                            positions.append ((row, column))

        return positions
    def zugGenerator(self):
        positions = self.get_playingSide_pieces()
        züge = { }
        for position in positions:
            row,column = position
            piece =board[row][column]
            piece.clear_list()
            if isinstance(piece, Pawn):
                piece.possible_moves_pawn(self.board)
            elif isinstance(piece, King):
                piece.possible_moves_king(self.board)
            elif isinstance(piece, Knight):
                piece.possible_moves_knight(self.board)
            elif isinstance(piece, Bishop):
                piece.possible_moves_bishop(self.board)
            elif isinstance(piece, Rook):
                piece.possible_moves_rook(self.board)
            elif isinstance(piece, Queen):
                piece.possible_moves_queen(self.board)
            züge[position] = piece.possible_moves_list
        legal_moves = {}
        for position, moves in züge.items(): #gpt
            for move in moves:
                if self.isLegal(position, move):
                    if position not in legal_moves:
                        legal_moves[position] = [move]
                    else:
                        legal_moves[position].append(move)

        return legal_moves


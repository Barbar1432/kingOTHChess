import pygame
import pygame.gfxdraw
from piece import piece
from piece import Rook, Knight, Bishop, Queen, King,Pawn
class board :
    def __init__(self):
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

    def draw_board(self, booly, pos, name, clickedpos):
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
            # Clicked tile lit green
             self.screen.blit(transparent_screen, (col * self.square_size + self.dislocation_count_col, row * self.square_size + self.dislocation_count_row))
             self.screen.blit(clicked_image, (pos[1]-30 + self.dislocation_count_col, pos[0]-30 + self.dislocation_count_row))


    def draw(self, booly, pos, name, clickedpos):
        self.draw_board(booly, pos, name, clickedpos)
        pygame.display.flip()

    def move(self, sqSelected, sqDest):

        row, col = sqSelected

        piece = self.board[row][col]
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




    def positions(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if (self.board[row][column] != None):
                    self.board[row][column].position = (row,column)

                    print( self.board[row][column].name, "pozisyonu" ,(row,column), "self", self.board[row][column].position) #KALDIR



    def get_Kingsposition(self, sqSelected):
        r_selected ,c_selected = sqSelected
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if isinstance(self.board[row][column], King) and self.board[r_selected][c_selected].color == self.board[row][column].color:
                    return (row, column)

    def is_king_threatened(self,start_pos,dest_pos):

        (kingr, kingc)= self.get_Kingsposition(start_pos)
        self.move(start_pos,dest_pos)
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[kingr][kingc].color == self.board[row][column].color:
                    continue
                if  self.board[kingr][kingc] in self.board[row][column].possible_moves_list:
                    self.move(self, dest_pos, start_pos) #undo
                    return True
        self.move(self, dest_pos, start_pos)  # undo
        return False



    def isLegal(self, start_pos, dest_pos):
        start_row, start_col = start_pos
        dest_row, dest_col = dest_pos
        start = self.board[start_row][start_col] # start is a piece
        dest = self.board[dest_row][dest_col] # dest can either be a square (None) or a piece
        if start is None : # look if there actually is a piece on the start square
            return False
        if not start.possible_moves_list.__contains__(dest_pos) : # look if the destination is a possible move for the piece
            return False
        if start.possible_moves_list.__contains__(dest_pos) and dest !=None:
            if dest.color == start.color:
                return False
        if self.is_king_threatened(start_pos, dest_pos): #if the move results in a check position for the playing side is ilegal
            return False
        else :
            return True





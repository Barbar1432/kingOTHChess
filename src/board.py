import pygame
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

    def draw_board(self, booly, pos, name, clickedpos):
         colors = [(255, 206, 158), (209, 139, 71)]

         for row in range(8):
             for col in range(8):

                 color = colors[(row + col) % 2]
                 rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                 pygame.draw.rect(self.screen, color, rect)
                 if self.board[row][col] != None:  # Print the piece on the board
                     piece_image = pygame.image.load('images/' + self.board[row][col].name + '.png')
                     piece_image = pygame.transform.scale(piece_image, (self.square_size, self.square_size))
                     self.screen.blit(piece_image, rect)

         if booly: # Drag and drop booly

             clicked_image = pygame.image.load('images/' + name + '.png')
             (row,col) = clickedpos
             transparent_screen = pygame.Surface((self.square_size, self.square_size))
             transparent_screen.set_alpha(120)
             transparent_screen.fill((144, 238, 144))
            # Clicked tile lit green
             self.screen.blit(transparent_screen, (col * self.square_size, row * self.square_size))
             self.screen.blit(clicked_image, (pos[1]-30, pos[0]-30))
    def draw(self, booly, pos, name, clickedpos):
        self.draw_board(booly, pos, name, clickedpos)
        pygame.display.flip()

    def move(self, sqSelected, sqDest):
        row, col = sqSelected
        piece = self.board[row][col]
        self.board[row][col] = None
        row, col = sqDest
        self.board[row][col] = piece



    def positions(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if (self.board[row][column] != None):
                    self.board[row][column].position = (row,column)

    def get_Kingsposition(self, king):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] == king:
                    return (row, column)

    def is_king_threatened(self,start_pos,dest_pos,king):

        kingPos= self.get_Kingsposition(self,king)
        self.move(start_pos,dest_pos)
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if king.color == self.board[row][column].color:
                    continue
                if  king in self.board[row][column].possible_moves_list:
                    self.move(self, dest_pos, start_pos) #undo
                    return True
        self.move(self, dest_pos, start_pos)  # undo
        return False



    def isLegal(self, start_pos, dest_pos):
        start_row, start_col = start_pos
        dest_row, dest_col = dest_pos
        start= self.board[start_row][start_col] # start is a piece
        dest = self.board[dest_row][dest_col] # dest can either be a square (None) or a piece
        if start is None : # look if there actually is a piece on the start square
            return False
        if not start.possible_moves_list.__contains__(dest_pos) : # look if the destination is a possible move for the piece
            return False
        if start.possible_moves_list.__contains__(dest_pos) and dest.color==start.color:
            return False
        if   self.is_king_threatened(): #if the move results in a check position for the playing side is ilegal
            return False
        else :
            return True





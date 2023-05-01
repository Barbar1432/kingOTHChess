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

    def draw_board(self):
         colors = [(255, 206, 158), (209, 139, 71)]

         for row in range(8):
             for col in range(8):

                 color = colors[(row + col) % 2]
                 rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                 pygame.draw.rect(self.screen, color, rect)
                 if self.board[row][col] != None:
                     piece_image = pygame.image.load('images/'+ self.board[row][col].name +'.png')
                     piece_image = pygame.transform.scale(piece_image, (self.square_size, self.square_size))
                     self.screen.blit(piece_image, rect)




    def draw(self):
        self.draw_board()
        pygame.display.flip()

    def move(self,sqSelected,sqDest):


        row, col = sqSelected
        row_move, col_move = sqDest
        piece = self.board[row][col]
        #piece.possible_moves()
        #if sqDest in piece.possible_moves_list:     TEKRAR BAKILACAK
        self.board[row][col] = None
        self.board[row_move][col_move] = piece

    def positions(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if (self.board[row][column] != None):
                    self.board[row][column].position = row,column












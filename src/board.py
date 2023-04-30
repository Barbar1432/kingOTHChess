import pygame
class board :
    def __init__(self):
     self.board=[["bK", "bAt", "bFil", "bV", "bSah", "bFil", "bAt", "bK"],
        ["bPion", "bPion", "bPion", "bPion", "bPion", "bPion", "bPion", "bPion"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["sPion", "sPion", "sPion", "sPion", "sPion", "sPion", "sPion", "sPion"],
        ["sK", "sAt", "sFil", "sV", "sSah", "sFil", "sAt", "sK"]
    ]
     self.square_size = 50
     self.screen_size = (self.square_size * 8, self.square_size * 8)
     self.screen = pygame.display.set_mode(self.screen_size)

    def draw_board(self):
         colors = [(255, 206, 158), (209, 139, 71)]

         for row in range(8):
             for col in range(8):

                 color = colors[(row + col) % 2]
                 rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                 pygame.draw.rect(self.screen, color, rect)
                 if self.board[row][col] != " ":
                     piece_image = pygame.image.load('images/'+ self.board[row][col] +'.png')
                     piece_image = pygame.transform.scale(piece_image, (self.square_size, self.square_size))
                     self.screen.blit(piece_image, rect)

        #test
        #test


    def draw(self):
        self.draw_board()
        pygame.display.flip()

    def move(self,sqSelected,sqDest):
        row, col = sqSelected
        piece = self.board[row][col]
        self.board[row][col] = " "
        row, col = sqDest
        self.board[row][col] = piece









import pygame
import pygame.gfxdraw
from colors import get_color
from piece import piece
from piece import Rook, Knight, Bishop, Queen, King,Pawn
import numpy as np
import copy
class board :
    def __init__(self):
         self.whiteKing = King("white","bSah",(0,0))
         self.blackKing = King("black", "sSah",(0,0))
         self.Anzahlmoves = 0
         self.whiteKing.position =(7,4)
         self.blackKing.position=(0,4)
         self.finished = False
         self.moves_white ={}
         self.moves_black = {}

         self.mapping =piece_mapping = {
              "sSah": 1111,
             "bSah": 2111,
            "sK": 1011,
            "bK": 2011,
            "sAt": 1001,
             "bAt": 2001,
            "sFil": 1010,
             "bFil": 2010,
             "sV": 1110,
             "bV": 2110,
            "sPion": 1000,
            "bPion": 2000
}
         self.board = [
            [ Rook('black', "sK",(0,0)),Knight('black',"sAt",(0,0)), Bishop('black',"sFil",(0,0)), Queen('black',"sV",(0,0)), self.blackKing, Bishop('black',"sFil",(0,0)),
             Knight('black',"sAt",(0,0)), Rook('black',"sK",(0,0))],
            [Pawn('black',"sPion",(0,0)) for _ in range(8)],
            [None] * 8, [None] * 8,[None] * 8,[None] * 8,
            [Pawn('white',"bPion",(0,0)) for _ in range(8)],
            [Rook('white', "bK",(0,0)), Knight('white', "bAt",(0,0)), Bishop('white', "bFil",(0,0)), Queen('white',"bV",(0,0)),
             self.whiteKing, Bishop('white',"bFil",(0,0)), Knight('white', "bAt",(0,0)), Rook('white', "bK",(0,0))] ]
         self.boardInteger = np.array([
             [1011, 1001, 1010, 1110, 1111, 1010, 1001, 1011],[1000 for _ in range(8)],
             [1600 for _ in range(8)],
             [1600 for _ in range(8)],
             [1600 for _ in range(8)],
             [1600 for _ in range(8)],
             [2000 for _ in range(8)],
             [2011, 2001, 2010, 2110, 2111, 2010, 2001, 2011]])
         self.square_size = 64
         self.screen_size = (self.square_size * 8, self.square_size * 8)
         self.screen = pygame.display.set_mode(self.screen_size)
         self.lastmove = ()
         self.eatenPiecesWhite = []
         self.eatenPiecesBlack = []
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
         trans_color = get_color("shadow")
         orange_color = get_color("orange")
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
         if self.lastmove != ():
             sqSelected, sqDest = self.lastmove
             sqSelectedRow, sqSelectedCol = sqSelected
             sqDestRow, sqDestCol = sqDest
             pygame.gfxdraw.box(self.screen, pygame.Rect(sqSelectedCol * self.square_size + self.dislocation_count_col,
                                      sqSelectedRow * self.square_size + self.dislocation_count_row, self.square_size,
                                      self.square_size), orange_color)
             pygame.gfxdraw.box(self.screen, pygame.Rect(sqDestCol * self.square_size + self.dislocation_count_col,
                                        sqDestRow * self.square_size + self.dislocation_count_row, self.square_size,
                                        self.square_size), orange_color)
             piece_image = pygame.image.load('images/' + self.board[sqDestRow][sqDestCol].name + '.png')
             piece_image = pygame.transform.scale(piece_image, (self.square_size, self.square_size))
             self.screen.blit(piece_image, pygame.Rect(sqDestCol * self.square_size + self.dislocation_count_col,
                                        sqDestRow * self.square_size + self.dislocation_count_row, self.square_size,
                                        self.square_size))

         if booly: # Drag and drop booly
             # Helping bubbles for possible moves
             (row, col) = clickedpos
             clickedpiece = self.board[row][col]
             self.callPossibleMoves(clickedpos)
             listBub = clickedpiece.possible_moves_list
             colorBub = get_color("bubble")
             for bubble in listBub:
                 if (self.isLegal(clickedpos, bubble)):
                     bub_row, bub_col = bubble
                     pygame.draw.circle(self.screen, colorBub,
                                        (bub_col * self.square_size + self.dislocation_count_col + 32,
                                         bub_row * self.square_size + self.dislocation_count_row + 32),
                                        10)
             # Dragged piece animation
             clicked_image = pygame.image.load('images/' + name + '.png')
             (row,col) = clickedpos
             transparent_screen = pygame.Surface((self.square_size, self.square_size))
             transparent_screen.set_alpha(120)
             transparent_screen.fill(colorBub)
             pos1, pos2 = pygame.mouse.get_pos()
             pos1 = pos1 - self.dislocation_count_row
             pos2 = pos2 - self.dislocation_count_col
            # Clicked tile lit green
             self.screen.blit(transparent_screen, (col * self.square_size + self.dislocation_count_col, row * self.square_size + self.dislocation_count_row))
             self.screen.blit(clicked_image, (pos1-30 + self.dislocation_count_row, pos2-30 + self.dislocation_count_col))

         if self.eatenPiecesBlack is not [] or self.eatenPiecesWhite is not []:
             listBlack = list(self.eatenPiecesBlack)
             listWhite = list(self.eatenPiecesWhite)
             font = pygame.font.SysFont("fonts/PokemonGB.ttf", 15)
             text_color = get_color("text")
             text_dislocation_w = 14
             text_dislocation_b = 14
             i = 0
             j = 0
             k = 0
             l = 0
             m = 0
             n = 0
            #  Print eaten black Pieces:
             for eatenpieces in listBlack:
                 if eatenpieces[2] > 9:
                     text_dislocation_b = 12
                 img = pygame.image.load('images/' + eatenpieces[0] + '.png')
                 img = pygame.transform.scale(img, (32, 32))
                 turnText = font.render(("%d" % eatenpieces[2]), False, text_color)
                 if j != 0 and j % 4 == 0:
                     k += 34
                     i = 0
                 self.screen.blit(img, (self.dislocation_count_col + self.square_size * 8 + 23 + i,
                                        self.dislocation_count_row + self.square_size * 4 + 24 + k))
                 self.screen.blit(turnText, (self.dislocation_count_col + self.square_size * 8 + 23 + text_dislocation_b + i,
                                        self.dislocation_count_row + self.square_size * 4 + 24 + 28 + k)) #  28 - Text mesafe
                 i += 28
                 j += 1
            # Print eaten white Pieces
             for eatenpieces2 in listWhite:
                 if eatenpieces2[2] > 9:
                     text_dislocation_w = 12
                 img = pygame.image.load('images/' + eatenpieces2[0] + '.png')
                 img = pygame.transform.scale(img, (32, 32))
                 turnText = font.render(("%d" % eatenpieces2[2]), False, text_color)
                 if m != 0 and m % 4 == 0:
                     n += 34
                     l = 0
                 self.screen.blit(img, (self.dislocation_count_col + self.square_size * 10 + 26 + l,
                                        self.dislocation_count_row + self.square_size * 4 + 24 + n))
                 self.screen.blit(turnText, (self.dislocation_count_col + self.square_size * 10 + 26 + text_dislocation_w + l,
                                             self.dislocation_count_row + self.square_size * 4 + 24 + 28 + n))  # 28 - Text mesafe
                 l += 28
                 m += 1


    def draw(self, booly, name, clickedpos):
        self.draw_board(booly, name, clickedpos)
        pygame.display.flip()

    def positions(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if (self.board[row][column] != None):
                    self.board[row][column].position = (row, column)
    def callPossibleMoves (self,sqSelected):
        row, col = sqSelected
        piece = self.board[row][col]
        if self.board[row][col] != None:
            piece.clear_list()
        if isinstance(piece, Pawn):
            piece.possible_moves_pawn(self.board)
        elif isinstance(piece, King):
            piece.possible_moves_king(self.board,self)
        elif isinstance(piece, Knight):
            piece.possible_moves_knight(self.board)
        elif isinstance(piece, Bishop):
            piece.possible_moves_bishop(self.board)
        elif isinstance(piece, Rook):
            piece.possible_moves_rook(self.board)
        elif isinstance(piece, Queen):
            piece.possible_moves_queen(self.board)

    def is_king_threatened(self, start_pos, des_pos, king,positions):
        kingPos = king.position
        row, column = start_pos
        a, b = des_pos
        dest = self.board[a][b]
        pinned = self.board[row][column]
        if (start_pos == kingPos):
            king.position = des_pos
        self.board[row][column] = None
        self.board[a][b] = pinned
        row_indices, col_indices = positions
        for x, y in zip(row_indices, col_indices):
            if self.board[x][y] is not None and self.board[x][y].color != king.color :
                    sq = (x, y)
                    self.callPossibleMoves(sq)
                    if self.board[x][y].possible_moves_list.__contains__(king.position):
                        self.board[row][column] = pinned
                        self.board[a][b] = dest
                        king.position = kingPos
                        return True

        self.board[row][column] = pinned
        self.board[a][b] = dest
        king.position = kingPos

        return False

    def is_square_threatening_king(self, square, king):

        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                if self.board[x][y] is not None and self.board[x][y].color != king.color:
                    opponent_piece = self.board[x][y]

                    if opponent_piece.possible_moves_list.__contains__(square):


                        return True

        return False

    def isLegal(self, start_pos, dest_pos):
        start_row, start_col = start_pos
        dest_row, dest_col = dest_pos
        if not (0 <= start_row < len(self.board) and 0 <= start_col < len(self.board[0])):
            return False
        if not (0 <= dest_row < len(self.board) and 0 <= dest_col < len(self.board[0])):
            return False
        if (self.Anzahlmoves %2 == 0 and self.board[start_row][start_col].color != "white"):
            return False
        if (self.Anzahlmoves % 2 == 1 and self.board[start_row][start_col].color != "black"):
            return False

        start = self.board[start_row][start_col] # start is a piece

        dest = self.board[dest_row][dest_col] # dest can either be a square (None) or a piec
        self.callPossibleMoves(start_pos)
        if start is None : # look if there actually is a piece on the start square
            return False
        if not start.possible_moves_list.__contains__(dest_pos) : # look if the destination is a possible move for the piece
            return False

        if dest is not None:
               if start.color=="black" and dest.color== "white":
                  return True
               if start.color == "white" and dest.color == "black":
                    return True
        else :
            return True
    def bewertungsFunktion(self):

        whitePoints = 0
        blackPoints = 0
        center = [(3,4), (4,4), (3,3), (4,3)]
        black_positions = np.where(self.boardInteger < 1600)
        white_positions = np.where(self.boardInteger >= 2000)
        row_indices, col_indices = white_positions
        for row, col in zip(row_indices, col_indices):
            piece = self.board[row][col]
            if isinstance(piece, King) and piece.color == "white" and self.Anzahlmoves >= 12:
               whitePoints +=piece.PST_white_midGame
               continue
            whitePoints += piece.PST_white[row][col]
            if(isinstance(piece, Pawn)):
                temp =self.board[row+1][col]
                if (isinstance(temp, Pawn)):
                    if (temp.color == "white"):
                       whitePoints=whitePoints-10
                whitePoints += 100
                continue
            whitePoints += piece.point
        rindices, cindices = black_positions
        for r, c in zip(rindices, cindices):
            piece = self.board[r][c]
            if isinstance(piece, King) and piece.color == "black" and self.Anzahlmoves >= 12:
                blackPoints +=piece.PST_black_midGame
                continue
            blackPoints += piece.PST_black[r][c]
            if (isinstance(piece, Pawn)):
                temp = self.board[r + 1][c]
                if (isinstance(temp, Pawn)):
                    if (temp.color == "black"):
                        blackPoints = blackPoints - 10
                blackPoints += 100
                continue
            blackPoints += piece.point
        bewertung = (whitePoints - blackPoints)
        return bewertung


    def legalMoves(self):
        legalMoves = {}

        black_positions = np.where(self.boardInteger < 1600)
        white_positions = np.where(self.boardInteger >= 2000)
        if self.Anzahlmoves % 2 == 0:  # sıra beyazda
            row_indices, col_indices = white_positions
            for row, col in zip(row_indices, col_indices):
                pos = (row, col)

                self.callPossibleMoves(pos)
                legalMoves[pos] = []
                for pM in self.board[row][col].possible_moves_list:
                   if (self.isLegal(pos, pM) and self.is_king_threatened(pos, pM, self.whiteKing,black_positions) == False):
                        legalMoves[self.board[row][col].position].append(pM)

            return legalMoves
        if self.Anzahlmoves % 2 == 1:
            row_indices, col_indices = black_positions
            for row, col in zip(row_indices, col_indices):
                pos = (row, col)
                self.callPossibleMoves(pos)
                legalMoves[pos] = []
                for pM in self.board[row][col].possible_moves_list:
                    if (self.isLegal(pos, pM) and self.is_king_threatened(pos, pM, self.blackKing,white_positions) == False):
                        legalMoves[self.board[row][col].position].append(pM)


            return legalMoves
    def moveZa (self,sqSelected, sqDest):



       if self.finished:
           pygame.display.set_caption("GAME OVER")
           return

       try:
           row, col = sqSelected


           legalMoves = self.legalMoves()
           row, col = sqSelected
           piece = self.board[row][col]
           if isinstance(piece,Rook):
               piece.rook_moved = True



           row_dest, col_dest = sqDest

           if self.board[row][col] != None:
                if legalMoves[sqSelected].__contains__(sqDest):
                    row_dest, col_dest = sqDest

                    #  Collection of eaten pieces  #
                    if self.boardInteger[row_dest][col_dest] != 1600:
                        if self.board[row_dest][col_dest].color == 'white':
                            self.eatenPiecesWhite.append((self.board[row_dest][col_dest].name,
                                                          self.boardInteger[row_dest][col_dest], self.Anzahlmoves))
                        else:
                            self.eatenPiecesBlack.append((self.board[row_dest][col_dest].name,
                                                          self.boardInteger[row_dest][col_dest], self.Anzahlmoves))

                    self.board[row][col] = None
                    self.board[row_dest][col_dest] = piece
                    self.boardInteger[row][col] = 1600
                    self.boardInteger[row_dest][col_dest] = self.mapping[piece.name]

                    piece.position = (row_dest, col_dest)
                    print(self.bewertungsFunktion())
                    self.Anzahlmoves+= 1
                    #print(self.Anzahlmoves)
                    if isinstance(piece, King):
                        if piece.position == (4,3) or piece.position == (3,3) or piece.position == (3,4) or piece.position == (4,4):
                            self.finished = True


                        if sqDest == (7, 6) and piece.king_moved == False:
                            rook = self.board[7][7]
                            self.board[7][7] = None
                            self.boardInteger[7][7] = 1600
                            self.board[7][5] = rook
                            self.boardInteger[7][5] = 2011
                            rook.position = (7, 5)

                        elif sqDest == (7, 1) and piece.king_moved == False:
                            rook = self.board[7][0]
                            self.board[7][0] = None
                            self.boardInteger[7][0] = 1600
                            self.board[7][2] = rook
                            self.boardInteger[7][2] = 2011
                            rook.position = (7, 2)

                        elif sqDest == (0, 6) and piece.king_moved == False:
                            rook = self.board[0][7]
                            self.board[0][7] = None
                            self.boardInteger[0][7] = 1600
                            self.board[0][5] = rook
                            self.boardInteger[0][5] = 1011
                            rook.position = (0, 5)

                        elif sqDest == (0, 1) and piece.king_moved == False:
                            rook = self.board[0][0]
                            self.board[0][0] = None
                            self.boardInteger[0][0] = 1600
                            self.board[0][2] = rook
                            self.boardInteger[0][2] = 1600
                            rook.position = (0, 2)
                        piece.king_moved = True
                    self.lastmove = (sqSelected, sqDest)

       except KeyError:
           return



    def is_castling_free(self, sqSelected):
        right_free = False
        left_free = False
        row, col = sqSelected


        King = self.board[row][col]

        for i in range (col+1,7):

            if self.board[row][i] == None: #check if there is a piece inbetween
                right_free = True

                #print("Kimsecikler yok")
            else:
                right_free = False
                break
        if right_free == True and (isinstance(self.board[row][7],Rook) == True) and self.board[row][7].rook_moved == False and King.king_moved == False and (self.board[row][7].position ==(0,7) or self.board[row][7].position ==(7,7)): #if free and there is a rook

            right_free = True
        else:
            right_free = False

        for y in range (col-1,0,-1):
            #print("YYYYYYY", y)
            if self.board[row][y] == None:
                left_free = True
                #print("kimse yok sol")
            else:
                left_free = False
                break

        if left_free == True and isinstance(self.board[row][0],Rook) == True and self.board[row][0].rook_moved == False and King.king_moved == False and (self.board[row][0].position ==(0,0) or self.board[row][0].position ==(7,0)):

            left_free = True
        else:
            left_free = False

        return (right_free, left_free)

    def castling_checked(self,sqSelected):
        right_castling = False
        left_castling = False
        row, col = sqSelected

        King = self.board[row][col]
        right, left = self.is_castling_free(sqSelected)
        #print("right= ",right, " left= " ,left)
        (king_row, king_column) = King.position #real position
        (king_row1, king_column1) = King.position

        if right == True and King.color == 'white':
            threatened_right_white = self.is_square_threatening_king((7,5),King)
            #print("threatened_right_white:",threatened_right_white)
            if threatened_right_white == False:
                threatened_right_white = self.is_square_threatening_king((7,6), King)

            if threatened_right_white == True:
                right = False
        elif right == True and King.color == 'black':
            threatened_right_black = self.is_square_threatening_king((0, 5), King)
            if threatened_right_black == False:
                threatened_right_black = self.is_square_threatening_king((0, 6), King)
            if threatened_right_black == True:
                right = False

        if left == True and King.color == 'white':
            threatened_left_white = self.is_square_threatening_king((7,3),King)
            if threatened_left_white == False:
                threatened_left_white = self.is_square_threatening_king((7, 2), King)
                if threatened_left_white == False:
                    threatened_left_white = self.is_square_threatening_king((7, 1), King)
            if threatened_left_white == True:
                left =False

        elif left == True and King.color == 'black':
            threatened_left_black = self.is_square_threatening_king((0,3),King)
            if threatened_left_black == False:
                threatened_left_black = self.is_square_threatening_king((0, 2), King)
                if threatened_left_black == False:
                    threatened_left_black = self.is_square_threatening_king((0, 1), King)
            if threatened_left_black == True:
                left = False




        #print((king_row, king_column + 2), "OLSUNDU")
        #print(King.possible_moves_list)
        #print("----------")
        return (right,left)

    def undo_move(self, sqSelected, sqDest):
        row, col = sqSelected
        piece = self.board[row][col]
        row_dest, col_dest = sqDest
        self.board[row][col] = None
        self.board[row_dest][col_dest] = piece
        self.boardInteger[row][col] = 1600
        self.boardInteger[row_dest][col_dest] = self.mapping[piece.name]
        piece.position = (row_dest, col_dest)
        self.Anzahlmoves = self.Anzahlmoves - 1

    def alpha_beta(self, board, depth, alpha, beta, is_max):
        if depth == 0 or self.isGameOver(board):
            return board.bewertungsFunktion()
        if is_max:
            best_value = alpha
            _, moves_list = board.legalMoves_alphaBeta(self.board,self.boardInteger,True)
            for move in moves_list:
                sq_selected, sq_dest = move
                board.move(sq_selected, sq_dest)  # Apply the move to the current board
                value = self.alpha_beta(board, depth - 1, best_value, beta, False)
                board.undo_move(sq_selected, sq_dest)  # Undo the move to restore the board state
                best_value = max(best_value, value)
                if best_value >= beta:  # Beta-Cutoff
                    break
            return best_value

        else:
            best_value = beta
            _, moves_list = board.legalMoves_alphaBeta(self.board, self.boardInteger, False)
            for move in moves_list:
                sq_selected, sq_dest = move
                board.move(sq_selected, sq_dest)  # Apply the move to the current board
                value = self.alpha_beta(board, depth - 1, alpha, best_value, True)
                board.undo_move(sq_selected, sq_dest)  # Undo the move to restore the board state
                best_value = min(best_value, value)
                if best_value <= alpha:  # Alpha-Cutoff
                    break
            return best_value

    def isGameOver(self):
        # TODO: If no more possible moves - Stalemate
        if self.finished:
            return True

    def move(self, sqSelected, sqDest):
        row, col = sqSelected
        piece = self.board[row][col]
        row_dest, col_dest = sqDest
        self.board[row][col] = None
        self.board[row_dest][col_dest] = piece
        self.boardInteger[row][col] = 1600
        self.boardInteger[row_dest][col_dest] = self.mapping[piece.name]
        piece.position = (row_dest, col_dest)
        self.Anzahlmoves += 1

    def legalMoves_alphaBeta(self, board,intBoard,isMax):
        legalMoves = {}
        moves = []
        black_positions = np.where(self.boardInteger < 1600)
        white_positions = np.where(self.boardInteger >= 2000)
        if isMax:  # sıra beyazda
            row_indices, col_indices = white_positions
            for row, col in zip(row_indices, col_indices):
                pos = (row, col)

                self.callPossibleMoves(pos)
                legalMoves[pos] = []
                for pM in self.board[row][col].possible_moves_list:
                    if (self.isLegal(pos, pM) and self.is_king_threatened(pos, pM, self.whiteKing,black_positions) == False):
                        legalMoves[self.board[row][col].position].append(pM)
                        moves.append((self.board[row][col].position, pM))

            return legalMoves, moves
        else:
            row_indices, col_indices = black_positions
            for row, col in zip(row_indices, col_indices):
                pos = (row, col)
                self.callPossibleMoves(pos)
                legalMoves[pos] = []
                for pM in self.board[row][col].possible_moves_list:
                    if (self.isLegal(pos, pM) and self.is_king_threatened(pos, pM, self.blackKing, white_positions) == False):
                        legalMoves[self.board[row][col].position].append(pM)
                        moves.append((self.board[row][col].position, pM))

            return legalMoves, moves




   
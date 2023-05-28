import pygame
import pygame.gfxdraw
from colors import get_color
from piece import piece
from piece import Rook, Knight, Bishop, Queen, King,Pawn
import numpy as np
class board :
    def __init__(self):
         self.whiteKing = King("white","bSah")
         self.blackKing = King("black", "sSah")
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
            [ Rook('black', "sK"),Knight('black',"sAt"), Bishop('black',"sFil"), Queen('black',"sV"), self.blackKing, Bishop('black',"sFil"),
             Knight('black',"sAt"), Rook('black',"sK")],
            [Pawn('black',"sPion") for _ in range(8)],
            [None] * 8, [None] * 8,[None] * 8,[None] * 8,
            [Pawn('white',"bPion") for _ in range(8)],
            [Rook('white', "bK"), Knight('white', "bAt"), Bishop('white', "bFil"), Queen('white',"bV"),
             self.whiteKing, Bishop('white',"bFil"), Knight('white', "bAt"), Rook('white', "bK")] ]
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
            if(piece==Pawn):
                temp =self.board[row+1][col]
                if (temp==Pawn):
                    if (temp.color == "white"):
                       whitePoints=whitePoints-5
                whitePoints += 10
                continue
            if (piece.played):
                whitePoints+=20
            whitePoints += piece.point * 15
            whitePoints = whitePoints + piece.PST_white[row][col]
        rindices, cindices = black_positions
        for r, c in zip(rindices, cindices):
            piece = self.board[r][c]
            if (piece == Pawn):
                temp = self.board[r + 1][c]
                if (temp == Pawn):
                    if (temp.color == "black"):
                        blackPoints = blackPoints - 5
                blackPoints += 10
                continue
            if (piece.played):
                blackPoints += 20
            blackPoints += piece.point * 15
            blackPoints = blackPoints + -1*piece.PST_black[r][c]

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
           #print(self.bewertungsFunktion())
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

    """
         bu klasik alpha beta boyleydi hemen hemen şimdilik gptye bidaha yazdırttım anla diye kodun kalanını
         """
    def alpha_beta(self,board, depth, alpha, beta, is_max):
        # if depth == 0 or isGameOver(board):
           # return board_evaluation(board)

        if is_max:
            best_value = float('-inf')
            for child in self.createBoard(board):
                value = self.alpha_beta(child, depth - 1, alpha, beta, False)
                best_value = max(best_value, value)
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    # Alpha cutoff
                    break
            return best_value

        else:
            best_value = float('inf')
            for child in self.createBoard(board):
                value =self.alpha_beta(child, depth - 1, alpha, beta, True)
                best_value = min(best_value, value)
                beta = min(beta, best_value)
                if beta <= alpha:
                    # Beta cutoff
                    break
            return best_value


    """
        Abi şimdilik benim herşeyi tek boardda yapmaya calıstıgım implementasyonu rafakaldırdık. bu klasik bir sürü board generate etmeli
        implementasyonu deneyelim tekrardan diye düşündüm. Onun içinde deepCpy kullanmak gerekiyor heralde. 
        Boardu copyliyincede cok masraflı oluyo ondan bu numpy boardu copyleyemek daha mantıklı geldi. 
        """
    """
     şimdi su sekil calısıyo bu once bitane IntegerBoard alıyo , o dalyarragı mecburen self.convert_board_integer_to_board
     fonksiyonuyla normal bi boarda çeviriyo (legalMoves falan vb fonksiyonları kullanamıyoruz yoksa) sonra 20 tane legal move
     varsa 20 tane board oluşturuyo hepsinde birer move oynanmış olarak
     dipNot olarak " self.convert_board_integer_to_board fonksiyonuyla normal bi boarda çeviriyo" şimdi madem dondurcektik buna
     ne manası oldu gibi bir düşünce var aklımda ama mesela en son depthtekilerin hiçbirini cevirmiyoruz 7 depthte bile 256 board 
     yapıyor birde cutoffları falan dusununce yinede yapmaya deger gibi geldi .Board represantasyonunu terk edip boardIntegera gecebilsek
     super olurdu aslında ama o cok iş gibi gozukuyor şimdilik piece classını falan epey degistirmemiz gerekir 
     """
    def createBoard (self,boardInt):
         zaBoard =  self.convert_board_integer_to_board(boardInt)
         legalMoves,moves= self.legalMoves_alphaBeta(zaBoard)
         for move in moves:
             start,dest = move
             s_row ,s_col = start
             d_row,d_col = dest
             board = np.copy(boardInt)
             pieceMoved =board[s_row][s_col]
             board[s_row][s_col] = 1600
             board[d_row][d_col] =pieceMoved

    """
    bu işte ismi zaten anlatıyo ne bok yaptıgını , yalnız pozisyon atamıyo galiba  Pawn('black', "sPion") lara pozisyon 
    variablesinide ekleyebiliriz 
     """

    def convert_board_integer_to_board(self,boardInt):
        board = []
        for row in boardInt:
            board_row = []
            for value in row:
                if value == 1000:
                    board_row.append(Pawn('black', "sPion"))
                elif value == 1011:
                    board_row.append(Rook('black', "sK"))
                elif value == 1001:
                    board_row.append(Knight('black', "sAt"))
                elif value == 1010:
                    board_row.append(Bishop('black', "sFil"))
                elif value == 1110:
                    board_row.append(Queen('black', "sV"))
                elif value == 1111:
                    board_row.append(King("black", "sSah"))
                elif value == 2000:
                    board_row.append(Pawn('white', "bPion"))
                elif value == 2011:
                    board_row.append(Rook('white', "bK"))
                elif value == 2001:
                    board_row.append(Knight('white', "bAt"))
                elif value == 2010:
                    board_row.append(Bishop('white', "bFil"))
                elif value == 2110:
                    board_row.append(Queen('white', "bV"))
                elif value == 2111:
                    board_row.append( King("white","bSah"))
                else:
                    board_row.append(None)
            board.append(board_row)
        return board

    """
     bunu surekli degisiklikler yaptıgım için ekledim kodun kalanında sıkıntılar oluyodu deneme tahtası gibi ama farkı su annlık
     board parametresi alıyo bitane ( self.board) dısındakı seylerle pushlayabiliyoruz birde legalMOves dicionarysinin yanında normal 
     moves diye tim legal moveları donduren bi liste de veriyor . birde buna işte kimin sırası olduguna dair bir parametre daha 
     ekleyebiliriz yoksa siyahın sıralarını generate etcekken self.AnzahlMoves bu alpha betadan bagımsız oldugu için 
     sorun cıkabilir 
        """

    def legalMoves_alphaBeta(self, board):
        legalMoves = {}
        moves = []
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
                        moves.append((self.board[row][col].position, pM))

            return legalMoves, moves
        if self.Anzahlmoves % 2 == 1:
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




   
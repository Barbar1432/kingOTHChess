import pygame


class piece :
    def __init__(self,color,type):
        self.color =color
        self.type=type
        self.position = (0,0)
        self.possible_moves_list = []





class Pawn(piece):
    def __init__(self, color,name):
        super().__init__(color, 'pawn')
        self.name = name
        self.position = (0,0)
        self.played = False


    def possible_moves_pawn(self, board):

            # moves_of_Pawn = []
        if (self.played == False and self.color == 'black'):
            (row, column) = self.position
            self.possible_moves_list.append((row + 1, column))
            self.possible_moves_list.append((row + 2, column))
            self.played = True

        elif (self.played == True and self.color == 'black'):
            (row, column) = self.position
            self.possible_moves_list.append((row + 1, column))

        elif (self.played == False and self.color == 'white'):
            (row, column) = self.position
            self.possible_moves_list.append((row - 1, column))
            self.possible_moves_list.append((row - 2, column))
            self.played = True

        else:
            (row, column) = self.position
            self.possible_moves_list.append((row - 1, column))

    def clear_list(self):
        self.possible_moves_list.clear()


class Bishop(piece):
    def __init__(self, color,name):
        super().__init__(color, 'bishop')
        self.name=name
        self.position = (0,0)

class Knight(piece):
    def __init__(self, color,name):
        super().__init__(color, 'knight')
        self.name=name
        self.position = (0,0)

    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_knight(self, board):
        (row, column) = self.position

        try:
            self.possible_moves_list.append((row - 2, column + 1))
        except IndexError:
            pass

        try:
            self.possible_moves_list.append((row - 1, column + 2))
        except IndexError:
            pass

        try:
            self.possible_moves_list.append((row + 1, column + 2))
        except IndexError:
            pass

        try:
            self.possible_moves_list.append((row + 2, column + 1))
        except IndexError:
            pass

        try:
            self.possible_moves_list.append((row - 2, column - 1))
        except IndexError:
            pass

        try:
            self.possible_moves_list.append((row - 1, column - 2))
        except IndexError:
            pass

        try:
            self.possible_moves_list.append((row + 2, column - 1))
        except IndexError:
            pass

        try:
            self.possible_moves_list.append((row + 1, column - 2))
        except IndexError:
            pass


class King(piece):
    def __init__(self, color,name):
        super().__init__(color, 'king')
        self.name=name
        self.position = (0,0)

    def clear_list(self):
        self.possible_moves_list.clear()


    def possible_moves_king(self,board):
        (row, column) = self.position
        try:
            self.possible_moves_list.append((row + 1, column))
        except IndexError:
            pass
        try:
            self.possible_moves_list.append((row - 1, column))
        except IndexError:
            pass
        try:
            self.possible_moves_list.append((row, column - 1))
        except IndexError:
            pass
        try:
            self.possible_moves_list.append((row, column + 1))
        except IndexError:
            pass
        try:
            self.possible_moves_list.append((row - 1, column + 1))
        except IndexError:
            pass
        try:
            self.possible_moves_list.append((row + 1, column - 1))
        except IndexError:
            pass
        try:
            self.possible_moves_list.append((row + 1, column + 1))
        except IndexError:
            pass
        try:
            self.possible_moves_list.append((row - 1, column - 1))
        except IndexError:
            pass

class Queen(piece):
    def __init__(self, color,name):
        super().__init__(color, 'queen')
        self.name=name
        self.position = (0,0)

    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_queen(self, board):
        (row, column) = self.position

        for i in range(column + 1, len(board[0])):
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color != self.color:  # opponent's piece
                self.possible_moves_list.append((row, i))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction

            # Check moves to the left
        for i in range(column - 1, -1, -1):
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color != self.color:  # opponent's piece
                self.possible_moves_list.append((row, i))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction

            # Check moves down
        for i in range(row + 1, len(board)):
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color != self.color:  # opponent's piece
                self.possible_moves_list.append((i, column))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction

            # Check moves up
        for i in range(row - 1, -1, -1):
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color != self.color:  # opponent's piece
                self.possible_moves_list.append((i, column))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction



class Rook(piece):
    def __init__(self, color,name):
        super().__init__(color,'rook')
        self.name=name
        self.position = (0,0)

    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_rook(self, board):
        (row, column) = self.position

        for i in range(column + 1, len(board[0])):
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color != self.color:  # opponent's piece
                self.possible_moves_list.append((row, i))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction

            # Check moves to the left
        for i in range(column - 1, -1, -1):
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color != self.color:  # opponent's piece
                self.possible_moves_list.append((row, i))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction

            # Check moves down
        for i in range(row + 1, len(board)):
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color != self.color:  # opponent's piece
                self.possible_moves_list.append((i, column))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction

            # Check moves up
        for i in range(row - 1, -1, -1):
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color != self.color:  # opponent's piece
                self.possible_moves_list.append((i, column))
                break  # stop checking in this direction if there is an opponent's piece
            else:  # own piece blocking the way
                break  # stop checking in this direction



'''def possible_moves(piece, board):
    """

        for row in range(len(board)):
        for column in range(len(board[0])):
            if (board[row][column] == None):
                free = row, column
                self.possible_moves_list.append(free)
    """

    # BU FONKSİYONLARDA HEDEF KARENİN BOŞ OLUP OLMADIĞI KONTROL EDİLMİYOR, MOVE KISMINDA
    # SORGULATIRIZ DİYE DÜŞÜNEREK YAZMADIM DİLERSEK DEĞİŞİKLİK YAPABİLİRİZ AMA SONRA

    if(piece == Pawn):
        #moves_of_Pawn = []
        if(piece.played == False and piece.color == 'black'):
            (row, column) = piece.position
            piece.possible_moves_list.append((row + 1,column))
            piece.possible_moves_list.append((row + 2, column))
            piece.played=True

        elif(piece.played == True and piece.color == 'black'):
            (row, column) = piece.position
            piece.possible_moves_list.append((row + 1, column))

        elif (piece.played == False and piece.color == 'white'):
            (row, column) = piece.position
            piece.possible_moves_list.append((row - 1, column))
            piece.possible_moves_list.append((row - 2, column))

        else:
            (row, column) = piece.position
            piece.possible_moves_list.append((row - 1, column))



    elif(self == Bishop):
        moves_of_Bishop=[]
        (row, column) = piece.position




    elif(self == Knight):
        moves_of_Knight = []
        (row, column) = self.position

        try:
            moves_of_Knight.append((row-2, column+1))
        except IndexError:
            pass

        try:
            moves_of_Knight.append((row-1, column+2))
        except IndexError:
            pass

        try:
            moves_of_Knight.append((row+1, column+2))
        except IndexError:
            pass

        try:
            moves_of_Knight.append((row+2, column+1))
        except IndexError:
            pass

        try:
            moves_of_Knight.append((row-2, column-1))
        except IndexError:
            pass

        try:
            moves_of_Knight.append((row-1, column-2))
        except IndexError:
            pass

        try:
            moves_of_Knight.append((row+2, column-1))
        except IndexError:
            pass

        try:
            moves_of_Knight.append((row+1, column-2))
        except IndexError:
            pass



    elif (self == King):
        moves_of_King = []
        (row, column) = self.position
        try:
            moves_of_King.append((row+1, column))
        except IndexError:
            pass
        try:
            moves_of_King.append((row-1, column))
        except IndexError:
            pass
        try:
            moves_of_King.append((row, column-1))
        except IndexError:
            pass
        try:
            moves_of_King.append((row, column+1))
        except IndexError:
            pass
        try:
            moves_of_King.append((row-1, column+1))
        except IndexError:
            pass
        try:
            moves_of_King.append((row+1, column-1))
        except IndexError:
            pass
        try:
            moves_of_King.append((row + 1, column + 1))
        except IndexError:
            pass
        try:
            moves_of_King.append((row - 1, column - 1))
        except IndexError:
            pass



        True

    elif (self ==  Queen):
        True

    else: #Rook
        moves_of_Rook = []
        (row, column) = self.position

        while (board[row][column+1]==None and column+1 < len(board[0])): #RIGHT
            column+=1
            moves_of_Rook.append((row,column))



        (row, column) = self.position

        while (board[row+1][column] == None and column + 1 < len(board)): #DOWN
            row+=1
            moves_of_Rook.append((row, column))

        (row, column) = self.position

        while (board[row-1][column] == None and row -1 > 0):
            row -= 1
            moves_of_Rook.append((row, column))

        (row, column) = self.position

        while (board[row][column - 1] == None and column - 1 > 0):  # RIGHT
            column -= 1
            moves_of_Rook.append((row, column))

        (row, column) = self.position'''













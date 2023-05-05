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

class King(piece):
    def __init__(self, color,name):
        super().__init__(color, 'king')
        self.name=name
        self.position = (0,0)

class Queen(piece):
    def __init__(self, color,name):
        super().__init__(color, 'queen')
        self.name=name
        self.position = (0,0)


class Rook(piece):
    def __init__(self, color,name):
        super().__init__(color,'rook')
        self.name=name
        self.position = (0,0)



def possible_moves(self, board):
    """

        for row in range(len(board)):
        for column in range(len(board[0])):
            if (board[row][column] == None):
                free = row, column
                self.possible_moves_list.append(free)
    """

    # BU FONKSİYONLARDA HEDEF KARENİN BOŞ OLUP OLMADIĞI KONTROL EDİLMİYOR, MOVE KISMINDA
    # SORGULATIRIZ DİYE DÜŞÜNEREK YAZMADIM DİLERSEK DEĞİŞİKLİK YAPABİLİRİZ AMA SONRA

    if(self == Pawn):
        moves_of_Pawn = []
        if(self.played == False and self.color == 'black'):
            (row, column) = self.position
            moves_of_Pawn.append((row + 1,column))
            moves_of_Pawn.append((row + 2, column))
            self.played=True

        elif(self.played == True and self.color == 'black'):
            (row, column) = self.position
            moves_of_Pawn.append((row + 1, column))

        elif (self.played == False and self.color == 'white'):
            (row, column) = self.position
            moves_of_Pawn.append((row - 1, column))
            moves_of_Pawn.append((row - 2, column))

        else:
            (row, column) = self.position
            moves_of_Pawn.append((row - 1, column))



    elif(self == Bishop):
        moves_of_Bishop=[]
        (row, column) = self.position




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

        (row, column) = self.position













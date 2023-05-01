import pygame
class piece :
    def __init__(self,color,type):
        self.color =color
        self.type=type
        self.position = 0,0
        self.possible_moves_list = []





class Pawn(piece):
    def __init__(self, color,name):
        super().__init__(color, 'pawn')
        self.name = name

class Bishop(piece):
    def __init__(self, color,name):
        super().__init__(color, 'bishop')
        self.name=name

class Knight(piece):
    def __init__(self, color,name):
        super().__init__(color, 'knight')
        self.name=name

class King(piece):
    def __init__(self, color,name):
        super().__init__(color, 'king')
        self.name=name

class Queen(piece):
    def __init__(self, color,name):
        super().__init__(color, 'queen')
        self.name=name


class Rook(piece):
    def __init__(self, color,name):
        super().__init__(color,'rook')
        self.name=name



def possible_moves(self, board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if (board[row][column] == None):
                free = row, column
                self.possible_moves_list.append(free)








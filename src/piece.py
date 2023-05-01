import pygame
class piece :
    def __init__(self,color,type):
     self.color =color
     self.type=type


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




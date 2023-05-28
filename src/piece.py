import pygame


class piece:
    def __init__(self, color, type, point):
        self.color = color
        self.type = type
        self.position = (0, 0)
        self.possible_moves_list = []
        self.point = point



class Pawn(piece):
    def __init__(self, color, name,position):
        super().__init__(color, 'pawn', 1)
        self.name = name
        self.position = position
        self.played = False
        self.PST_white =  [[ 0,  0,  0,  0,  0,  0,  0,  0],
                     [50, 50, 50, 50, 50, 50, 50, 50],
                     [10, 10, 20, 30, 30, 20, 10, 10],
                     [ 5,  5, 10, 27, 27, 10,  5,  5],
                     [ 0,  0,  0, 25, 25,  0,  0,  0],
                     [ 5, -5,-10,  0,  0,-10, -5,  5],
                       [ 5, 10, 10,-25,-25, 10, 10,  5],
                      [ 0,  0,  0,  0,  0,  0,  0,  0]]

        self.PST_black = [[ 0,  0,  0,  0,  0,  0,  0,  0],
                          [ -5, -10, -10,25,25, -10, -10,  -5],
                          [-5, 5, 10, 0, 0, 10, 5, 5],
                          [0, 0, 0, -25, -25, 0, 0, 0],
                          [-5, -5, -10, -27, -27, -10, -5, -5],
                          [-10, -10, -20, -30, -30, -20, -10, -10],
                          [-50, -50, -50, -50, -50, -50, -50, -50],
                          [0, 0, 0, 0, 0, 0, 0, 0]]



    def possible_moves_pawn(self, board):

        # moves_of_Pawn = []
        (row, column) = self.position
        if row == 1 and self.color == 'black':
            (row, column) = self.position
            if board[row + 1][column] == None and board[row + 2][column] == None:
                self.possible_moves_list.append((row + 1, column))
                self.possible_moves_list.append((row + 2, column))
            elif board[row + 1][column] == None and board[row + 2][column] != None:
                self.possible_moves_list.append((row + 1, column))

            if column + 1 <= 7:
                if board[row + 1][column + 1] != None:
                    self.possible_moves_list.append((row + 1, column + 1))
            if column - 1 >= 0:
                if board[row + 1][column - 1] != None:
                    self.possible_moves_list.append((row + 1, column - 1))

        elif (self.color == 'black'):
            (row, column) = self.position
            if row + 1 <= 7:
                if board[row + 1][column] == None:
                    self.possible_moves_list.append((row + 1, column))
                if column + 1 <= 7:
                    if board[row + 1][column + 1] != None:
                        self.possible_moves_list.append((row + 1, column + 1))
                if column - 1 >= 0:
                    if board[row + 1][column - 1] != None:
                        self.possible_moves_list.append((row + 1, column - 1))

        elif (row == 6 and self.color == 'white'):
            (row, column) = self.position

            if board[row - 1][column] == None and board[row - 2][column] == None:
                self.possible_moves_list.append((row - 1, column))
                self.possible_moves_list.append((row - 2, column))
            elif board[row - 1][column] == None and board[row - 2][column] != None:
                self.possible_moves_list.append((row - 1, column))

            if column + 1 <= 7:
                if board[row - 1][column + 1] != None:
                    self.possible_moves_list.append((row - 1, column + 1))
            if column - 1 >= 0:
                if board[row - 1][column - 1] != None:
                    self.possible_moves_list.append((row - 1, column - 1))

        elif (self.color == 'white'):
            (row, column) = self.position
            if row - 1 >= 0:
                if board[row - 1][column] == None:
                    self.possible_moves_list.append((row - 1, column))
                if column + 1 <= 7:
                    if board[row - 1][column + 1] != None:
                        self.possible_moves_list.append((row - 1, column + 1))
                if column - 1 >= 0:
                    if board[row - 1][column - 1] != None:
                        self.possible_moves_list.append((row - 1, column - 1))

    def clear_list(self):
        self.possible_moves_list.clear()


class Bishop(piece):
    def __init__(self, color, name,position):
        super().__init__(color, 'bishop', 3)
        self.name = name
        self.position = position
        self.played = False
        self.PST_white = [[-10, -10, -10, -10, -10, -10, -10, -10],
                          [-10, 10, 0,0, 0, 0, 10, -10],
                          [-10, 0, 0, 0, 0, 10, 0, -10],
                          [-10, 0, 10, 10, 10, 10, 0, -10],
                          [-10, 0, 10, 7, 7, 10, 0, -10],
                          [-10, 0, 10, 7, 7, 10, 0, -10],
                          [-10, 5, 10, 10, 10, 10, 5, -10],
                          [-10, -10, -10, -10, -10, -10, -10, -10]]
        self.PST_black = [
            [10, 10, 10, 10, 10, 10, 10, 10],
            [10, -10, 0, 0, 0, 0, -10, 10],
            [10, 0, 0, 0, 0, -10, 0, 10],
            [10, 0, -10, -10, -10, -10, 0, 10],
            [10, 0, -10, -7, -7, -10, 0, 10],
            [10, 0, -10, -7, -7, -10, 0, 10],
            [10, -5, -10, -10, -10, -10, -5, 10],
            [10, 10, 10, 10, 10, 10, 10, 10]
        ]

    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_bishop(self, board):
        (row, column) = self.position

        while row > 0 and column < 7:  # right top
            row -= 1
            column += 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position

        while row < 7 and column > 0:  # sol asagi
            row += 1
            column -= 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position

        while row > 0 and column > 0:  # sol yukari
            row -= 1
            column -= 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position

        while row < 7 and column < 7:  # sag asagi
            row += 1
            column += 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position


class Knight(piece):
    def __init__(self, color, name,position):
        super().__init__(color, 'knight', 3)
        self.name = name
        self.position = position
        self.played = False
        self.PST_white = [[-50, -10, -10, -10, -10, -10, -10, -50],
                          [-40, -10, 0, 5, 5, 0, -10, -40],
                          [-25, 5, 5, 0, 0, 10, 5, -25],
                          [-25, 10, 10, 10, 10, 10, 5, -25],
                          [-25, 0, 10, 15, 15, 10, 5, -25],
                          [-25, 10, 10, 15, 15, 10, 10, -25],
                          [-40, -20, 0, 5, 5, 0, -20, -40],
                          [-50, -10, -10, -10, -10, -10, -10, -50]]
        self.PST_black = [
            [50, 10, 10, 10, 10, 10, 10, 50],
            [40, 20, 0, -5, -5, 0, 10, 40],
            [25, -5, -5, 0, 0, -10, -5, 25],
            [25, -10, -10, -10, -10, -10, -5, 25],
            [25, 0, -10, -15, -15, -10, -5, 25],
            [25, -10, -10, -15, -15, -10, -10, 25],
            [40, 10, 0, -5, -5, 0, 10, 40],
            [50, 10, 10, 10, 10, 10, 10, 50]
        ]

    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_knight(self, board):
        (row, column) = self.position

        if row - 2 >= 0 and row - 2 <= 7 and column + 1 >= 0 and column + 1 <= 7:
            self.possible_moves_list.append((row - 2, column + 1))

        if row - 1 >= 0 and row - 1 <= 7 and column + 2 >= 0 and column + 2 <= 7:
            self.possible_moves_list.append((row - 1, column + 2))

        if row + 1 >= 0 and row + 1 <= 7 and column + 2 >= 0 and column + 2 <= 7:
            self.possible_moves_list.append((row + 1, column + 2))

        if row + 2 >= 0 and row + 2 <= 7 and column + 1 >= 0 and column + 1 <= 7:
            self.possible_moves_list.append((row + 2, column + 1))

        if row - 2 >= 0 and row - 2 <= 7 and column - 1 >= 0 and column - 1 <= 7:
            self.possible_moves_list.append((row - 2, column - 1))

        if row - 1 >= 0 and row - 1 <= 7 and column - 2 >= 0 and column - 2 <= 7:
            self.possible_moves_list.append((row - 1, column - 2))

        if row + 2 >= 0 and row + 2 <= 7 and column - 1 >= 0 and column - 1 <= 7:
            self.possible_moves_list.append((row + 2, column - 1))

        if row + 1 >= 0 and row + 1 <= 7 and column - 2 >= 0 and column - 2 <= 7:
            self.possible_moves_list.append((row + 1, column - 2))


class King(piece):
    def __init__(self, color, name,position):
        super().__init__(color, 'king', 10)
        self.name = name
        self.position = position
        self.king_moved = False
        self.played = False
        self.PST_white = [
            [-40, -40, -40, -50, -50, -40, -40, -40],
            [-40, -40, -30, -30, -50, -40, -40, -40],
            [-40, -40, -30, -30, -30, -40, -40, -40],
            [-30, -40, 0, 1000, 1000, 0, -40, -30],
            [-30, -30, 0, 1000, 1000, 0, -30, -30],
              [-10, -10, 5, 10, 10, 5, -10, -10],
               [-5, -5, 0, 10, 10, 0, -5, -5],
               [0, 5, 10, 10, 10, 10, 5, 0]
        ]
        self.PST_black =[[0, -5, -10, -10, -10, -10, -5, 0],
                         [5, 5, 0, -10, -10, 0, 5, 5],
                         [10, 10, -5, -10, -10, -5, 10, 10],
                         [30, 30, 0, -1000, -1000, 0, 30, 30],
                         [30, 40, 0, -1000, -1000, 0, 40, 30],
                         [40, 40, 30, 30, 30, 40, 40, 40],
                         [40, 40, 30, 30, 50, 40, 40, 40],
                         [40, 40, 40, 50, 50, 40, 40, 40],]
    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_king(self, board,brd):
        (row, column) = self.position

        (right, left) = brd.castling_checked(self.position)
        if right == True:
            self.possible_moves_list.append((row, column + 2))
            #print((row, column + 2), "GİRDİİİİİ ZAAA")
            #print(self.possible_moves_list)
            #print("----------")
        if left == True:
            self.possible_moves_list.append((row, column - 3))




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
    def __init__(self, color, name,position):
        super().__init__(color, 'queen', 9)
        self.name = name
        self.position = position
        self.played =False
        self.PST_white= [ [ -20, -10, -10, -5, -5, -10, -10, -20,],
          [-10, 0, 0, 0, 0, 0, 0, -10,],
          [-10, 0, 5, 5, 5, 5, 0, -10,],
          [-5, 0, 5, 5, 5, 5, 0, -5,],
          [ 0, 0, 5, 5, 5, 5, 0, -5,],
        [-10, 5, 5, 5, 5, 5, 0, -10,],
        [-10, 0, 5, 0, 0, 0, 0, -10,],
        [-20, -10, -10, -5, -5, -10, -10, -20]]

        self.PST_black = [
            [20, 10, 10, 5, 5, 10, 10, 20],
            [10, 0, 0, 0, 0, 0, 0, 10],
            [10, 0, -5, -5, -5, -5, 0, 10],
            [5, 0, -5, -5, -5, -5, 0, 5],
            [0, 0, -5, -5, -5, -5, 0, 5],
            [10, -5, -5, -5, -5, -5, 0, 10],
            [10, 0, -5, 0, 0, 0, 0, 10],
            [20, 10, 10, 5, 5, 10, 10, 20]
        ]

    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_queen(self, board):
        (row, column) = self.position

        for i in range(column + 1, len(board[0])):
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color == self.color:
                break
            elif board[row][i].color != self.color:
                self.possible_moves_list.append((row, i))
                break

            # Check moves to the left
        for i in range(column - 1, -1, -1):
            # if board[row][i] is None:  # empty square
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color == self.color:
                break
            elif board[row][i].color != self.color:
                self.possible_moves_list.append((row, i))
                break

            # Check moves down
        for i in range(row + 1, len(board)):
            # if board[i][column] is None:  # empty square
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color == self.color:
                break
            elif board[i][column].color != self.color:
                self.possible_moves_list.append((i, column))
                break

            # Check moves up
        for i in range(row - 1, -1, -1):
            # if board[i][column] is None:  # empty square
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color == self.color:
                break
            elif board[i][column].color != self.color:
                self.possible_moves_list.append((i, column))
                break

        (row, column) = self.position

        while row > 0 and column < 7:  # right top
            row -= 1
            column += 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position

        while row < 7 and column > 0:  # sol asagi
            row += 1
            column -= 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position

        while row > 0 and column > 0:  # sol yukari
            row -= 1
            column -= 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position

        while row < 7 and column < 7:  # sag asagi
            row += 1
            column += 1
            if board[row][column] == None:
                self.possible_moves_list.append((row, column))
            elif board[row][column] != None and self.color != board[row][column].color:
                self.possible_moves_list.append((row, column))
                break
            else:
                break

        (row, column) = self.position


class Rook(piece):
    def __init__(self, color, name,position):
        super().__init__(color, 'rook', 5)
        self.name = name
        self.position = position
        self.rook_moved = False
        self.played =False
        self.PST_white = [[-5, 0, 0, 0, 0, 0, 0, -5],
                          [5, 5, 5, 10, 10, 5, 5, 5],
                          [-5, 0, 5, 5, 5, 0, 0, -5],
                          [2.5, 5, 5, 1, 1, 5, 5, 2.5],
                          [2.5, 5, 5, 1, 1, 5, 5, 2.5],
                          [-5, 0, 0, 5, 5, 0, 0, -5],
                          [-5, 0, 0, 5, 5, 0, 0, -5],
                          [0, 0, 0, 5, 5, 0, 0, 0]]
        self.PST_black = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [5, 0, 0, -5, -5, 0, 0, 5],
                          [5, 0, 5, -5, -5, 0, 0, -5],
                          [-2.5, -5, -5, -1, -1, -5, -5, -2.5],
                          [-2.5, -5, -5, -1, -1, -5, -5, -2.5],
                          [5, 0, 0, -5, -5, 0, 0, 5],
                          [-5, -5, -5, -10, -10, -5, -5, -5],
                           [5, 0, 0, 0, 0, 0, 0, 5]]

    def clear_list(self):
        self.possible_moves_list.clear()

    def possible_moves_rook(self, board):
        (row, column) = self.position

        for i in range(column + 1, len(board[0])):
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color == self.color:
                break
            elif board[row][i].color != self.color:
                self.possible_moves_list.append((row, i))
                break

            # Check moves to the left
        for i in range(column - 1, -1, -1):
            # if board[row][i] is None:  # empty square
            if board[row][i] is None:  # empty square
                self.possible_moves_list.append((row, i))
            elif board[row][i].color == self.color:
                break
            elif board[row][i].color != self.color:
                self.possible_moves_list.append((row, i))
                break

            # Check moves down
        for i in range(row + 1, len(board)):
            # if board[i][column] is None:  # empty square
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color == self.color:
                break
            elif board[i][column].color != self.color:
                self.possible_moves_list.append((i, column))
                break

            # Check moves up
        for i in range(row - 1, -1, -1):
            # if board[i][column] is None:  # empty square
            if board[i][column] is None:  # empty square
                self.possible_moves_list.append((i, column))
            elif board[i][column].color == self.color:
                break
            elif board[i][column].color != self.color:
                self.possible_moves_list.append((i, column))
                break




































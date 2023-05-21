import timeit
import time
import matplotlib.pyplot as plt
import numpy as np
from board import board
from aibot import randomizer
from tests import FENtoBoard


def zug_generator_starting():
    color = 'white'
    boardd = board()
    boardd.positions()
    list_of_possible_moves = []
    moves = boardd.legalMoves()
    for row in range(8):
        for col in range(8):
            piece = boardd.board[row][col]
            if piece != None and piece.color == color:
                legal_moves = moves[(row, col)]
                #print("Piece in pos:", row, col, " has legal moves:", legal_moves)
                while len(legal_moves) != 0:
                    move = legal_moves.pop()
                    possible_move = ((row, col), move)
                    list_of_possible_moves.append(possible_move)

    move = randomizer(list_of_possible_moves)
def zug_generator_middle():
    boardmiddle = board()
    boardmid, color, k1, k2, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    #print(boardmid, color)
    boardmiddle.board = boardmid
    boardmiddle.boardInteger = np.array(hilfsboard)
    boardmiddle.positions()
    list_of_possible_moves = []
    moves = boardmiddle.legalMoves()
    #print(moves)
    for row in range(8):
        for col in range(8):
            piece = boardmiddle.board[row][col]
            if piece != None and piece.color == color:
                legal_moves = moves[(row, col)]
                #print("Piece in pos:", row, col, " has legal moves:", legal_moves)
                while len(legal_moves) != 0:
                    move = legal_moves.pop()
                    possible_move = ((row, col), move)
                    list_of_possible_moves.append(possible_move)

    move = randomizer(list_of_possible_moves)

def zug_generator_end():
    boardend = board()
    boardend_d, color, k1, k2, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("r1b1k1nr/1pp2ppp/p1p5/2b1p3/P3P3/2N2PP1/1PPP3q/R1B1KQ2 w Qkq - 0 11")
    #print(boardmid, color)
    boardend.board = boardend_d
    boardend.boardInteger = np.array(hilfsboard)
    boardend.positions()
    list_of_possible_moves = []
    moves = boardend.legalMoves()
    #print(moves)
    for row in range(8):
        for col in range(8):
            piece = boardend.board[row][col]
            if piece != None and piece.color == color:
                legal_moves = moves[(row, col)]
                #print("Piece in pos:", row, col, " has legal moves:", legal_moves)
                while len(legal_moves) != 0:
                    move = legal_moves.pop()
                    possible_move = ((row, col), move)
                    list_of_possible_moves.append(possible_move)

    move = randomizer(list_of_possible_moves)


#(timeit.timeit(stmt='', setup='', timer=time.perf_counter, number=1, globals=None))
array1 = (timeit.repeat(stmt='zug_generator_starting()', setup='from __main__ import zug_generator_starting', repeat=5, number=1))
array4 = (timeit.repeat(stmt='zug_generator_starting()', setup='from __main__ import zug_generator_starting', repeat=1000, number=1))
array2 = (timeit.repeat(stmt='zug_generator_middle()', setup='from __main__ import zug_generator_middle', repeat=1000, number=1))
array3 = timeit.repeat(stmt='zug_generator_end()', setup='from __main__ import zug_generator_end', repeat=1000, number=1)
x = range(1, 1001)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, array4)
axs[0, 0].set_title('Starting board')
axs[0, 1].plot(x, array2, 'tab:green')
axs[0, 1].set_title('Middle board')
axs[1, 0].plot(x, array3, 'tab:red')
axs[1, 0].set_title('Near-end board')
fig.tight_layout()
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4])
plt.show()


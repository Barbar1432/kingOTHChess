import timeit
import time
import matplotlib.pyplot as plt
import numpy as np
import copy
from board import board
from aibot import randomizer
from tests import FENtoBoard

testing = 1 # 0 for Zuggenerator , 1 for MinMax - AlphaBetaSuche
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
def alpha_beta_depth1():
    a_b_board_1 = board()
    board_d, color, kwhite, kblack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (enPassentSquareRow, enPassentSquareCol), \
    halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    a_b_board_1.board = board_d
    a_b_board_1.boardInteger = np.array(hilfsboard)
    a_b_board_1.positions()
    a_b_board_1.blackKing = kblack
    if kblack.position != (0, 4):
        a_b_board_1.blackKing.king_moved = True
    a_b_board_1.whiteKing = kwhite
    if kwhite.position != (7, 4):
        a_b_board_1.whiteKing.king_moved = True
    if color == 'black':
        a_b_board_1.Anzahlmoves += 1
    if color == 'white':
        a_b_board_1.botplaying = (False,'white')
    bewertung, path, k = alpha_beta(a_b_board_1, 1, float('-inf'), float('inf'),True)
    move = path[0]

    print("AlphaBeta depth 1 untersuchter Zustände: ", k)

def alpha_beta_depth2():
    a_b_board_2 = board()
    board_d, color, kwhite, kblack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    a_b_board_2.board = board_d
    a_b_board_2.boardInteger = np.array(hilfsboard)
    a_b_board_2.positions()
    a_b_board_2.blackKing = kblack
    if kblack.position != (0, 4):
        a_b_board_2.blackKing.king_moved = True
    a_b_board_2.whiteKing = kwhite
    if kwhite.position != (7, 4):
        a_b_board_2.whiteKing.king_moved = True
    if color == 'black':
        a_b_board_2.Anzahlmoves += 1
    if color == 'white':
        a_b_board_2.botplaying = (False,'white')
    bewertung, path, k = alpha_beta(a_b_board_2, 2, float('-inf'), float('inf'), True)
    move = path[0]
    print("AlphaBeta depth 2 untersuchter Zustände: ", k)
def alpha_beta_depth3():
    a_b_board_3 = board()
    board_d, color, kwhite, kblack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    a_b_board_3.board = board_d
    a_b_board_3.boardInteger = np.array(hilfsboard)
    a_b_board_3.positions()
    a_b_board_3.blackKing = kblack
    if kblack.position != (0, 4):
        a_b_board_3.blackKing.king_moved = True
    a_b_board_3.whiteKing = kwhite
    if kwhite.position != (7, 4):
        a_b_board_3.whiteKing.king_moved = True
    if color == 'black':
        a_b_board_3.Anzahlmoves += 1
    if color == 'white':
        a_b_board_3.botplaying = (False,'white')
    bewertung, path, k = alpha_beta(a_b_board_3, 3, float('-inf'), float('inf'), True)
    move = path[0]
    print("AlphaBeta depth 3 untersuchter Zustände: ", k)

def mini_max_depth1():
    min_max_board = board()
    board_d, color, kwhite, kblack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    min_max_board.board = board_d
    min_max_board.boardInteger = np.array(hilfsboard)
    min_max_board.positions()
    min_max_board.blackKing = kblack
    if kblack.position != (0, 4):
        min_max_board.blackKing.king_moved = True
    min_max_board.whiteKing = kwhite
    if kwhite.position != (7, 4):
        min_max_board.whiteKing.king_moved = True
    if color == 'black':
        min_max_board.Anzahlmoves += 1
    if color == 'white':
        min_max_board.botplaying = (False,'white')
    bewertung, path, k = min_max(min_max_board, 1, float('-inf'), float('inf'), True)
    print("Minmax depth 1 untersuchter Zustände: ", k)
    move = path[0]
def mini_max_depth2():
    min_max_board_2 = board()
    board_d, color, kwhite, kblack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    min_max_board_2.board = board_d
    min_max_board_2.boardInteger = np.array(hilfsboard)
    min_max_board_2.positions()
    min_max_board_2.blackKing = kblack
    if kblack.position != (0, 4):
        min_max_board_2.blackKing.king_moved = True
    min_max_board_2.whiteKing = kwhite
    if kwhite.position != (7, 4):
        min_max_board_2.whiteKing.king_moved = True
    if color == 'black':
        min_max_board_2.Anzahlmoves += 1
    if color == 'white':
        min_max_board_2.botplaying = (False,'white')
    bewertung, path, k = min_max(min_max_board_2, 2, float('-inf'), float('inf'), True)
    move = path[0]
    print("Minmax depth 2 untersuchter Zustände: ", k)
def mini_max_depth3():
    min_max_board_3 = board()
    board_d, color, kwhite, kblack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, (
    enPassentSquareRow, enPassentSquareCol), \
        halfMoveClock, fullMoveClock, hilfsboard = FENtoBoard("4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22")
    min_max_board_3.board = board_d
    min_max_board_3.boardInteger = np.array(hilfsboard)
    min_max_board_3.positions()
    min_max_board_3.blackKing = kblack
    if kblack.position != (0, 4):
        min_max_board_3.blackKing.king_moved = True
    min_max_board_3.whiteKing = kwhite
    if kwhite.position != (7, 4):
        min_max_board_3.whiteKing.king_moved = True
    if color == 'black':
        min_max_board_3.Anzahlmoves += 1
    if color == 'white':
        min_max_board_3.botplaying = (False,'white')
    bewertung, path, k = min_max(min_max_board_3, 3, float('-inf'), float('inf'), True)
    move = path[0]
    print("Minmax depth 3 untersuchter Zustände: ", k)

def generate_mini_boards(board):
    board_list = []
    list_of_possible_moves = []
    moves = board.legalMoves()
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece != None and board.Anzahlmoves % 2 == 0 and piece.color == 'white':
                legal_moves = moves[(row, col)]
                # print("Piece in pos:", row, col, " has legal moves:", legal_moves)
                while len(legal_moves) != 0:
                    move = legal_moves.pop()
                    possible_move = ((row, col), move)
                    list_of_possible_moves.append(possible_move)
                    board_list.append(copy.deepcopy(board))
            elif piece != None and board.Anzahlmoves % 2 == 1 and piece.color == 'black':
                legal_moves = moves[(row, col)]
                # print("Piece in pos:", row, col, " has legal moves:", legal_moves)
                while len(legal_moves) != 0:
                    move = legal_moves.pop()
                    possible_move = ((row, col), move)
                    list_of_possible_moves.append(possible_move)
                    board_list.append(copy.deepcopy(board))
    i = 0
    for pos_moves in list_of_possible_moves:
        sq, des = pos_moves
        board_list[i].moveZa(sq, des)
        i += 1
    return board_list
def min_max(node, depth, alpha, beta, is_max, k=0, path=[]):
    k += 1
    if depth == 0 or isTerminal(node):
        return node.bewertungsFunktion(), path, k
    if is_max:
        best_value = alpha
        best_path = None
        for child in generate_mini_boards(node):
            # print("At child:", child.boardInteger)
            value, child_path, k = min_max(child, depth - 1, best_value, beta, False, k, path + [child])
            if value > best_value:
                best_value = value
                best_path = child_path
        return best_value, best_path, k
    else:
        best_value = beta
        best_path = None
        for child in generate_mini_boards(node):
            # print("At child:", child.boardInteger)
            value, child_path, k = min_max(child, depth - 1, alpha, best_value, True, k, path + [child])
            if value < best_value:
                best_value = value
                best_path = child_path
        return best_value, best_path, k
def alpha_beta(node, depth, alpha, beta, is_max, k=0, path=[]):
    k += 1
    if depth == 0 or isTerminal(node):
        return node.bewertungsFunktion(), path, k
    if is_max:
        best_value = alpha
        best_path = None
        for child in generate_mini_boards(node):
            # print("At child:", child.boardInteger)
            value, child_path, k = alpha_beta(child, depth - 1, best_value, beta, False, k, path + [child])
            if value > best_value:
                best_value = value
                best_path = child_path
            if best_value >= beta:  # Beta-Cutoff
                #print("BetaCutoff!")
                break
        return best_value, best_path, k
    else:
        best_value = beta
        best_path = None
        for child in generate_mini_boards(node):
            # print("At child:", child.boardInteger)
            value, child_path, k = alpha_beta(child, depth - 1, alpha, best_value, True, k, path + [child])
            if value < best_value:
                best_value = value
                best_path = child_path
            if best_value <= alpha:  # Alpha-Cutoff
                #print("AlphaCutoff!")
                break
        return best_value, best_path, k

def isTerminal(b_board):
    # TODO: If no more possible moves - Stalemate
    if b_board.finished:
        return True

if (testing == 0):
    array1 = (
        timeit.repeat(stmt='zug_generator_starting()', setup='from __main__ import zug_generator_starting', repeat=5,
                      number=1))
    array4 = (
        timeit.repeat(stmt='zug_generator_starting()', setup='from __main__ import zug_generator_starting', repeat=1000,
                      number=1))
    array2 = (
        timeit.repeat(stmt='zug_generator_middle()', setup='from __main__ import zug_generator_middle', repeat=1000,
                      number=1))
    array3 = timeit.repeat(stmt='zug_generator_end()', setup='from __main__ import zug_generator_end', repeat=1000,
                           number=1)
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


#(timeit.timeit(stmt='', setup='', timer=time.perf_counter, number=1, globals=None))
elif testing == 1:
    array4 = (
        timeit.repeat(stmt='alpha_beta_depth1()', setup='from __main__ import alpha_beta_depth1', repeat=5, number=1))
    array11 = (
        timeit.repeat(stmt='mini_max_depth1()', setup='from __main__ import mini_max_depth1', repeat=10, number=1))
    array1 = (
        timeit.repeat(stmt='alpha_beta_depth1()', setup='from __main__ import alpha_beta_depth1', repeat=10, number=1))
    array22 = (
        timeit.repeat(stmt='mini_max_depth2()', setup='from __main__ import mini_max_depth2', repeat=10, number=1))
    array2 = (
        timeit.repeat(stmt='alpha_beta_depth2()', setup='from __main__ import alpha_beta_depth2', repeat=10, number=1))

    array33 = (
        timeit.repeat(stmt='mini_max_depth3()', setup='from __main__ import mini_max_depth3', repeat=10, number=1))
    array3 = (
        timeit.repeat(stmt='alpha_beta_depth3()', setup='from __main__ import alpha_beta_depth3', repeat=10, number=1))

    x = range(1, 11)
    fig, axs = plt.subplots(3, 2)
    axs[0, 0].plot(x, array11, 'tab:blue')
    axs[0, 0].set_title('MinMax with Depth: 1')
    axs[0, 0].set_ylabel('time (s)')
    axs[0, 1].plot(x, array1, 'tab:cyan')
    axs[0, 1].set_title('AlphaBeta with Depth: 1')
    axs[1, 0].plot(x, array22, 'tab:red')
    axs[1, 0].set_title('MinMax with Depth: 2')
    axs[1, 0].set_ylabel('time (s)')
    axs[1, 1].plot(x, array2, 'tab:orange')
    axs[1, 1].set_title('AlphaBeta with Depth: 2')
    axs[2, 0].plot(x, array33, 'tab:purple')
    axs[2, 0].set_title('MinMax with Depth: 3')
    axs[2, 0].set_ylabel('time (s)')
    axs[2, 0].set_xlabel('repeat (n)')
    axs[2, 1].plot(x, array3, 'tab:pink')
    axs[2, 1].set_title('AlphaBeta with Depth: 3')
    axs[2, 1].set_xlabel('repeat(n)')
    fig.tight_layout()
    plt.show()
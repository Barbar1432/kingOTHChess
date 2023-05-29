import pygame
from piece import Rook, Knight, Bishop, Queen, King, Pawn
import random
import copy


def randomizer(moves_list):
    return random.choice(moves_list)


class bot:
    def __init__(self):

        self.ai_bool = False # AI-Bot active bool
        self.color = 'black'  # Make sure to decide the bots color beforehand

    def random_move(self, ai_bool, board):
        if ai_bool:  # AI-Bot is active
            bewertung, path = alpha_beta(board, 3, float('-inf'), float('inf'), True)
            move = path[0].lastmove
            print(move)
            sq, dest = move
            board.moveZa(sq, dest)

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

def alpha_beta(node, depth, alpha, beta, is_max, path=[]):
    if depth == 0 or isTerminal(node):
        return node.bewertungsFunktion(), path
    if is_max:
        best_value = alpha
        best_path = None
        for child in generate_mini_boards(node):
            # print("At child:", child.boardInteger)
            value, child_path = alpha_beta(child, depth - 1, best_value, beta, False, path + [child])
            if value > best_value:
                best_value = value
                best_path = child_path
            if best_value >= beta:  # Beta-Cutoff
                # print("BetaCutoff!")
                break
        return best_value, best_path
    else:
        best_value = beta
        best_path = None
        for child in generate_mini_boards(node):
            # print("At child:", child.boardInteger)
            value, child_path = alpha_beta(child, depth - 1, alpha, best_value, True, path + [child])
            if value < best_value:
                best_value = value
                best_path = child_path
            if best_value <= alpha:  # Alpha-Cutoff
                # print("AlphaCutoff!")
                break
        return best_value, best_path

def isTerminal(b_board):
    # TODO: If no more possible moves - Stalemate
    if b_board.finished:
        return True


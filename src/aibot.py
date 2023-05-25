import pygame
from piece import Rook, Knight, Bishop, Queen, King, Pawn
import random


def randomizer(moves_list):
    return random.choice(moves_list)


class bot:
    def __init__(self):
        self.ai_bool = False # AI-Bot active bool
        self.color = 'black'  # Make sure to decide the bots color beforehand


    def random_move(self, ai_bool, board):
        if ai_bool:  # AI-Bot is active
            list_of_possible_moves = []
            moves = board.legalMoves()
            for row in range(8):
                for col in range(8):
                    piece = board.board[row][col]
                    if piece != None and piece.color == self.color:
                        legal_moves = moves[(row,col)]
                        print("Piece in pos:", row, col, " has legal moves:", legal_moves)
                        while len(legal_moves) != 0:
                            move = legal_moves.pop()
                            possible_move = ((row,col),move)
                            list_of_possible_moves.append(possible_move)

            if len(list_of_possible_moves) != 0:
                if board.finished is False:
                    move = randomizer(list_of_possible_moves)
                    print("I choose you pikachu:", move)
                    sq, dest = move
                    board.moveZa(sq, dest)
                else:
                    board.finished = True
                    board.Anzahlmoves += 1
                    print("No more possible moves")
            else:
                board.finished = True
                board.Anzahlmoves += 1
                print("No more possible moves")



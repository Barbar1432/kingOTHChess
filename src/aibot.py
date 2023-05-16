import pygame
from piece import Rook, Knight, Bishop, Queen, King, Pawn
import random


def randomizer(moves_list):
    return random.choice(moves_list)


class bot:
    def __init__(self):
        self.ai_bool = True  # AI-Bot active bool
        self.color = ()  # Make sure to decide the bots color beforehand


    def random_move(self, ai_bool, board):
        if ai_bool:  # AI-Bot is active
            list_of_possible_moves = []
            for row in range(8):
                for col in range(8):
                    piece = board.board[row][col]
                    if piece != None and piece.color == self.color:
                        # Collect all possible moves
                        if isinstance(piece, Pawn):
                            piece.possible_moves_pawn(board.board)
                        elif isinstance(piece, King):
                            piece.possible_moves_king(board.board)
                        elif isinstance(piece, Knight):
                            piece.possible_moves_knight(board.board)
                        elif isinstance(piece, Bishop):
                            piece.possible_moves_bishop(board.board)
                        elif isinstance(piece, Rook):
                            piece.possible_moves_rook(board.board)
                        elif isinstance(piece, Queen):
                            piece.possible_moves_queen(board.board)
                        while(len(piece.possible_moves_list)!=0):
                            dest = piece.possible_moves_list.pop()
                            piece_and_its_move = ((row, col), dest)  # Create a tuple as: ((Current Pos),(Destination))
                            list_of_possible_moves.append(piece_and_its_move)
            if(len(list_of_possible_moves)!=0):
                #TODO: isLegal
                legal_list = []
                #while(len(list_of_possible_moves)!=0):
                #    pos1, pos2 = list_of_possible_moves.pop()
                #    print(pos1,pos2,"isLegal==",board.isLegal(pos1,pos2))
                #    if board.isLegal(pos1, pos2):
                #        legal_list.append((pos1, pos2))
                #print("Legal list:", legal_list)
                #move = randomizer(legal_list)
                move = randomizer(list_of_possible_moves)
                print("I choose you pikachu:", move)
                sq, dest = move
                board.move(sq, dest)


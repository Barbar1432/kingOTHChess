import unittest
import numpy as np
import copy
import piece
#import main
import visuals
import timeit
from board import board
from piece import Rook, Knight, Bishop, Queen, King,Pawn

# TODO: UNIT TESTS
class TestBoard(unittest.TestCase):

    """

    def test_mini_board(self):
        b_board = board()
        b_board.positions()
        b_board.screen = ()
        list_of_boards = generate_mini_boards(b_board)
        i = 0
        for boards in list_of_boards:
            print("Board ", i, "= \n", boards.boardInteger)
            i += 1
    """

    def test_alpha_beta_suche(self):
        b_board = board()
        b_board.screen = ()
        #Testing
        t_board = testingBoard("A", 1, "r2q1rk1/pp2ppbp/2np1np1/8/2PP4/2N1PN2/PPQ2PPP/R1B1K2R b KQ - 4 8", 12)
        b_board.board = t_board.board
        b_board.boardInteger = np.array(t_board.hilfsboard)
        b_board.positions()
        b_board.blackKing = t_board.kingBlack
        if t_board.kingBlack.position != (0, 4):
            b_board.blackKing.king_moved = True
        b_board.whiteKing = t_board.kingWhite
        if t_board.kingWhite.position != (7, 4):
            b_board.whiteKing.king_moved = True
        if t_board.color == 'black':
            b_board.Anzahlmoves += 1
        value, path = alpha_beta(b_board, 3, float('-inf'), float('inf'), True)
        print("Bewertungsfunktion ergibt = ", value)
        i = 0
        print("Current Board:", i)
        chessBoardVisualize(b_board.boardInteger)
        print("\n")
        print("Expected path for the best outcome: \n")
        i = 1
        for boards in path:
            print("Move:", i)
            chessBoardVisualize(boards.boardInteger)
            print("\n")
            i += 1
    """
    def test_deneme(self):
        t_board = testingBoard("deneme",-1,"2r4r/8/8/4k3/8/R7/8/4K2R w - - 0 1", -2)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        print(legal_moves)
    """
    def test_Fricke(self):
        #print(FENtoBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq b3 1 0"))
        boardd, stell, fen, moves = allBoards()[0]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)
    def test_A_1(self):
        boardd, stell, fen, moves = allBoards()[1]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)
    def test_A_2(self):
        boardd, stell, fen, moves = allBoards()[2]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_N_1(self):
        boardd, stell, fen, moves = allBoards()[3]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_N_2(self):
        boardd, stell, fen, moves = allBoards()[4]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_L_1(self):
        boardd, stell, fen, moves = allBoards()[5]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_L_2(self):
        boardd, stell, fen, moves = allBoards()[6]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_G_1(self):
        boardd, stell, fen, moves = allBoards()[7]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_G_2(self):
        boardd, stell, fen, moves = allBoards()[8]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_O_1(self):
        boardd, stell, fen, moves = allBoards()[9]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_O_2(self):
        boardd, stell, fen, moves = allBoards()[10]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_J_1(self):
        boardd, stell, fen, moves = allBoards()[11]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_J_2(self):
        boardd, stell, fen, moves = allBoards()[12]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_H_1(self):
        boardd, stell, fen, moves = allBoards()[13]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_H_2(self):
        boardd, stell, fen, moves = allBoards()[14]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AA_1(self):
        boardd, stell, fen, moves = allBoards()[15]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AA_2(self):
        boardd, stell, fen, moves = allBoards()[16]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AB_1(self):
        boardd, stell, fen, moves = allBoards()[17]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AB_2(self):
        boardd, stell, fen, moves = allBoards()[18]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_S_1(self):
        boardd, stell, fen, moves = allBoards()[19]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_S_2(self):
        boardd, stell, fen, moves = allBoards()[20]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AF_1(self):
        boardd, stell, fen, moves = allBoards()[21]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AF_2(self):
        boardd, stell, fen, moves = allBoards()[22]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_R_1(self):
        boardd, stell, fen, moves = allBoards()[23]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_R_2(self):
        boardd, stell, fen, moves = allBoards()[24]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_P_1(self):
        boardd, stell, fen, moves = allBoards()[25]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_P_2(self):
        boardd, stell, fen, moves = allBoards()[26]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AH_1(self):
        boardd, stell, fen, moves = allBoards()[27]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_AH_2(self):
        boardd, stell, fen, moves = allBoards()[28]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_F_1(self):
        boardd, stell, fen, moves = allBoards()[29]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_F_2(self):
        boardd, stell, fen, moves = allBoards()[30]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_T_1(self):
        boardd, stell, fen, moves = allBoards()[31]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_T_2(self):
        boardd, stell, fen, moves = allBoards()[32]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_U_1(self):
        boardd, stell, fen, moves = allBoards()[33]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_U_2(self):
        boardd, stell, fen, moves = allBoards()[34]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_U_3(self):
        boardd, stell, fen, moves = allBoards()[35]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_U_4(self):
        boardd, stell, fen, moves = allBoards()[36]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_V_1(self):
        boardd, stell, fen, moves = allBoards()[37]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_V_2(self):
        boardd, stell, fen, moves = allBoards()[38]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_K_1(self):
        boardd, stell, fen, moves = allBoards()[39]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_K_2(self):
        boardd, stell, fen, moves = allBoards()[40]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_X_1(self):
        boardd, stell, fen, moves = allBoards()[41]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_X_2(self):
        boardd, stell, fen, moves = allBoards()[42]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_C_1(self):
        boardd, stell, fen, moves = allBoards()[43]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_C_2(self):
        boardd, stell, fen, moves = allBoards()[44]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_M_1(self):
        boardd, stell, fen, moves = allBoards()[45]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_M_2(self):
        boardd, stell, fen, moves = allBoards()[46]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_Z_1(self):
        boardd, stell, fen, moves = allBoards()[47]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

    def test_Z_2(self):
        boardd, stell, fen, moves = allBoards()[48]
        t_board = testingBoard(boardd, stell, fen, moves)
        b_board = board()
        legal_moves = returnAllMoves(b_board, t_board)
        # print(legal_moves)
        self.assertEqual(len(legal_moves), t_board.moves)

class TestAlphaBeta(unittest.TestCase):
    """def test_alpha_beta_suche(self):
        b_board = board()
        b_board.screen = ()
        # Testing
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[3]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        print("Current Board:")
        chessBoardVisualize(b_board.boardInteger)
        print("\n")
        print("First move for the best outcome in depth: ", depth, " ->", move, "\n")
        print("Expected move:", t_board.moves)
        sq, dest = move
        b_board.moveZa(sq, dest)
        chessBoardVisualize(b_board.boardInteger)
        self.assertIn(move, t_board.moves)
            """
    def test_alpha_beta_suche2(self):
        b_board = board()
        b_board.screen = ()
        # Testing
        t_board = testingBoard("A", 2, "8/2p2R2/1p2p1Np/1P5k/3nr3/8/P7/2K5 w - - 0 34", 12)
        b_board.board = t_board.board
        b_board.boardInteger = np.array(t_board.hilfsboard)
        b_board.positions()
        b_board.blackKing = t_board.kingBlack
        if t_board.kingBlack.position != (0, 4):
            b_board.blackKing.king_moved = True
        b_board.whiteKing = t_board.kingWhite
        if t_board.kingWhite.position != (7, 4):
            b_board.whiteKing.king_moved = True
        if t_board.color == 'black':
            b_board.Anzahlmoves += 1
        value, path = alpha_beta(b_board, 3, float('-inf'), float('inf'), True)
        print("Bewertungsfunktion ergibt = ", value)
        i = 0
        print("Current Board:", i)
        chessBoardVisualize(b_board.boardInteger)
        print("\n")
        print("Expected path for the best outcome: \n")
        i = 1
        for boards in path:
            print("Move:", i)
            chessBoardVisualize(boards.boardInteger)
            print(boards.lastmove)
            print("\n")
            i += 1


    #  Alpha Beta Testing
    def test_alpha_J_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[0]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_J_1_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[1]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_J_1_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[2]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_J_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[3]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_J_2_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[4]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_J_2_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[5]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_C_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[6]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_C_1_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[7]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_C_1_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[8]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_C_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[9]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_C_2_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[10]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_C_2_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[11]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_O_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[12]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_O_1_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[13]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_O_1_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[14]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_K_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[15]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_K_1_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[16]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_K_1_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[17]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_K_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[18]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_K_2_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[19]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_K_2_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[20]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AB_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[21]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AB_2_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[22]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_H_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[23]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_H_1_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[24]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_M_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[25]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_M_2_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[26]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_V_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[27]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_V_1_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[28]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_V_1_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[29]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_V_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[30]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_V_2_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[31]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_V_2_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[32]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_F_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[33]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_F_1_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[34]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_F_1_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[35]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_F_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[36]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_F_2_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[37]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_F_2_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[38]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AA_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[39]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AA_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[40]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AA_2_depth2(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[41]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AA_2_depth3(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[42]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_N_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[43]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_N_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[44]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_A_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[45]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_A_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[46]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_B_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[47]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_B_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[48]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_S_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[49]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_S_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[50]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_O_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[51]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AD_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[52]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AD_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[53]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AB_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[54]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_H_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[55]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_M_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[56]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_T_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[57]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_T_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[58]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_R_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[59]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_R_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[60]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_P_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[61]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_P_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[62]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)
        # Given wrong move !?
        # def test_alpha_X_1_depth1(self):
        #    b_board = board()
        #    b_board.screen = ()
        #    boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[63]
        #    t_board = testingBoard(boardd, stell, fen, moves)
        #    move = returnAlphaBetaMove(b_board, t_board, depth)
        #    sq, dest = move
        #    b_board.moveZa(sq, dest)
        #    self.assertIn(move, t_board.moves)
        # def test_alpha_X_2_depth1(self):
        #    b_board = board()
        #    b_board.screen = ()
        #    boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[64]
        #    t_board = testingBoard(boardd, stell, fen, moves)
        #    move = returnAlphaBetaMove(b_board, t_board, depth)
        #    sq, dest = move
        #    b_board.moveZa(sq, dest)
        #    self.assertIn(move, t_board.moves)

    def test_alpha_AF_1_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[65]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

    def test_alpha_AF_2_depth1(self):
        b_board = board()
        b_board.screen = ()
        boardd, stell, depth, fen, moves = allBoardsForAlphaBetaSuche()[66]
        t_board = testingBoard(boardd, stell, fen, moves)
        move = returnAlphaBetaMove(b_board, t_board, depth)
        sq, dest = move
        b_board.moveZa(sq, dest)
        self.assertIn(move, t_board.moves)

class testingBoard():
    def __init__(self, name, stell, fen, moves):
        self.name = name
        self.stellung = stell
        self.FEN_Notation = fen
        self.moves = moves
        self.board, self.color, self.kingWhite, self.kingBlack, self.kingSideCastle_white, self.queenSideCastle_white, \
            self.kingSideCastle_black, self.queenSideCastle_black, \
            self.enPassent, self.halfMoveClock, self.fullMoveClock, self.hilfsboard = FENtoBoard(fen)

def returnAlphaBetaMove(b_board, t_board, depth):
    b_board.board = t_board.board
    b_board.boardInteger = np.array(t_board.hilfsboard)
    b_board.positions()
    b_board.blackKing = t_board.kingBlack
    if t_board.kingBlack.position != (0, 4):
        b_board.blackKing.king_moved = True
    b_board.whiteKing = t_board.kingWhite
    if t_board.kingWhite.position != (7, 4):
        b_board.whiteKing.king_moved = True
    if t_board.color == 'black':
        b_board.Anzahlmoves += 1
    if t_board.color == 'white':
        b_board.botplaying = (False, 'white')

    bewertung, path = alpha_beta(b_board, depth, float('-inf'), float('inf'), True)
    move = path[0].lastmove
    return move

def returnAllMoves(b_board, t_board):
    b_board.board = t_board.board
    b_board.boardInteger = np.array(t_board.hilfsboard)
    #chessBoardVisualize(b_board.boardInteger)
    #print(b_board.boardInteger)
    b_board.positions()
    b_board.blackKing = t_board.kingBlack
    if t_board.kingBlack.position != (0,4):
        b_board.blackKing.king_moved = True
    b_board.whiteKing = t_board.kingWhite
    if t_board.kingWhite.position != (7,4):
        b_board.whiteKing.king_moved = True
    list_of_possible_moves = []
    if t_board.color == 'black':
        b_board.Anzahlmoves += 1
    moves = b_board.legalMoves()
    for row in range(8):
        for col in range(8):
            piece = b_board.board[row][col]
            if piece is not None and piece.color == t_board.color:
                legal_moves = moves[(row,col)]
                while len(legal_moves) != 0:
                    move = legal_moves.pop()
                    possible_move = ((row, col), move)
                    list_of_possible_moves.append(possible_move)

    #print(list_of_possible_moves)
    return list_of_possible_moves


def FENtoBoard(FEN):
    board = [[None for _ in range(8)] for _ in range(8)]
    i = 0
    j = 0
    k = 0 # space counter
    kingsideCastleBlack = False
    queensideCastleBlack = False
    kingsideCastleWhite = False
    queensideCastleWhite = False
    kingWhite = None
    kingBlack = None
    enPassentSquareCol = ()
    enPassentSquareRow = ()
    halfMoveClock = ()
    fullMoveClock = ()
    rookPositions = []
    # [L1]/[L2]/[L3]/[L4]/[L5]/[L6]/[L7]/[L8] [Active Color] [Castling Availability]
    # [En Passant target square - Piyon önceki el 2 kare ilerledi]
    while FEN != "":
        char = FEN[0]
        FEN = ''.join(FEN.split(char, 1))
        if char == '/':
            i += 1
            j = 0
        elif char == 'p':
            board[i][j] = Pawn('black',"sPion",(i,j))
            j += 1
        elif char == 'n':
            board[i][j] = Knight('black',"sAt",(i,j))
            j += 1
        elif char == 'b':
            board[i][j] = (Bishop('black',"sFil",(i,j)))
            j += 1
        elif char == 'r':
            board[i][j] = (Rook('black',"sK",(i,j)))
            #print("Found a black rook: ", (i,j))
            rookPositions.append((i,j))
            j += 1
        elif char == 'q':
            board[i][j] = (Queen('black',"sV",(i,j)))
            j += 1
        elif char == 'k':
            board[i][j] = (King('black', "sSah",(i,j)))
            kingBlack = board[i][j]
            j += 1
        elif char == 'N':
            board[i][j] = (Knight('white', "bAt",(i,j)))
            j += 1
        elif char == 'B':
            board[i][j] = (Bishop('white', "bFil",(i,j)))
            j += 1
        elif char == 'R':
            board[i][j] = (Rook('white', "bK",(i,j)))
            #print("Found a white rook: ", (i, j))
            rookPositions.append((i, j))
            j += 1
        elif char == 'Q':
            board[i][j] = (Queen('white', "bV",(i,j)))
            j += 1
        elif char == 'K':
            board[i][j] = (King('white', "bSah",(i,j)))
            kingWhite = board[i][j]
            j += 1
        elif char == 'P':
            board[i][j] = (Pawn('white', "bPion",(i,j)))
            j += 1
        elif char.isdigit():
            j += int(char)
        elif char == ' ':
            k += 1
            if FEN != '':
                char = FEN[0]
                FEN = ''.join(FEN.split(char, 1))
            if k == 1: # Turn Variable
                if char == 'w':
                    color = 'white'
                elif char == 'b':
                    color = 'black'
            elif k == 2: # Castling availability - Rok nasıl yapılabilir?
                if char == 'K':
                    kingsideCastleWhite = True
                    if len(FEN) != 0:
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char == 'Q':
                    queensideCastleWhite = True
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char == 'k':
                    kingsideCastleBlack = True
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char == 'q':
                    queensideCastleBlack = True
            elif k == 3: # En Passent Variable
                if char == 'a':
                    enPassentSquareCol = 0
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'b':
                    enPassentSquareCol = 1
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'c':
                    enPassentSquareCol = 2
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'd':
                    enPassentSquareCol = 3
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'e':
                    enPassentSquareCol = 4
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'f':
                    enPassentSquareCol = 5
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'g':
                    enPassentSquareCol = 6
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                elif char == 'h':
                    enPassentSquareCol = 7
                    if FEN != "":
                        char = FEN[0]
                        FEN = ''.join(FEN.split(char, 1))
                if char.isdigit():
                    if int(char) == 1:
                        enPassentSquareRow = 7
                    elif int(char) == 2:
                        enPassentSquareRow = 6
                    elif int(char) == 3:
                        enPassentSquareRow = 5
                    elif int(char) == 4:
                        enPassentSquareRow = 4
                    elif int(char) == 5:
                        enPassentSquareRow = 3
                    elif int(char) == 6:
                        enPassentSquareRow = 2
                    elif int(char) == 7:
                        enPassentSquareRow = 1
                    elif int(char) == 8:
                        enPassentSquareRow = 0
            elif k == 4: # Half Move Clock
                if char.isdigit():
                    halfMoveClock = int(char)
            elif k == 5: # Full Move Clock
                if char.isdigit():
                    fullMoveClock = int(char)
            #print("Remaining FEN:", FEN)
        elif char == '-':
            continue
            # Board is done
    while len(rookPositions)!=0:
        i, j = rookPositions.pop()
        if board[i][j].color == 'black':
            if queensideCastleBlack == False and (i,j) == (0,0):
                board[i][j].rook_moved = True

            elif kingsideCastleBlack == False and (i,j) == (0,7):
                board[i][j].rook_moved = True

        if board[i][j].color == 'white':
            if queensideCastleWhite == False and (i,j) == (7,0):
                board[i][j].rook_moved = True
            elif kingsideCastleWhite == False and (i,j) == (7,7):
                board[i][j].rook_moved = True

    hilfsboard = [[1600 for _ in range(8)] for _ in range(8)]
    for i in range(len(board)):
        for j in range (len(board[i])):
            if board[i][j] is not None:
                if board[i][j].color == 'black':
                    if isinstance(board[i][j], Pawn):
                        hilfsboard[i][j] = 1000
                    elif isinstance(board[i][j], Bishop):
                        hilfsboard[i][j] = 1010
                    elif isinstance(board[i][j], Rook):
                        hilfsboard[i][j] = 1011
                    elif isinstance(board[i][j], Knight):
                        hilfsboard[i][j] = 1001
                    elif isinstance(board[i][j], King):
                        hilfsboard[i][j] = 1111
                    elif isinstance(board[i][j], Queen):
                        hilfsboard[i][j] = 1110
                elif board[i][j].color == 'white':
                    if isinstance(board[i][j], Pawn):
                        hilfsboard[i][j] = 2000
                    elif isinstance(board[i][j], Bishop):
                        hilfsboard[i][j] = 2010
                    elif isinstance(board[i][j], Rook):
                        hilfsboard[i][j] = 2011
                    elif isinstance(board[i][j], Knight):
                        hilfsboard[i][j] = 2001
                    elif isinstance(board[i][j], King):
                        hilfsboard[i][j] = 2111
                    elif isinstance(board[i][j], Queen):
                        hilfsboard[i][j] = 2110
    return board, color, kingWhite, kingBlack, kingsideCastleWhite, queensideCastleWhite, kingsideCastleBlack, queensideCastleBlack, \
        (enPassentSquareRow,enPassentSquareCol), halfMoveClock, fullMoveClock, hilfsboard

def generate_mini_boards(board):
    board_list = []
    list_of_possible_moves = []
    moves = board.legalMoves()
    for row in range(8):
        for col in range(8):
            piece = board.board[row][col]
            if piece != None and board.Anzahlmoves % 2 == 0 and piece.color == 'white':
                legal_moves = moves[(row, col)]
                #print("Piece in pos:", row, col, " has legal moves:", legal_moves)
                while len(legal_moves) != 0:
                    move = legal_moves.pop()
                    possible_move = ((row, col), move)
                    list_of_possible_moves.append(possible_move)
                    board_list.append(copy.deepcopy(board))
            elif piece != None and board.Anzahlmoves % 2 == 1 and piece.color == 'black':
                legal_moves = moves[(row, col)]
                #print("Piece in pos:", row, col, " has legal moves:", legal_moves)
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
            #print("At child:", child.boardInteger)
            value, child_path = alpha_beta(child, depth-1, best_value, beta, False, path + [child])
            if value > best_value:
                best_value = value
                best_path = child_path
            if best_value >= beta: # Beta-Cutoff
                #print("BetaCutoff!")
                break
        return best_value, best_path
    else:
        best_value = beta
        best_path = None
        for child in generate_mini_boards(node):
            #print("At child:", child.boardInteger)
            value, child_path = alpha_beta(child, depth-1, alpha, best_value, True, path + [child])
            if value < best_value:
                best_value = value
                best_path = child_path
            if best_value <= alpha: # Alpha-Cutoff
                #print("AlphaCutoff!")
                break
        return best_value, best_path

def isTerminal(b_board):
    #TODO: If no more possible moves - Stalemate
    if b_board.finished:
        return True

def chessBoardVisualize(integerList):
    print("+[Board]+")
    print("+--------+")
    for i in range (len(integerList)):
        string = "|"
        for j in range (len(integerList[i])):
            if integerList[i][j] == 1600:
                string += "_"
            elif integerList[i][j] == 2111:
                string += "♚"
            elif integerList[i][j] == 1111:
                string += "♔"
            elif integerList[i][j] == 2011:
                string += "♜"
            elif integerList[i][j] == 1011:
                string += "♖"
            elif integerList[i][j] == 2001:
                string += "♞"
            elif integerList[i][j] == 1001:
                string += "♘"
            elif integerList[i][j] == 2010:
                string += "♝"
            elif integerList[i][j] == 1010:
                string += "♗"
            elif integerList[i][j] == 2110:
                string += "♛"
            elif integerList[i][j] == 1110:
                string += "♕"
            elif integerList[i][j] == 2000:
                string += "♟"
            elif integerList[i][j] == 1000:
                string += "♙"
        print(string + "|")
    print("+--------+")


def allBoards():

    boards = [("Fricke", 1, "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w", 20),
              ("A", 1, "2b1k3/p5rp/Pppb1p1P/n2qpPpR/1PPpP1P1/R2P1Q1B/1Br4n/1N2K1N1 w", 33),
              ("A", 2, "r1bqk2r/ppp3pp/5p2/2nPp3/P1Pn2P1/3P1N2/1P2BP1P/RN1Q1RK1 b k", 42),
              ("N", 1, "r2qk2r/pp1bp1bp/2np1np1/2pP4/2P1P3/2N2N2/PP3PPP/R1BQKB1R w - - 0 1", 38),
              ("N", 2, "6r1/p5k1/3Q4/2N5/5P2/1p6/P5KP/4qR2 w - - 0 25", 42),
              ("L", 1, "r2qk2r/p1p1p1P1/1pn4b/1N1Pb3/1PB1N1nP/8/1B1PQPp1/R3K2R b Qkq - 0 1", 39), #düzeltildi rocharde yok yanlış yazmışlar
              ("L", 2, "r1bq4/pp1p1k1p/2p2p1p/2b5/3Nr1Q1/2N1P3/PPPK1PPP/3R1B1R w - - 0 1", 51),
              ("G", 1, "r1bqkr2/pp1pbpQp/8/2p1P3/2B5/2N5/PPP2PPP/R1B1K2R b KQq - 2 10", 20),
              ("G", 2, "r2r2k1/ppp1p2p/6p1/4b1p1/PnP4P/2N4P/1P6/R3KB2 w - 0 17", 22),
              ("O", 1, "1k6/p1nrp3/n2p4/2p5/3PP3/2P2P2/P7/RN4K1 w", 14),
              ("O", 2, "8/3np3/3pk3/2p5/1PKPP3/2P2P2/8/8 w", 9),
              ("J", 1, "r3k2r/pp6/2p3Pb/2N1pP2/Q2p4/4P3/PP1K4/7R w q e6 0 34", 42), #Kalıyo R-düzeltildi
              ("J", 2, "r3k2r/pp2qppp/1np2n2/2bPp1B1/B2P2Q1/2N2N2/PPP2PPP/2KR3R b kq - 0 10", 36),
              ("H", 1, "5r2/p2Qb2p/3n1p2/3P2k1/1PB5/8/1B5P/R3K2R b KQ - 1 27", 27),
              ("H", 2, "4k2r/r2n1pbp/3B2p1/p1p3P1/2p4P/7B/PP2K3/1R4NR w k - 0 22", 34),
              ("AA", 1, "K7/8/8/pP6/8/4R3/2Pq1k2/8 w - - 0 1", 20),
              ("AA", 2, "8/5k1K/1q5P/2p5/8/5pp1/8/8 w - - 0 1", 1),
              ("AB", 1, "rnbqk3/p6P/2n1p1P1/1r3p2/8/1PN1K3/P4P2/R1BQ1BNR w q - 0 1", 47),#Kalıyo R düzeltildi
              ("AB", 2, "rnb1kbnr/p6p/Bp4p1/8/Q4p2/N2qBN2/PP3PPP/R3K2R b kq - 0 1 ", 9),
              ("S", 1, "rnbqkbnr/ppp1pppp/8/4p3/3PP3/8/PPP2PPP/RNBQKBNR b KQkq d3 0 2", 29), #Kalıyo R YANLIŞ KAALE ALMA
              ("S", 2, "r3k1nr/pppb1ppp/4q3/2b1B3/3Q1P2/2N5/PPP1P1PP/R3KB1R w KQkq - 1 10", 43),
              ("AF", 1, "8/8/4kpp1/3p4/p6P/2B4b/6P1/6K1 w - - 1 48", 17),
              ("AF", 2, "5rk1/pp4pp/4p3/2R3Q1/3n4/6qr/P1P2PPP/5RK1 w - - 2 24", 41),
              ("R", 1, "r1bqkb1r/p2p2pp/1pn2p1n/2p1p3/3P1B2/1P3N2/P1P1PPPP/RN1QKB1R w KQkq - 0 1", 34),
              ("R", 2, "2r4r/8/8/4k3/8/R7/8/4K2R w K - 0 1 Legale Züge 30", 29), #Kalıyod
              ("P", 1, "r1b1k1nr/1pp2ppp/p1p5/2b1p3/P3P3/2N2PP1/1PPP3q/R1B1KQ2 w Qkq - 0 11", 27),
              ("P", 2, "8/2p2R2/1p2p1Np/1P5k/3nr3/8/P7/2K5 w - - 0 34", 24),
              ("AH", 1, "1n1qkbnr/2pppppp/p7/p2P4/6Q1/8/PPPP1PPP/R1B1K1NR b KQk - 0 6", 16),
              ("AH", 2, "8/8/r3k3/8/8/3K4/8/8 b - - 0 31", 18),
              ("F", 1, "rnbqk2r/ppppppbp/5np1/8/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 2 4", 26),
              ("F", 2, "3r2k1/p6p/6p1/4b3/2P5/8/P1K3PP/5R2 w - - 5 27", 24),
              ("T", 1, "r1bqk1nr/ppp2ppp/2n1p3/3p4/1b1P1B2/4PN2/PPP2PPP/RN1QKB1R w KQkq - 3 5", 6),
              ("T", 2, "8/8/4k3/3pP3/3K4/8/8/8 b - - 12 45", 4),
              ("U", 1, "r1bq1rk1/ppp2ppp/2np1n2/3p4/2PP4/2NBPN2/PP3PPP/R1BQK2R w KQ - 4 6", 43),
              ("U", 2, "r4rk1/1pp1q1pp/2np1pn1/p3p3/2PPP3/2N1BP2/PPQ2P1P/R3K2R w KQ - 2 14", 40),
              ("U", 3, "2kr3r/1p3pp1/p1nqbn1p/3p4/3P2P1/1BN2N2/PPP1QPBP/R4RK1 w - - 0 14", 41),
              ("U", 4, "r4rk1/1bqn1ppp/p2bpn2/1p1p4/2pP4/1PNBPN2/PB3PPP/R2Q1RK1 w - - 1 12", 40),
              ("V", 1, "r1bq1rk1/ppp2ppp/2nb1n2/3pp3/2PPP3/2N2N2/PP2BPPP/R1BQ1RK1 w - - 0 10", 36),
              ("V", 2, "2kr1b1r/pp2pppp/2p5/1B6/2PPn3/8/PP3PPP/R1B1R1K1 b - - 0 14", 30),
              ("K", 1, "4k3/pp3pp1/8/8/1P2N1p1/7r/3K4/2r5 b", 41),
              ("K", 2, "r3k2r/p5pp/2p3qn/7K/6P1/2N4N/P5PP/7R w", 1),
              ("X", 1, "8/6P1/5K1k/6N1/5N2/8/8/8 w", 20), #Düzeltildi piyon değişimi
              ("X", 2, "rnbqk1nr/pppp1ppp/4p3/8/1bPP4/8/PP2PPPP/RNBQKBNR w", 4),
              ("C", 1, "r1b1kb1r/pp1p1ppp/1q3n2/2p5/4P3/2N5/PPP2PPP/R1BQKB1R w - - 0 1", 40),
              ("C", 2, "rn1qkbnr/ppp1ppp1/4b3/3pN2p/8/2N4P/PPPPPPP1/R1BQKB1R w - - 0 1", 29),
              ("M", 1, "rnbq1rk1/pp2n1pp/2p2p1b/3pp2N/2PPP3/1PN2P2/P5PP/R1BQKB1R w KQ - 0 1", 38),
              ("M", 2, "2bk2q1/8/8/8/8/8/2Q5/2R3K1 w - - 0 1", 6),
              ("Z", 1, "r1b1kb2/p2qp1pr/n1pp1n1p/1P3p2/5P1P/BPN4R/P2PP1P1/R2QKBN1 w", 33),#Kalıyo düzeltildi
              ("Z", 2, "8/3k4/8/3r4/8/3Q4/8/3K4 w", 8),
              ]
    return boards

def allBoardsForAlphaBetaSuche():
    boards = [
              ("J", 1, 1, "2k5/6q1/3P1P2/4N3/8/1K6/8/8 w - - 0 1", [((2, 5), (1, 6))]),
              ("J", 1, 2, "2k5/6q1/3P1P2/4N3/8/1K6/8/8 w - - 0 1", [((2, 5), (1, 6))]),
              ("J", 1, 3, "2k5/6q1/3P1P2/4N3/8/1K6/8/8 w - - 0 1", [((5, 1), (4, 2))]),

              ("J", 2, 1, "k7/8/3p4/4q3/3P4/8/4Q3/K7 w - - 0 1", [((4, 3), (3, 4)), ((6, 4), (3, 4))]),
              ("J", 2, 2, "k7/8/3p4/4q3/3P4/8/4Q3/K7 w - - 0 1", [((4, 3), (3, 4))]),
              ("J", 2, 3, "k7/8/3p4/4q3/3P4/8/4Q3/K7 w - - 0 1", [((6, 4), (2, 0)), ((6, 4), (5, 5)), ((6, 4), (6, 0)), ((6, 4), (6, 6))]),

              ("C", 1, 1, "rnbqkbnr/1pppppp1/p6p/8/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 1 3", [((1, 3), (2, 3))]),
              ("C", 1, 2, "rnbqkbnr/1pppppp1/p6p/8/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 1 3", [((0, 1), (2, 2))]),
              ("C", 1, 3, "rnbqkbnr/1pppppp1/p6p/8/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 1 3", [((2, 0), (3, 0))]),

              ("C", 2, 1, "r1b2rk1/ppqn1ppp/2n1p3/3pP3/1b1P4/3B1N2/PP1N1PPP/R1BQR1K1 b - - 0 1", [((1, 2), (0, 3))]),
              ("C", 2, 2, "r1b2rk1/ppqn1ppp/2n1p3/3pP3/1b1P4/3B1N2/PP1N1PPP/R1BQR1K1 b - - 0 1", [((2, 2), (0, 3))]),
              ("C", 2, 3, "r1b2rk1/ppqn1ppp/2n1p3/3pP3/1b1P4/3B1N2/PP1N1PPP/R1BQR1K1 b - - 0 1", [((2, 2), (0, 3))]),

              ("O", 1, 1, "r2q1rk1/pp2ppbp/2np1np1/8/2PP4/2N1PN2/PPQ2PPP/R1B1K2R b KQ - 4 8", [((0, 0), (0, 2))]),
              ("O", 1, 2, "r2q1rk1/pp2ppbp/2np1np1/8/2PP4/2N1PN2/PPQ2PPP/R1B1K2R b KQ - 4 8", [((0, 3), (3, 0))]),
              ("O", 1, 3, "r2q1rk1/pp2ppbp/2np1np1/8/2PP4/2N1PN2/PPQ2PPP/R1B1K2R b KQ - 4 8", [((2, 2), (3, 0))]),
              # Q atladım
              ("K", 1, 1, "4k3/p7/8/8/1P2N1p1/8/6r1/3K4 w", [((4, 1), (3, 1))]),
              ("K", 1, 2, "4k3/p7/8/8/1P2N1p1/8/6r1/3K4 w", [((4, 4), (2, 3)), ((4, 4), (2, 5))]),
              ("K", 1, 3, "4k3/p7/8/8/1P2N1p1/8/6r1/3K4 w", [((4, 4), (2, 5))]),

              ("K", 2, 1, "4k3/p7/7n/8/K5P1/2r5/P5P1/8 w", [((6, 0), (5, 0)), ((6, 6), (5, 6)), ((4, 6), (3, 6))]),
              ("K", 2, 2, "4k3/p7/7n/8/K5P1/2r5/P5P1/8 w", [((6, 0), (5, 0)), ((6, 6), (5, 6)), ((4, 6), (3, 6))]),
              ("K", 2, 3, "4k3/p7/7n/8/K5P1/2r5/P5P1/8 w", [((4, 0), (4, 1)), ((4, 6), (3, 6))]),

              # L Atladım
              ("AB", 2, 1, "rnb1kbnr/p6p/Bp4p1/8/Q4p2/N2qBN2/PP3PPP/R3K2R b kq - 0 1", [((2, 1), (3, 1))]),
              ("AB", 2, 2, "rnb1kbnr/p6p/Bp4p1/8/Q4p2/N2qBN2/PP3PPP/R3K2R b kq - 0 1", [((0, 2), (1, 3))]),

              ("H", 1, 1, "rn1qr1k1/1pp2ppp/p2bbn2/3p4/3P1B2/2NB1N2/PPPQ1PPP/2KR3R w - - 0 10", [((4, 5), (2, 3))]),
              ("H", 1, 2, "rn1qr1k1/1pp2ppp/p2bbn2/3p4/3P1B2/2NB1N2/PPPQ1PPP/2KR3R w - - 0 10", [((5, 5), (3, 6))]),

              ("M", 2, 1, "r1bq1rk1/ppp2ppp/2n1pn2/2b5/2P5/2N1PN2/PPQ2PPP/R1B1KB1R w KQ - 0 11", [((6, 0), (5, 0))]),
              ("M", 2, 3, "r1bq1rk1/ppp2ppp/2n1pn2/2b5/2P5/2N1PN2/PPQ2PPP/R1B1KB1R w KQ - 0 11", [((6, 1), (5, 1))]),
              # G atladım
              # I atladım
              ("V", 1, 1, "r3r1k1/p4ppp/2Q1b3/4N3/5q2/4RP2/PPB3PP/R5K1 w - - 0 1", [((2, 2), (5, 2))]),
              ("V", 1, 2, "r3r1k1/p4ppp/2Q1b3/4N3/5q2/4RP2/PPB3PP/R5K1 w - - 0 1", [((2, 2), (4, 4))]),
              ("V", 1, 3, "r3r1k1/p4ppp/2Q1b3/4N3/5q2/4RP2/PPB3PP/R5K1 w - - 0 1", [((7, 0), (7, 4))]),

              ("V", 2, 1, "r3k2r/p2n1ppp/2p5/1pN1p1B1/8/3PnP2/PP4PP/R3K2R b KQkq - 0 16", [((5, 4), (6, 6))]),
              ("V", 2, 2, "r3k2r/p2n1ppp/2p5/1pN1p1B1/8/3PnP2/PP4PP/R3K2R b KQkq - 0 16", [((5, 4), (6, 6))]),
              ("V", 2, 3, "r3k2r/p2n1ppp/2p5/1pN1p1B1/8/3PnP2/PP4PP/R3K2R b KQkq - 0 16", [((5, 4), (6, 2))]),

              ("F", 1, 1, "rnbqk2r/ppppppbp/5np1/8/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 2 4", [((2, 5), (3, 3))]),
              ("F", 1, 2, "rnbqk2r/ppppppbp/5np1/8/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 2 4", [((0, 4), (0, 6))]),
              ("F", 1, 3, "rnbqk2r/ppppppbp/5np1/8/2PP4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 2 4", [((0, 1), (2, 2))]),

              ("F", 2, 1, "3r2k1/p6p/6p1/4b3/2P5/8/P1K3PP/5R2 w - - 5 27", [((7, 5), (1, 5))]),
              ("F", 2, 2, "3r2k1/p6p/6p1/4b3/2P5/8/P1K3PP/5R2 w - - 5 27", [((6, 2), (7, 1))]),
              ("F", 2, 3, "3r2k1/p6p/6p1/4b3/2P5/8/P1K3PP/5R2 w - - 5 27", [((6, 6), (5, 6))]),

              ("AA", 1, 1, "5rk1/1p4pp/2R1p3/p5Q1/P4P2/6qr/2n3PP/5RK1 w - - 0 1", [((6, 7), (5, 6))]),
              ("AA", 2, 1, "5r1k/2p5/4R3/2N3np/1b4p1/6P1/2Q4P/2K5 b - - 0 1", [((4, 1), (5, 0))]),
              ("AA", 2, 2, "5r1k/2p5/4R3/2N3np/1b4p1/6P1/2Q4P/2K5 b - - 0 1", [((4, 1), (5, 0))]),
              ("AA", 2, 3, "5r1k/2p5/4R3/2N3np/1b4p1/6P1/2Q4P/2K5 b - - 0 1", [((0, 5), (7, 5))]),

       # Without depth specification

            ("N", 1, 1, "r3kb1r/1p1nqp1p/p2p1np1/P1p1p3/2P1P3/2N1K1PP/1P1P1P2/R1BQ1B1R w kq - 1 11", [((7, 0), (7, 2))]),
            ("N", 2, 1, "r1bqkbnr/p2ppppp/2p5/1p4N1/2B1P3/8/PPQP1PPP/RNB1K2R w KQkq b6 0 1", [((5, 4), (5, 5))]),

            ("A", 1, 1, "r2qk2r/p1ppn1pp/bpnb1p2/4p3/4P3/2NPBN2/PPP1BPPP/R2Q1RK1 w Qkq", [((7, 0), (7, 2))]),
            ("A", 2, 1, "8/1k6/1r3rp1/8/4R2P/2K5/3R4/8 w - -", [((5, 2), (5, 3))]),

            ("B", 1, 1, "r2qk2r/pp1bp1bp/2np1np1/2pP4/2P1P3/2N2N2/PP3PPP/R1BQKB1R w - - 0 1", [((6, 7), (5, 7))]),
            ("B", 2, 1, "4K3/4P1k1/8/8/8/8/7R/5r2 w - - 0 1", [((6, 7), (6, 4))]),

            ("S", 1, 1, "rnb1kbnr/pppp1ppp/4pq2/6N1/8/2N5/PPPPPPPP/R1BQKB1R b KQkq 0 5", [((2, 5), (3, 6)), ((2, 5), (5, 2))]),
            ("S", 2, 1, "r1b1kbnr/p2p1ppp/1p3q2/1BpNp3/4P3/3Q1N2/PPP2PPP/R1B1K2R w KQkq 0 7", [((3, 3), (2, 5))]),

            ("O", 2, 1, "r4rk1/1bp1qp1p/p2p1np1/2nPp3/2P1P3/1PN2N2/PB1Q1PPP/R3K2R w KQ - 2 14", [((6, 3), (5, 4))]),

            ("AD", 1, 1, "r2q1rk1/ppp2ppp/2n5/2b1PbN1/8/4p3/PPP3PP/RNBQR1K1 w - - 0 1", [((7, 3), (0, 3))]),
            ("AD", 2, 1, "r3r1k1/p4ppp/1p1p4/2pP4/Q5bq/P1B1P3/1P3PPP/3R1RK1 b - - 1 21", [((6, 2), (4, 0))]),

            ("AB", 1, 1, "rnbqk3/p6P/2n1p1P1/1r3p2/8/1PN1K3/P4P2/R1BQ1BNR w q - 0 1", [((1, 7), (0, 7))]),

            ("H", 2, 1, "rq2kb1r/pbppp1p1/n4p1p/1p1n4/7P/1PP1PNPR/P1QP1P2/RNB1KB2 b Qkq - 2 9", [((3, 1), (4, 1))]),

            ("M", 1, 1, "8/5P2/8/p4Kpp/6pk/P5p1/6P1/8 w - - 0 1", [((1, 5), (0, 5))]),

            ("T", 1, 1, "2kr3r/pp2q3/2p2p2/3p4/3Pb3/5nPp/PPB2P1B/R2QR1K1 w - - 1 24", [((7, 3), (5, 5))]),
            ("T", 2, 1, "1R6/6n1/4p3/3p3P/6P1/3nk3/1p6/6K1 w - - 1 48", [((3, 7), (2, 7))]),

            ("R", 1, 1, "rnbqk1nr/pp1p1ppp/2p5/2b1p1B1/8/3P1N2/PPP1PPPP/RN1QKB1R w KQkq - 0 1", [((3, 6), (0, 3))]),
            ("R", 2, 1, "r3k3/p4ppp/n1p2q1n/2b1p1B1/4P3/N7/P1PQ2PP/K1R2B1R w Kq - 0 1", [((3, 6), (2, 5))]),

            ("P", 1, 1, "r1b1k1nr/1pp2ppp/p1p5/2b1p3/P3P3/2N2PP1/1PPP3q/R1B1KQ2 w KQkq", [((5, 6), (4, 6))]),
            ("P", 2, 1, "8/2p2R2/1p2p1Np/1P5k/3nr3/8/P7/2K5 w - - 0 34", [((2, 6), (0, 5))]),

            ("X", 1, 1, "r2qkb1r/p1p2ppp/5n2/1p1P4/3Q4/2N2P2/PPP2P1P/R3KB1R", [((7, 5), (3, 1))]),
            ("X", 2, 1, "r2qkb1r/ppp2ppp/2np1n2/8/3pP3/2N1BP2/PPP2P1P/R2QKB1R", [((5, 4), (4, 3))]),

            ("AF", 1, 1, "r1bqk1nr/8/2n3P1/p1bP3p/3pPPQ1/p1N5/8/R1B1KBNR b KQkq - 0 1", [((0, 2), (4, 6))]),
            ("AF", 2, 1, "rnbqkbnr/p1pppppp/8/1p6/Q7/2P5/PP1PPPPP/RNB1KBNR w KQkq - 0 1", [((4, 0), (3, 1))]),
              ]
    return boards


if __name__ == '__main__':
    unittest.main()
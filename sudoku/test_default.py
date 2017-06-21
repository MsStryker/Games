import unittest

from sudoku import SudokuBoard, verify_sudoku_board, is_unique_list


class SudokuBoardTestCase(unittest.TestCase):

    # def setUp(self):
    #     self.sudoku = SudokuBoard(9)

    def test_get_initial_list(self):
        board = SudokuBoard(9)
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(board._get_initial_list(), expected_result)

    def test_board_list(self):
        board = SudokuBoard(16)
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.assertEqual(board.board_list, expected_result)

    def test_get_initial_matrix(self):
        board = SudokuBoard(4).get_initial_matrix()
        expected_result = [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ]
        self.assertEqual(board, expected_result)

    def test_get_full_board(self):
        board = SudokuBoard(4).get_full_board()
        non_expected_result = [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ]
        self.assertNotEqual(board, non_expected_result)

    def test_get_playable_board(self):
        """should not equal board"""
        board = SudokuBoard(9)
        playable_board = board.get_playable_board()
        self.assertNotEqual(playable_board, board.board)


class IsUniqueListTestCase(unittest.TestCase):

    def test_true(self):
        test_list = [1, 2, 3, 4, 5, 6]
        self.assertTrue(is_unique_list(test_list))

    def test_with_none(self):
        test_list = [1, 2, 3, None, 5, 4]
        self.assertTrue(is_unique_list(test_list))

    def test_false(self):
        test_list = [1, 1, 2, 3, 4, 5]
        self.assertFalse(is_unique_list(test_list))

    def test_false_with_none(self):
        test_list = [1, 2, 5, None, 3, 2]
        self.assertFalse(is_unique_list(test_list))


class VerifySudokuBoardTestCase(unittest.TestCase):

    def test_true(self):
        test_board = [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ]
        self.assertTrue(verify_sudoku_board(test_board))

    def test_with_none(self):
        test_board = [
            [1, 2, 3, 4],
            [2, 3, 4, None],
            [3, None, 1, 2],
            [4, 1, 2, 3]
        ]
        self.assertTrue(verify_sudoku_board(test_board))

    def test_false(self):
        test_board = [
            [1, 2, 3, 4],
            [2, 3, 4, 4],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ]
        self.assertFalse(verify_sudoku_board(test_board))

    def test_false_with_none(self):
        test_board = [
            [1, 2, 3, 4],
            [None, 3, 4, 4],
            [3, None, 1, 2],
            [4, 1, 2, None]
        ]
        self.assertFalse(verify_sudoku_board(test_board))


if __name__ == '__main__':
    unittest.main()

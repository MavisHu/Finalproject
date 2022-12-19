import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_checkHorizon(self):
        board = [
            [None, 'O', None],
            ['X', 'X', 'O'],
            [None, None, 'O']
        ]
        self.assertEqual(logic.checkHorizon(board), False)

    def test_checkRow(self):
        board = [
            [None, 'O', None],
            ['X', 'X', 'X'],
            [None, None, 'O']
        ]
        self.assertEqual(logic.checkRow(board), False)

    def test_checkDig(self):
        board = [
            ['X', 'O', None],
            ['X', 'X', 'O'],
            [None, None, 'X']
        ]
        self.assertEqual(logic.checkDig(board), True)


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3

import unittest
from life import (
    get_adjacent_neighbours,
    get_adjacent_neighbours_count,
    get_dead_cells,
    get_newborn_cells,
    life,
)


class GameOfLifeTests(unittest.TestCase):
    def test_get_number_of_adjacent_neighbours(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        cells = (2, 2)
        neighbours = get_adjacent_neighbours_count(board, cells)

        self.assertEqual(neighbours, 2)

    def test_get_number_of_adjacent_neighbours_right_corner(self):
        board = [
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        len(board)
        cells = (0, 4)
        neighbours = get_adjacent_neighbours_count(board, cells)

        self.assertEqual(neighbours, 1)

    def test_get_number_of_adjacent_neighbours_left_corner(self):
        board = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        len(board)
        cells = (0, 0)
        neighbours = get_adjacent_neighbours_count(board, cells)

        self.assertEqual(neighbours, 0)

    def test_get_number_of_adjacent_neighbours_bottom_left_corner(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
        ]
        len(board)
        cells = (0, 0)
        neighbours = get_adjacent_neighbours_count(board, cells)

        self.assertEqual(neighbours, 0)

    def test_get_number_of_adjacent_neighbours_bottom_right_corner(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
        ]
        len(board)
        cells = (4, 4)
        neighbours = get_adjacent_neighbours_count(board, cells)

        self.assertEqual(neighbours, 0)

    def test_get_dead_cells(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        cells = {(1, 2), (2, 2), (3, 2)}
        dead_cells = get_dead_cells(board, cells)

        self.assertEqual(dead_cells, {(1, 2), (3, 2)})

    def test_get_cell_adjacent_neighbours(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        live_cell = (2, 2)
        adjacent_cells = get_adjacent_neighbours(board, live_cell)

        self.assertEqual(
            adjacent_cells, [(1, 3), (2, 3), (3, 3), (3, 1), (2, 1), (1, 1)]
        )

    def test_get_newborn_cells(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        cells = [(1, 2), (2, 2), (3, 2)]
        newborn_cells = get_newborn_cells(board, cells)

        self.assertEqual(newborn_cells, [(1, 2), (1, 1)])

    def test_get_new_board(self):
        board = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        cells = [(1, 2), (2, 2), (3, 2)]
        new_board = life(board, cells)

        self.assertEqual(
            new_board,
            [
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
                [(2, 3), (2, 1), (2, 2)],
            ],
        )


if __name__ == "__main__":
    unittest.main()

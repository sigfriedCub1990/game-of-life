#!/usr/bin/python3

import time
import os

MOVES = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


class Bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"

    def disable(self):
        self.HEADER = ""
        self.OKBLUE = ""
        self.OKGREEN = ""
        self.WARNING = ""
        self.FAIL = ""
        self.ENDC = ""


def is_position_in_range(pos_x, pos_y, board):
    board_size_x = len(board)
    board_size_y = len(board[0])
    return pos_x >= 0 and pos_x < board_size_x and pos_y >= 0 and pos_y < board_size_y


def get_adjacent_neighbours_count(board, cell):
    neighbours = 0
    for move in MOVES:
        (dx, dy) = move
        (cx, cy) = cell
        pos_x = cx + dx
        pos_y = cy + dy
        if is_position_in_range(pos_x, pos_y, board):
            if board[pos_x][pos_y] == 1:
                neighbours += 1

    return neighbours


def get_dead_cells(board, cells):
    """Compute which cells will die on this tick

    1. A cell dies if it has less than 2 neighbours (loneliness)
    2. A cell also dies if it has more than 3 neighbours (overpopulation)
    """
    dead_cells = set()

    for cell in cells:
        cell_neighbours = get_adjacent_neighbours_count(board, cell)
        if cell_neighbours < 2 or cell_neighbours > 3:
            dead_cells.add(cell)

    return dead_cells


def get_adjacent_neighbours(board, live_cell):
    """
    Get squares(neighbours) adjacent to a cell
    """
    adjacent_neighbours = []

    for move in MOVES:
        (dx, dy) = move
        (cx, cy) = live_cell
        pos_x = cx + dx
        pos_y = cy + dy
        if is_position_in_range(pos_x, pos_y, board):
            if board[pos_x][pos_y] != 1:
                adjacent_neighbours.append((pos_x, pos_y))

    return adjacent_neighbours


def get_newborn_cells(board, cells):
    """Computes which cells will be born in the next generation

    It does so by:
    1. Calculating all the neighbours squares for the existing cells
    2. Determines if those neighbours squares have 3 adjacent cells
    3. If 2 is True then a new cell is born in that square
    """
    maybe_newborn_cells = set()
    for current_cell in cells:
        adjacent_neighbours = get_adjacent_neighbours(board, current_cell)
        for neighbour in adjacent_neighbours:
            maybe_newborn_cells.add(neighbour)

    newborn_cells = []
    for maybe_newborn in maybe_newborn_cells:
        if get_adjacent_neighbours_count(board, maybe_newborn) == 3:
            newborn_cells.append(maybe_newborn)

    return newborn_cells


def life(board, initial_cells):
    board_copy = board.copy()
    newborn_cells = get_newborn_cells(board, initial_cells)
    dead_cells = get_dead_cells(board, initial_cells)
    live_cells = set(initial_cells).difference(dead_cells)
    next_generation = [*newborn_cells, *[live for live in live_cells]]

    for newborn in newborn_cells:
        (nx, ny) = newborn
        board_copy[nx][ny] = 1

    for dead in dead_cells:
        (dx, dy) = dead
        board_copy[dx][dy] = 0

    return [board_copy, next_generation]


def print_board(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != 0:
                print(f"{Bcolors.OKGREEN}*{Bcolors.ENDC}", end=" ")
            else:
                print("-", end=" ")
        print()


def get_inital_cells(board):
    cells = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 1:
                cells.append((row, column))

    return cells


if __name__ == "__main__":
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    cells = get_inital_cells(board)
    while True:
        os.system("clear")
        print_board(board)
        [new_board, next_generation] = life(board, cells)
        board = new_board
        cells = next_generation
        time.sleep(1)
        os.system("clear")

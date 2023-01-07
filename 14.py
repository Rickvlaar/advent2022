from util import console, parse_file_as_list, time_function
import numpy as np
from itertools import pairwise

test_file = parse_file_as_list('input/14_test.txt')
day_file = parse_file_as_list('input/14.txt')


AIR = '.'
SAND = '0'
STONE = '#'


@time_function()
def run_a(file):
    stone_lines = get_stone_lines(file)
    stone_map, sand_entry_point = prepare_map(stone_lines)
    min_x, max_x = get_limits(stone_lines, 0)
    stone_map = draw_stone_lines(stone_lines, stone_map, min_x)
    stone_map = drop_sand(stone_map, sand_entry_point)
    return np.where(stone_map == SAND)[0].size


@time_function()
def run_b(file):
    stone_lines = get_stone_lines(file)
    stone_map, sand_entry_point = prepare_map_with_floor(stone_lines)
    stone_map = draw_stone_lines(stone_lines, stone_map, 0)
    stone_map = drop_sand(stone_map, sand_entry_point)
    return np.where(stone_map == SAND)[0].size


def drop_sand(stone_map: np.ndarray, sand_entry_point: tuple):
    dropping = True
    while dropping:
        x, y = sand_entry_point
        while 1:
            try:
                below = stone_map[y + 1, x]
                if below == AIR:
                    y += 1
                elif below == STONE or below == SAND:
                    below_left = stone_map[y + 1, x - 1]
                    if below_left == AIR:
                        x -= 1
                        y += 1
                    elif below_left == STONE or below_left == SAND:
                        below_right = stone_map[y + 1, x + 1]
                        if below_right == AIR:
                            x += 1
                            y += 1
                        elif below_right == STONE or below_right == SAND:
                            stone_map[y, x] = SAND
                            if(x, y) == sand_entry_point:
                                dropping = False
                            break
            except IndexError:
                dropping = False
                break
    return stone_map


def prepare_map(stone_lines: list[list[tuple]]):
    min_x, max_x = get_limits(stone_lines, 0)
    min_y, max_y = get_limits(stone_lines, 1)
    x_len = max_x - min_x
    y_len = max_y
    sand_entry_point = (500 - min_x, 0)
    stone_map = np.full(shape=(y_len + 1, x_len + 1), fill_value=AIR, dtype=str)
    return stone_map, sand_entry_point


def prepare_map_with_floor(stone_lines: list[list[tuple]]):
    min_y, max_y = get_limits(stone_lines, 1)
    x_len = 999
    y_len = max_y + 2
    sand_entry_point = (500, 0)
    stone_map = np.full(shape=(y_len + 1, x_len + 1), fill_value=AIR, dtype=str)
    stone_map[-1] = STONE
    return stone_map, sand_entry_point


def draw_stone_lines(stone_lines: list[list[tuple]], stone_map, x_offset):
    for line in stone_lines:
        for coord_pair in pairwise(line):
            x_diff = abs(coord_pair[0][0] - coord_pair[1][0])
            y_diff = abs(coord_pair[0][1] - coord_pair[1][1])
            lowest_x_coord = sorted([coord_pair[0][0], coord_pair[1][0]])[0] - x_offset
            lowest_y_coord = sorted([coord_pair[0][1], coord_pair[1][1]])[0]
            start_x = coord_pair[0][0] - x_offset
            start_y = coord_pair[0][1]

            for step in range(x_diff + 1):
                stone_map[start_y, lowest_x_coord + step] = STONE

            for step in range(y_diff):
                stone_map[lowest_y_coord + step, start_x] = STONE

    return stone_map


def get_limits(stone_lines: list[list[tuple]], index: int) -> tuple:
    min_limit = 999
    max_limit = 0
    for coord_tuple_list in stone_lines:
        for coord in coord_tuple_list:
            bla = coord[index]
            if bla < min_limit:
                min_limit = bla
            if bla > max_limit:
                max_limit = bla
    return min_limit, max_limit


def get_stone_lines(file: list[str]) -> list[list[tuple]]:
    return [[int_tuple_from_string_coord(coord) for coord in line.split(' -> ')] for line in file]


def int_tuple_from_string_coord(coord: str) -> tuple:
    x, y = coord.split(',')
    return int(x), int(y)


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

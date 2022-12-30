from util import console, parse_file_as_list, time_function
import numpy as np
from itertools import product

test_file = parse_file_as_list('input/12_test.txt')
day_file = parse_file_as_list('input/12.txt')

START = ord('S') - 97
GOAL = ord('E') - 97


@time_function()
def run_a(file):
    elevation_map = get_map_from_file(file)
    the_start = np.where(elevation_map == START)  # Y, X
    the_goal = np.where(elevation_map == GOAL)  # Y, X

    start_coord = (the_start[0][0], the_start[1][0])
    goal_coord = (the_goal[0][0], the_goal[1][0])

    elevation_map[start_coord] = 0
    elevation_map[goal_coord] = 26
    visited_nodes_map = np.zeros(elevation_map.shape)
    console.print(elevation_map)

    the_hood = get_the_hood_straight(elevation_map)
    the_hood = remove_impossible_neighbours(the_hood, elevation_map)


    go_stepping(start_coord, elevation_map, visited_nodes_map, the_hood)

    return


def remove_impossible_neighbours(the_hood: dict, elevation_map: np.ndarray) -> dict:
    clean_hood = dict()
    for coord, neighbours in the_hood.items():
        coord_elevation = elevation_map[coord]
        clean_hood[coord] = [neighbour for neighbour in neighbours if coord_elevation - 1 <= elevation_map[neighbour] <= coord_elevation + 1]
    return clean_hood


def go_stepping(start_coord: tuple, elevation_map: np.ndarray, visited_nodes: np.ndarray, the_hood: dict):

    neighbours = the_hood[start_coord]
    coord_elevation = elevation_map[start_coord]
    console.print(coord_elevation)
    for coord in neighbours:
        elevation = elevation_map[coord]
        # check if height difference is traversable
        # if coord_elevation - 1 <= elevation <= coord_elevation + 1:
        #
        #
        # console.print(elevation)

    console.print(neighbours)

    pass


@time_function()
def run_b(file):
    # elevation_map = get_map_from_file(file)
    # console.print(elevation_map)

    pass


def get_map_from_file(file: list[str]) -> np.ndarray:
    return np.array([[ord(char) - 97 for char in line] for line in file])


def get_the_hood_8(grid: np.array):
    max_y = grid.shape[0]
    max_x = grid.shape[1]
    the_hood = dict()
    for y, line in enumerate(grid):
        for x, num in enumerate(line):
            xs = [x_2 for x_2 in range(x - 1, x + 2) if 0 <= x_2 < max_x]
            ys = [y_2 for y_2 in range(y - 1, y + 2) if 0 <= y_2 < max_y]
            the_hood[(y, x)] = [coord for coord in product(ys, xs) if coord != (y, x)]
    return the_hood


def get_the_hood_straight(grid):
    max_y = grid.shape[0] - 1
    max_x = grid.shape[1] - 1
    the_hood = dict()
    for y, line in enumerate(grid):
        for x, num in enumerate(line):
            neighbs = []
            if x > 0:
                neighbs.append((y, x - 1))
            if x < max_x:
                neighbs.append((y, x + 1))
            if y > 0:
                neighbs.append((y - 1, x))
            if y < max_y:
                neighbs.append((y + 1, x))
            the_hood[(y, x)] = neighbs
    return the_hood


if __name__ == '__main__':
    answer_a = run_a(test_file)
    answer_b = run_b(test_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

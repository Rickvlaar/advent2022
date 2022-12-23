import numpy as np

from util import console, parse_file_as_list, time_function
from math import dist

test_file = parse_file_as_list('input/9_test.txt')
test_b_file = parse_file_as_list('input/9b_test.txt')
day_file = parse_file_as_list('input/9.txt')

direction_coord_dict = {
        'U': 1,
        'D': 1,
        'L': 0,
        'R': 0
}

direction_modifier_dict = {
        'U': -1,
        'D': 1,
        'L': -1,
        'R': 1
}


@time_function()
def run_a(file):
    instructions = parse_instructions(file)

    tail_visits = set()
    head_position = [0, 0]  # x, y
    tail_position = [0, 0]

    for inst in instructions:
        direction = inst[0]
        steps = int(inst[1])

        for _ in range(steps):
            previous_head_position = head_position.copy()
            head_position[direction_coord_dict[direction]] += direction_modifier_dict[direction]
            if dist(head_position, tail_position) >= 2:
                tail_position = previous_head_position
                tail_visits.add(tuple(previous_head_position))

    return len(tail_visits)


@time_function()
def run_b(file):
    instructions = parse_instructions(file)

    tail_visits = set()
    head_position = [0, 0]  # x, y
    tail_positions = [[0, 0] for _ in range(9)]  # x, y

    for inst in instructions:
        direction = inst[0]
        steps = int(inst[1])

        for _ in range(steps):
            head_position[direction_coord_dict[direction]] += direction_modifier_dict[direction]
            compare_to = head_position.copy()

            for knot_num, knot_pos in enumerate(tail_positions):
                if dist(compare_to, knot_pos) >= 2:

                    tail_positions[knot_num][direction_coord_dict[direction]] += direction_modifier_dict[direction]
                    x = tail_positions[knot_num][0]
                    y = tail_positions[knot_num][1]

                    if x != compare_to[0] and y != compare_to[1]:
                        vertical_move = direction_coord_dict[direction]
                        if vertical_move:
                            tail_positions[knot_num][0] = compare_to[0]
                        else:
                            tail_positions[knot_num][1] = compare_to[1]

                    if knot_num == 8:
                        tail_visits.add(tuple(tail_positions[knot_num]))

                compare_to = tail_positions[knot_num].copy()
    return len(tail_visits)


def parse_instructions(file: list[str]):
    return [line.split(' ') for line in file]


if __name__ == '__main__':
    answer_a = run_a(test_file)
    answer_b = run_b(test_b_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

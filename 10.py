from util import console, parse_file_as_list, time_function
import numpy as np


test_file = parse_file_as_list('input/10_test.txt')
day_file = parse_file_as_list('input/10.txt')


@time_function()
def run_a(file):
    instructions = parse_file(file)
    x = 1
    cycle = 0
    signal_strengths = []
    instruction = None
    instruct_len = 0

    while True:
        cycle += 1

        if cycle % 20 == 0:
            signal_strengths.append(cycle * x)

        if not instruction:
            instruction = instructions.pop(0)

            if instruction[0] == 'noop':
                instruct_len = 1
            elif instruction[0] == 'addx':
                instruct_len = 2

        instruct_len -= 1
        if instruct_len == 0:
            if instruction[0] == 'addx':
                x += int(instruction[1])
            instruction = None

        if not instructions and not instruction:
            break

    return sum([signal for index, signal in enumerate(signal_strengths) if index in {0, 2, 4, 6, 8, 10}])


@time_function()
def run_b(file):
    np.set_printoptions(linewidth=100000)
    instructions = parse_file(file)
    sprite_pos = 1
    cycle = 0
    screen = [['_' for _ in range(40)] for _ in range(6)]
    console.print(screen)
    instruction = None
    instruct_len = 0

    while True:
        cycle += 1

        console.print(cycle)
        if cycle == 240:
            break

        crt_x = (cycle % 40) - 1
        crt_y = cycle // 40

        if sprite_pos - 1 <= crt_x <= sprite_pos + 1:
            screen[crt_y][crt_x] = '#'
        else:
            screen[crt_y][crt_x] = '.'


        if not instruction:
            instruction = instructions.pop(0)

            if instruction[0] == 'noop':
                instruct_len = 1
            elif instruction[0] == 'addx':
                instruct_len = 2

        instruct_len -= 1
        if instruct_len == 0:
            if instruction[0] == 'addx':
                sprite_pos += int(instruction[1])
            instruction = None

        if not instructions and not instruction:
            break

    return np.array(screen)


def parse_file(file: list[str]):
    return [line.split(' ') for line in file]


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B:\n {answer_b}')

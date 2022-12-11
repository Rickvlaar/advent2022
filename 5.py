from util import console, parse_file_as_list, time_function
from collections import deque

test_file = parse_file_as_list('input/5_test.txt')
day_file = parse_file_as_list('input/5.txt')


@time_function()
def run_a(file):
    stacks, instructions = parse_file(file)
    stacks = follow_instructions(stacks, instructions)
    return get_stack_message(stacks)


@time_function()
def run_b(file):
    pass


def parse_file(file: list[str]):
    stacks = [deque() for _ in range(9)]
    instructions = []
    for line in file:
        if '[' in line:
            for index, char in enumerate(line):
                if char.isalpha():
                    if index == 1:
                        stacks[0].append(char)
                    else:
                        target_index = int(index // 4)
                        stacks[target_index].append(char)

        elif line.startswith('move'):
            instructions.append([int(char) for char in line.split(' ') if char.isdigit()])
    return stacks, instructions


def follow_instructions(stacks: list[deque[str]], instructions: list[list[int]]):
    for instruction in instructions:
        move_count = instruction[0]
        source_stack_no = instruction[1] - 1
        target_stack_no = instruction[2] - 1

        for _ in range(move_count):
            item = stacks[source_stack_no].popleft()
            stacks[target_stack_no].appendleft(item)

    return stacks


def get_stack_message(stacks: list[deque[str]]):
    return ''.join([stack.popleft() for stack in stacks if stack])


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(test_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

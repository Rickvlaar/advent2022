from util import console, parse_file_as_list, time_function
from dataclasses import dataclass, field
from math import floor, prod, lcm

test_file = parse_file_as_list('input/11_test.txt')
day_file = parse_file_as_list('input/11.txt')


@dataclass
class Monkey:
    operation: () = None
    test: () = None
    actions_dict: dict[bool: int] = field(default_factory=dict[bool: int])
    items: list[int] = field(default_factory=list[int])
    action_count: int = 0


@time_function()
def run_a(file):
    monkey_dict = create_monkey_dict(file)
    return monkey_on(monkey_dict, 20, 3)


@time_function()
def run_b(file):
    monkey_dict = create_monkey_dict(file)
    # divider = lcm(23, 19, 13, 17)
    divider = lcm(2, 3, 5, 7, 11, 13, 17, 19)
    return monkey_on(monkey_dict, 10000, divider)


def monkey_on(monkey_dict: dict[int: Monkey], rounds: int, divider: int):
    for _ in range(rounds):
        monkey_dict = play_round(monkey_dict=monkey_dict, divider=divider)

    monkey_scores = [monkey.action_count for monkey in monkey_dict.values()]
    monkey_scores.sort(reverse=True)

    return prod(monkey_scores[:2])


def create_monkey_dict(file: list[str]) -> dict[int: Monkey]:
    monkey_dict = {}
    monkey_num = 0
    monkey = Monkey()
    for line in file:
        line = line.lstrip()
        if line.startswith('Starting items: '):
            parsed_line = line.removeprefix('Starting items: ')
            monkey.items = [int(item) for item in parsed_line.split(', ')]
        elif line.startswith('Operation: '):
            parsed_line = line.removeprefix('Operation: new = ')
            monkey.operation = eval('lambda old: ' + parsed_line)
        elif line.startswith('Test: divisible by '):
            parsed_line = line.removeprefix('Test: divisible by ')
            monkey.test = eval('lambda worry_level: (worry_level % ' + parsed_line + ') == 0')
        elif line.startswith('If true: throw to monkey '):
            parsed_line = line.removeprefix('If true: throw to monkey ')
            monkey.actions_dict[True] = int(parsed_line)
        elif line.startswith('If false: throw to monkey '):
            parsed_line = line.removeprefix('If false: throw to monkey ')
            monkey.actions_dict[False] = int(parsed_line)
        elif line.startswith('Monkey'):
            continue
        else:
            monkey_dict[monkey_num] = monkey
            monkey_num += 1
            monkey = Monkey()
    monkey_dict[monkey_num] = monkey
    return monkey_dict


def play_round(monkey_dict: dict[int: Monkey], divider: int) -> dict[int: Monkey]:
    for monkey in monkey_dict.values():
        while monkey.items:
            old = monkey.items.pop(0)
            monkey.action_count += 1
            worry_level = monkey.operation(old)
            worry_level = floor(worry_level % divider)
            test_result = monkey.test(worry_level)
            receiving_monkey = monkey.actions_dict[test_result]
            monkey_dict[receiving_monkey].items.append(worry_level)
    return monkey_dict


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

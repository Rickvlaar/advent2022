from util import console, parse_file_as_list, time_function
from itertools import starmap

test_file = parse_file_as_list('input/13_test.txt')
day_file = parse_file_as_list('input/13.txt')


@time_function()
def run_a(file):
    parsed_pairs = parse_file(file)
    return compare_pairs(parsed_pairs)


@time_function()
def run_b(file):
    pass


def compare_pairs(pairs: list):
    return sum([index + 1 for index, result in enumerate(starmap(compair, pairs)) if result])


def compair(left: list, right: list) -> bool:
    for index, left_value in enumerate(left):
        try:
            right_value = right[index]
        except:
            return False

        if is_int(left_value) and is_int(right_value):
            if left_value < right_value:
                return True
            elif left_value > right_value:
                return False
            else:
                continue

        elif is_list(left_value) and is_int(right_value):
            right_value = [right_value]

        elif is_list(right_value) and is_int(left_value):
            left_value = [left_value]

        result = compair(left_value, right_value)

        if result is not None:
            return result

    if len(left) < len(right):
        return True


def is_list(value) -> bool:
    return isinstance(value, list)


def is_int(value) -> bool:
    return isinstance(value, int)


def parse_file(file: list[str]):
    parsed_pairs = []
    pair = []
    for line in file:
        if line:
            parsed_line = eval(line)
            pair.append(parsed_line)
        else:
            parsed_pairs.append(pair)
            pair = []
    parsed_pairs.append(pair)
    return parsed_pairs


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(test_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

from util import console, parse_file_as_list, time_function

test_file = parse_file_as_list('input/6_test.txt')
day_file = parse_file_as_list('input/6.txt')


@time_function()
def run_a(file):
    return find_marker(file, 4)


@time_function()
def run_b(file):
    return find_marker(file, 14)


def find_marker(file: list[str], marker_length: int):
    index = 0
    while True:
        signal_set = set(file[0][index: index + marker_length])
        if len(signal_set) == marker_length:
            return index + marker_length
        index += 1


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

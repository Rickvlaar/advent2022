from util import console, parse_file_as_list, time_function

test_file = parse_file_as_list('input/4_test.txt')
day_file = parse_file_as_list('input/4.txt')


@time_function()
def run_a(file):
    assignment_pairs = convert_to_assignments(file)
    return intersecting_assigments(assignment_pairs)


@time_function()
def run_b(file):
    assignment_pairs = convert_to_assignments(file)
    return overlapping_assignments(assignment_pairs)


def convert_to_assignments(file: list[str]):
    return [[tuple([int(val) for val in assignment.split('-')]) for assignment in line.split(',')] for line in file]


def intersecting_assigments(assignments: [list[list[tuple]]]):
    intersecting_pairs = 0
    for assignment_pair in assignments:
        one = assignment_pair[0]
        two = assignment_pair[1]

        if (one[0] <= two[0] <= one[1] and two[1] <= one[1]) or (two[0] <= one[0] <= two[1] and one[1] <= two[1]):
            intersecting_pairs += 1
    return intersecting_pairs


def overlapping_assignments(assignments: [list[list[tuple]]]):
    overlapping_assigmnents = 0
    for assignment_pair in assignments:
        one = assignment_pair[0]
        two = assignment_pair[1]

        if two[0] <= one[0] <= two[1] or one[0] <= two[0] <= one[1] or two[0] <= one[1] <= two[1] or one[0] <= two[1] <= \
                one[1]:
            overlapping_assigmnents += 1
    return overlapping_assigmnents


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

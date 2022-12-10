from util import console, parse_file_as_list, time_function

test_file = parse_file_as_list('input/2_test.txt')
day_file = parse_file_as_list('input/2.txt')

# A = Rock = X == 1
# B = Paper = Y == 2
# C = Scissors = Z == 3
# lost = 0
# draw = 3
# won = 6

@time_function()
def run_a(file):
    rounds_in_points = convert_rounds_to_points(file)
    outcomes = get_round_outcomes(rounds_in_points)
    return sum(outcomes)


@time_function()
def run_b(file):
    rounds_in_points = convert_rounds_to_points(file)
    outcomes = get_round_outcomes_b(rounds_in_points)
    return sum(outcomes)


winner_outcome_dict = {
        1: 2,
        2: 3,
        3: 1
}

loser_outcome_dict = {
        1: 3,
        2: 1,
        3: 2
}


def convert_rounds_to_points(rounds: list[str]) -> list[list[int]]:
    return [[get_shape_points_value(shape) for shape in play_round.split(' ')] for play_round in rounds]


def get_round_outcomes(rounds: list[list[int]]) -> list[int]:
    outcomes = []
    for play_round in rounds:
        elf_move = play_round[0]
        your_move = play_round[1]
        if elf_move == your_move:
            outcomes.append(your_move + 3)
        elif your_move == winner_outcome_dict.get(elf_move):
            outcomes.append(your_move + 6)
        else:
            outcomes.append(your_move)
    return outcomes


def get_round_outcomes_b(rounds: list[list[int]]) -> list[int]:
    outcomes = []
    for play_round in rounds:
        elf_move = play_round[0]
        your_move = play_round[1]
        if your_move == 1:
            outcomes.append(loser_outcome_dict.get(elf_move))
        elif your_move == 2:
            outcomes.append(elf_move + 3)
        elif your_move == 3:
            outcomes.append(winner_outcome_dict.get(elf_move) + 6)
    return outcomes


def get_shape_points_value(shape: str) -> int:
    if shape == 'A' or shape == 'X':
        return 1
    elif shape == 'B' or shape == 'Y':
        return 2
    elif shape == 'C' or shape == 'Z':
        return 3


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

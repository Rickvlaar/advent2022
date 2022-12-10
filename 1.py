from util import console, parse_file_as_list, time_function

test_file = parse_file_as_list('input/1_test.txt')
day_file = parse_file_as_list('input/1.txt')


@time_function()
def run_a(file):
    elves = split_elves(file)
    summed_elves = [sum(elf_calories) for elf_calories in elves]
    return max(summed_elves)


@time_function()
def run_b(file):
    elves = split_elves(file)
    summed_elves = [sum(elf_calories) for elf_calories in elves]
    summed_elves.sort(reverse=True)
    top_three_sum = sum(summed_elves[0:3])
    return top_three_sum


def split_elves(file: list[str]) -> list[list[int]]:
    elves = []
    elflist = []
    for calories in file:
        if calories == '':
            elves.append(elflist)
            elflist = []
        else:
            elflist.append(int(calories))
    elves.append(elflist)

    return elves


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

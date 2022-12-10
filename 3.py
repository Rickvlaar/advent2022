import string

from util import console, parse_file_as_list, time_function

test_file = parse_file_as_list('input/3_test.txt')
day_file = parse_file_as_list('input/3.txt')


common_item_points_dict = {item: index + 1 for index, item in enumerate(string.ascii_letters)}


@time_function()
def run_a(file: list[str]):
    split_rucksacks = [split_compartments(rucksack) for rucksack in file]
    common_items = get_common_items_from_compartments(split_rucksacks)
    return sum([common_item_points_dict[item] for item in common_items])


@time_function()
def run_b(file: list[str]):
    elf_groups = split_into_elf_groups(file)
    common_items = get_common_items_from_elf_groups(elf_groups)
    return sum([common_item_points_dict[item] for item in common_items])


def split_compartments(rucksack: str) -> list[set[str]]:
    split_index = int(len(rucksack) / 2)
    return [set(rucksack[0:split_index]), set(rucksack[split_index:len(rucksack)])]


def get_common_items_from_compartments(rucksacks: list[list[set[str]]]) -> list[str]:
    return [compartments[0].intersection(compartments[1]).pop() for compartments in rucksacks]


def split_into_elf_groups(rucksacks: list[str]) -> list[list[set[str]]]:
    return [[set(rucksack) for rucksack in rucksacks[index: index + 3]] for index in range(0, len(rucksacks), 3)]


def get_common_items_from_elf_groups(rucksacks: list[list[set[str]]]) -> list[str]:
    return [rucksack[0].intersection(rucksack[1], rucksack[2]).pop() for rucksack in rucksacks]


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

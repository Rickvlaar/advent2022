from util import console, parse_file_as_list, time_function
import numpy as np

test_file = parse_file_as_list('input/8_test.txt')
day_file = parse_file_as_list('input/8.txt')


@time_function()
def run_a(file):
    tree_map = convert_to_int(file)
    x_dim_len = len(tree_map[0])
    y_dim_len = len(tree_map)
    visible_tree_map = np.zeros((x_dim_len, y_dim_len))
    visible_tree_map = set_horizontal_vis(tree_map, visible_tree_map)
    visible_tree_map = set_vertical_vis(tree_map, visible_tree_map)
    return np.count_nonzero(visible_tree_map)


@time_function()
def run_b(file):
    tree_map = convert_to_int(file)
    return max(get_scenic_scores(tree_map))


def convert_to_int(file: list[str]):
    return np.array([[int(char) for char in line] for line in file])


def set_horizontal_vis(tree_map: np.ndarray, visible_tree_map: np.ndarray):
    for y_index, tree_line in enumerate(tree_map):
        last_tree_height = -1
        for x_index, tree_height in enumerate(tree_line):
            if tree_height > last_tree_height:
                visible_tree_map[y_index, x_index] = 1
                last_tree_height = tree_height
        # reverse it!
        last_tree_height = -1
        for x_index, tree_height in enumerate(reversed(tree_line)):
            if tree_height > last_tree_height:
                visible_tree_map[y_index, len(tree_line) - x_index - 1] = 1
                last_tree_height = tree_height
    return visible_tree_map


def set_vertical_vis(tree_map: np.ndarray, visible_tree_map: np.ndarray):
    transposed_map = tree_map.transpose()
    transposed_visible_tree_map = visible_tree_map.transpose()
    for y_index, tree_line in enumerate(transposed_map):
        last_tree_height = -1
        for x_index, tree_height in enumerate(tree_line):
            if tree_height > last_tree_height:
                transposed_visible_tree_map[y_index, x_index] = 1
                last_tree_height = tree_height
        # reverse it!
        last_tree_height = -1
        for x_index, tree_height in enumerate(reversed(tree_line)):
            if tree_height > last_tree_height:
                transposed_visible_tree_map[y_index, len(tree_line) - x_index - 1] = 1
                last_tree_height = tree_height
    visible_tree_map = transposed_visible_tree_map.transpose()
    return visible_tree_map


def get_scenic_scores(tree_map: np.ndarray):
    scenice_scores = []
    for y_index, tree_line in enumerate(tree_map):
        for x_index, tree_height in enumerate(tree_line):
            visible_trees = []
            # look_right
            check_trees = tree_line[x_index + 1:]
            trees_visible = get_trees_visible(tree_line=check_trees, tree_height=tree_height)
            visible_trees.append(trees_visible)

            # look_left
            check_trees = np.flip(tree_line[:x_index])
            trees_visible = get_trees_visible(tree_line=check_trees, tree_height=tree_height)
            visible_trees.append(trees_visible)

            # look_up
            check_trees = np.flip(tree_map[:, x_index][:y_index])
            trees_visible = get_trees_visible(tree_line=check_trees, tree_height=tree_height)
            visible_trees.append(trees_visible)

            # look_down
            check_trees = tree_map[:, x_index][y_index + 1:]
            trees_visible = get_trees_visible(tree_line=check_trees, tree_height=tree_height)
            visible_trees.append(trees_visible)
            scenice_scores.append(np.product(visible_trees))
    return scenice_scores


def get_trees_visible(tree_line: np.ndarray, tree_height: int):
    trees_visi_count = 0
    for next_tree in tree_line:
        trees_visi_count += 1
        if next_tree >= tree_height:
            break
    return trees_visi_count


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

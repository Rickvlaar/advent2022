from copy import copy

from util import console, parse_file_as_list, time_function
from dataclasses import dataclass, field

test_file = parse_file_as_list('input/7_test.txt')
day_file = parse_file_as_list('input/7.txt')

MAX_DIR_SIZE = 100000
TOTAL_DISK_SPACE = 70000000
UPDATE_SIZE = 30000000


@dataclass
class Directory:
    parent: 'Directory'
    name: str
    files: list[tuple[int, str]] = field(init=True, default_factory=list)
    children: dict[str, 'Directory'] = field(init=True, default_factory=dict)
    size: int = 0

    def update_parent_sizes(self, file_size: int):
        if self.parent:
            self.parent.size += file_size
            self.parent.update_parent_sizes(file_size)


@time_function()
def run_a(file):
    instructions = copy(file)
    root_dir = Directory(name='root', parent=None)
    root_dir = map_harddisk(root_dir, instructions)
    all_dirs = []
    flatten_dirs(root_dir, all_dirs)
    return sum(get_deletable_dirs(all_dirs))


@time_function()
def run_b(file):
    instructions = copy(file)
    root_dir = Directory(name='root', parent=None)
    root_dir = map_harddisk(root_dir, instructions)
    disk_space_needed = UPDATE_SIZE - (TOTAL_DISK_SPACE - root_dir.size)
    all_dirs = []
    flatten_dirs(root_dir, all_dirs)
    return get_minimal_delete_size(all_dirs, disk_space_needed)


def map_harddisk(root_dir: Directory, file: list[str]):
    current_dir = root_dir

    while file:
        instruction = file.pop(0)
        if 'cd' in instruction:
            target_dir = instruction.split(' ').pop()
            if target_dir == '..':
                current_dir = current_dir.parent
            elif target_dir in current_dir.children:
                current_dir = current_dir.children[target_dir]

        if 'ls' in instruction:
            contents = []
            while True:
                if not file or file[0].startswith('$'):
                    break
                contents.append(file.pop(0))

            process_contents(contents=contents, current_dir=current_dir)

    return root_dir


def process_contents(contents: list[str], current_dir: Directory):
    for line in contents:
        splitline = line.split(' ')
        prefix = splitline[0]
        name = splitline[1]
        if prefix == 'dir':
            child_dir = Directory(name=name, parent=current_dir)
            current_dir.children[name] = child_dir
        else:
            file_size = int(prefix)
            file = (file_size, name)
            current_dir.size += file_size
            current_dir.update_parent_sizes(file_size)
            current_dir.files.append(file)


def flatten_dirs(dir: Directory, all_dirs: list[int]):
    all_dirs.append(dir.size)
    if dir.children:
        for child in dir.children.values():
            flatten_dirs(child, all_dirs)


def get_deletable_dirs(dirs: list[int]):
    return [size for size in dirs if size <= MAX_DIR_SIZE]


def get_minimal_delete_size(dirs: list[int], disk_space_needed: int):
    dirs.sort()
    for size in dirs:
        if size > disk_space_needed:
            return size


if __name__ == '__main__':
    answer_a = run_a(day_file)
    answer_b = run_b(day_file)

    console.print(f'solution A: {answer_a}')
    console.print(f'solution B: {answer_b}')

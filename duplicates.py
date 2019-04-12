import os
import sys
from collections import defaultdict


def generate_dict_of_files(dirname):
    files_locations = defaultdict(list)
    for (this_dir, _, files) in os.walk(dirname):
        for filename in files:
            full_path = os.path.join(this_dir, filename)
            file_size = os.path.getsize(full_path)
            files_locations[(filename, file_size)].append(full_path)
    return files_locations


def print_similar_files(dict_files):
    for (filename, file_size), paths in dict_files.items():
        if len(paths) > 1:
            print('{} {}'.format(filename, file_size))
            for path in paths:
                print(path)
            print('_' * 40)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        sys.exit('Введите стартовую директорию')
    if os.path.isdir(root):
        print_similar_files(generate_dict_of_files(root))
    else:
        print('Директория не найдена')

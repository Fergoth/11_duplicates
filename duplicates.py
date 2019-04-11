import os
import sys


def generate_dict_of_files(dirname):
    dict_files = {}
    for (this_dir, _, files) in os.walk(dirname):
        for filename in files:
            fullpath = os.path.join(this_dir, filename)
            file_size = os.path.getsize(fullpath)
            if (filename, file_size) in dict_files:
                dict_files[(filename, file_size)].append(fullpath)
            else:
                dict_files[(filename, file_size)] = [fullpath]
    return dict_files


def print_similar_files(dict_files):
    for key in dict_files:
        if len(dict_files[key]) > 1:
            print('{} {}'.format(key[0], key[1]))
            for path in dict_files[key]:
                print(path)
            print('_' * 40)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        sys.exit('Введите стартовую директорию')
    if os.path.exists(root):
        print_similar_files(generate_dict_of_files(root))
    else:
        print('Директория не найдена')

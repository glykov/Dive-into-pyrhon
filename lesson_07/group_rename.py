import os

folder = "d:\\test_02"

def group_rename(original: str, replacement: str, num_digits: int, orig_ext: str, repl_ext: str, orig_part: list) -> None:
    counter = 1
    filler = 0
    with os.scandir(path=folder) as contents:
        for entry in contents:
            if (entry.name.find(original) != -1 and entry.is_file() and entry.name[entry.name.rfind('.') + 1:] == orig_ext):
                print(entry.name)
                new_name = f'{original[orig_part[0]:orig_part[1]]}{replacement}_{counter:{filler}{num_digits}}.{repl_ext}'
                print(new_name)
                os.rename(folder + '\\' + entry.name, folder + '\\' + new_name)
                counter += 1


if __name__ == '__main__':
    group_rename('test', '_file', 3, 'txt', 'doc', [0, 4])

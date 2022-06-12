#!/usr/bin/env python
from gendiff.parser import prepare_file


def true_style(file):
    if file is None:
        return 'null'
    elif isinstance(file, bool):
        return str(file).lower()
    else:
        return file


def generate_diff(first_file, second_file):
    answer = "{\n"
    data_first_file = prepare_file(first_file)
    data_second_file = prepare_file(second_file)
    keys = sorted(data_first_file | data_second_file)
    for key in keys:
        prefix = ''
        if key in data_first_file:
            prefix = '-'
            if data_second_file.get(key) == data_first_file.get(key):
                prefix = ' '
            answer += f'  {prefix} {key}: {true_style(data_first_file[key])}\n'
        if key in data_second_file and prefix != ' ':
            prefix = '+'
            answer += f'  {prefix} {key}: ' \
                      f'{true_style(data_second_file[key])}\n'
    answer += '}'
    return answer

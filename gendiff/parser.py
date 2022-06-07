import argparse
import os
import yaml
import json


def parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output', default='json')
    return parser.parse_args()


def get_format(file_path):
    file_format = os.path.splitext(file_path)[1]
    return file_format



def open_file(file_path):
    with open(os.path.abspath(f'gendiff/tests/fixtures/{file_path}')) as f:
        file = f.read()
    return file


def parse_file(file_format):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    return format[file_format.lower()]


def prepare_file(file_path):
    file_format = get_format(file_path)
    file = open_file(file_path)
    open_type = parse_file(file_format)
    return open_type(file)

#!/usr/bin/env python
from gendiff.logic import generate_diff
from gendiff.parser import parser


def main():
    args = parser()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

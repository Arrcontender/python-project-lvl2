import itertools


def stylish(value: dict, replacer=' ', spaces_count=2):
    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        if depth == 0:
            deep_indent_size = depth + spaces_count
            current_indent = replacer * depth
        else:
            deep_indent_size = depth + spaces_count + 2
            current_indent = replacer * (depth + 2)
        deep_indent = replacer * deep_indent_size
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)


def sort_diff(dictionary):
    for key in dictionary:
        if isinstance(dictionary[key], dict):
            dictionary[key] = sort_diff(dictionary[key])

    sorted_tuple = sorted(dictionary.items(), key=lambda x: x[0][2:])
    return dict(sorted_tuple)

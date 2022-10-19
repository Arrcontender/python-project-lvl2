from gendiff.file_parser import json_parse, yaml_parse


def generate_diff(file1, file2):
    if '.json' in file1 and '.json' in file2:
        parsed_file1, parsed_file2 = json_parse(file1), json_parse(file2)
    else:
        parsed_file1, parsed_file2 = yaml_parse(file1), yaml_parse(file2)

    data1, data2 = parsed_file1, parsed_file2

    diff1, diff2 = list(), list()

    for k, v in data1.items():
        if k in data2:
            if data1[k] == data2[k]:
                diff1.append(f'    {k}: {data1[k]}')
            else:
                diff1.append(f'  - {k}: {data1[k]}')
        else:
            diff1.append(f'  - {k}: {data1[k]}')

    for k, v in data2.items():
        if k in data1:
            if data2[k] != data1[k]:
                diff2.append(f'  + {k}: {data2[k]}')
        else:
            diff2.append(f'  + {k}: {data2[k]}')

    diff = diff1 + diff2
    diff.sort(key=lambda i: i[4])
    for i, v in enumerate(diff):
        diff[i] = ''.join(map(lambda x: str(x).lower(), v))
    diff.insert(0, '{')
    diff.append('}')
    res = '\n'.join(diff)
    return res

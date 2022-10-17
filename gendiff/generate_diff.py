import json


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))

    diff1 = []
    diff2 = []

    for key in data1.keys():
        if key in data2:
            if data1[key] == data2[key]:
                diff1.append(('    ', key + ': ', data1[key]))
            else:
                diff1.append(('  - ', key + ': ', data1[key]))
        else:
            diff1.append(('  - ', key + ': ', data1[key]))

    for key in data2.keys():
        if key in data1:
            if data2[key] != data1[key]:
                diff2.append(('  + ', key + ': ', data2[key]))
        else:
            diff2.append(('  + ', key + ': ', data2[key]))

    diff = diff1 + diff2
    diff.sort(key=lambda i: i[1])
    for i, v in enumerate(diff):
        diff[i] = ''.join(map(lambda x: str(x).lower(), v))
    diff.insert(0, '{')
    diff.append('}')
    res = '\n'.join(diff)
    return res



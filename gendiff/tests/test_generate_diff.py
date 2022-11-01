from gendiff.generate_diff import generate_diff


def test_generate_diff_type_json():
    y = generate_diff('gendiff/tests/fixtures/file1.json',
                      'gendiff/tests/fixtures/file2.json')
    assert isinstance(y, str), 'Неверный тип результирующего файла'


def test_generate_diff_json():
    y = generate_diff('gendiff/tests/fixtures/file1.json',
                      'gendiff/tests/fixtures/file2.json')
    with open('gendiff/tests/fixtures/true_json.txt', 'r') as expected:
        assert expected.read() == y, 'Результат сравнения неверен'


def test_generate_diff_type_yaml():
    y = generate_diff('gendiff/tests/fixtures/file1.yml',
                      'gendiff/tests/fixtures/file2.yml')
    assert isinstance(y, str), 'Неверный тип результирующего файла'


def test_generate_diff_yaml():
    y = generate_diff('gendiff/tests/fixtures/file1.yml',
                      'gendiff/tests/fixtures/file2.yml')
    with open('gendiff/tests/fixtures/true_yaml.txt', 'r') as expected:
        assert expected.read() == y, 'Результат сравнения неверен'


def test_nested_json():
    first_file = 'gendiff/tests/fixtures/nested/nested_file1.json'
    second_file = 'gendiff/tests/fixtures/nested/nested_file2.json'
    with open('gendiff/tests/fixtures/nested/true_nested.txt', 'r') \
            as expected:
        assert generate_diff(first_file, second_file) == expected.read()


def test_nested_yaml():
    first_file = 'gendiff/tests/fixtures/nested/nested_file1.yml'
    second_file = 'gendiff/tests/fixtures/nested/nested_file2.yml'
    with open('gendiff/tests/fixtures/nested/true_nested.txt', 'r') \
            as expected:
        assert generate_diff(first_file, second_file) == expected.read()

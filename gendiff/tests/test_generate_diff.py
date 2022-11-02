from gendiff.generate_diff import generate_diff
import pytest
from gendiff.formatter.plain import compose_diff, plain


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


def test_json_plain_format():
    first_file = 'gendiff/tests/fixtures/nested/nested_file1.json'
    second_file = 'gendiff/tests/fixtures/nested/nested_file2.json'
    with open('gendiff/tests/fixtures/plain/plain_formatter_expected.txt',
              'r') as expected:
        assert generate_diff(first_file, second_file,
                             format=plain) == expected.read()


def test_yaml_plain_format():
    first_file = 'gendiff/tests/fixtures/nested/nested_file1.yml'
    second_file = 'gendiff/tests/fixtures/nested/nested_file2.yml'
    with open('gendiff/tests/fixtures/plain/plain_formatter_expected.txt',
              'r') as expected:
        assert generate_diff(first_file, second_file,
                             format=plain) == expected.read()


@pytest.fixture
def decompose():
    return {
        "+ cookie": 'milk',
        "- cookie": 'drink',
        "+ honey": 'bee',
        "  nested": {
            '- cool': 'wow',
            '+ cool': 'not wow',
            '  good': 'very'
        }
    }


@pytest.fixture
def expected_compose():
    return {
        "-+cookie": 'drink',
        "+ honey": 'bee',
        "  nested": {
            '-+cool': 'wow',
            '  good': 'very'
        }
    }


def test_compose_diff(decompose, expected_compose):
    value = decompose
    expected = expected_compose
    updated_expected = {
        "-+cookie": 'milk',
        '-+cool': 'not wow'
    }
    updated = compose_diff(value)
    assert updated == updated_expected
    assert value == expected

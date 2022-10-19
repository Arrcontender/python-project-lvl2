from gendiff.generate_diff import generate_diff
from gendiff.tests.fixtures.true_json import json_true
from gendiff.tests.fixtures.true_yaml import yaml_true


def test_generate_diff_type_json():
    y = generate_diff('gendiff/tests/fixtures/file1.json',
                      'gendiff/tests/fixtures/file2.json')
    assert isinstance(y, str), 'Неверный тип результирующего файла'


def test_generate_diff_json():
    y = generate_diff('gendiff/tests/fixtures/file1.json',
                      'gendiff/tests/fixtures/file2.json')
    assert json_true == y, 'Результат сравнения неверен'


def test_generate_diff_type_yaml():
    y = generate_diff('gendiff/tests/fixtures/file1.yml',
                      'gendiff/tests/fixtures/file2.yml')
    assert isinstance(y, str), 'Неверный тип результирующего файла'


def test_generate_diff_yaml():
    y = generate_diff('gendiff/tests/fixtures/file1.yml',
                      'gendiff/tests/fixtures/file2.yml')
    assert yaml_true == y, 'Результат сравнения неверен'

from gendiff.generate_diff import generate_diff
from gendiff.tests.fixtures.true_json import json_true


def test_generate_diff_json():
    y = generate_diff('gendiff/tests/fixtures/file1.json',
                      'gendiff/tests/fixtures/file2.json')
    assert json_true == y, 'Результат сравнения неверен'

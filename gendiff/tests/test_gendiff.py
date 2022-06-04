from gendiff.logic import generate_diff
import pytest
import os


@pytest.mark.parametrize(
    'first_file, second_file, file_result',
    [
        ('gendiff/tests/fixtures/file1.json',
         'gendiff/tests/fixtures/file2.json',
         'gendiff/tests/fixtures/result_json')
    ],
)
def test_generate_diff(first_file, second_file, file_result):
    with open(os.path.abspath(file_result)) as file:
        result = file.read()
    assert generate_diff(first_file, second_file) == result
    assert type(result) == str
    assert type(generate_diff(first_file, second_file)) == str

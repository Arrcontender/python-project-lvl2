build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
		poetry run gendiff

gendiff-json:
		poetry run gendiff gendiff/tests/fixtures/file1.json gendiff/tests/fixtures/file2.json

lint:
		poetry run flake8 gendiff
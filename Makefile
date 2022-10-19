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

test:
	poetry run pytest --cov

check:
	poetry run flake8 gendiff
	poetry run pytest --cov

test-coverage:
	poetry run pytest --cov=tests/ --cov-report xml

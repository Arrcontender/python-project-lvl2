gendiff json:
	poetry run gendiff file1.json file2.json

gendiff yaml:
	poetry run gendiff file1.json file2.yaml

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --user --force-reinstall  dist/*.whl

install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
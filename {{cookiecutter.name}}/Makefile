PACKAGE=$(shell ./setup.py --name)
  
all: test type lint sort format package;

venv:
	python{{cookiecutter.python}} -m venv venv --clear
	venv/bin/pip install --editable .
	venv/bin/pip install -r requirements.txt

test: venv
	venv/bin/pytest tests

type: venv
	venv/bin/mypy ${PACKAGE}

lint: venv
	venv/bin/pylint ${PACKAGE}

sort: venv
	venv/bin/isort --apply --recursive ${PACKAGE}

format: venv
	venv/bin/black --quiet --line-length 79 ${PACKAGE}

add:
	git add --all ${PACKAGE}/*.py

hook:
	git config core.hooksPath hooks/

clean:
	find . -name '*.whl' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

package: venv
	venv/bin/python setup.py bdist_wheel --universal

publish: clean package
	venv/bin/twine upload --repository pypi dist/*.whl

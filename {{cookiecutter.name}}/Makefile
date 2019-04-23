PACKAGE=$(shell python setup.py --name)
  
all: test type lint sort format addall distribute;

hook:
	git config core.hooksPath hooks/

venv:
	python -m venv venv --clear
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

addall:
	git add --all ${PACKAGE}/*.py

cleanall:
	find . -name '*.whl' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

distribute: venv
	venv/bin/python setup.py bdist_wheel --universal

publish: cleanall distribute
	.venv/bin/twine upload -r pypi dist/*.whl

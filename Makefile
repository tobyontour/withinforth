test:
	python setup.py pytest

build:
	python setup.py bdist_wheel

venv:
	python3 -m venv venv
	venv/pip3 install -r requirements.txt


CWD?= $(realpath $(dir $(firstword $(MAKEFILE_LIST))))
PIP:= ${CWD}/bin/pip
PYTHON:= ${CWD}/bin/python

BASE?=setuptools wheel numpy cython

.DEFAULT: venv
venv: ${PYTHON}
${PYTHON}: requirements.txt
	python3 -mvenv ${CWD}
	${PIP} install --upgrade pip
	${PIP} install --upgrade ${BASE}
	${PIP} install -r requirements.txt

.PHONY: clean
clean:
	@git clean -xfd

requirements.txt:
	@echo requirements.txt is missing.

Data:
	@echo Generating faux data
	${PYTHON} 01_MakeMDF-Data.py
	@echo Done generating faux data.

.PHONY: index
index: mdf_index.sqlite

mdf_index.sqlite: Data
	${PYTHON} 02_IndexMDF-Data.py


.PHONY: lazy
lazy:
	autopep8 --in-place --aggressive --aggressive --aggressive *.py
	isort --apply *.py

.PHONY: sprint
sprint:
	/bin/sh .sprintcommit

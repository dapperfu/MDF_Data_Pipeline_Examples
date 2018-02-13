VENV?=.venv
PIP?=${VENV}/bin/pip
PYTHON?=${VENV}/bin/python

BASE?=setuptools wheel numpy runcython3

.DEFAULT: venv
venv: ${VENV}
${VENV}: requirements.txt
	python3 -mvenv ${VENV}
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

mdf_index.sqlite: Data
	${PYTHON} 02_IndexMDF-Data.py

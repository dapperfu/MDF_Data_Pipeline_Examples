# Config
# Makefile directory
MK_DIR = $(realpath $(dir $(firstword $(MAKEFILE_LIST))))

# Project name
PROJ ?= $(notdir ${MK_DIR})
# Virtual environment path
VENV ?= ${MK_DIR}
# Hostname
HOST:=$(shell hostname).local
# Executable paths
PIP:=${VENV}/bin/pip
PYTHON:=${VENV}/bin/python

# Base python modules to install before everything else
# Some projects need wheel, numpy and cython
# before they will install correctly.
BASE_MODULES?=setuptools wheel numpy cython

# Targets

## Default
.DEFAULT: all
.PHONY: all
all:
	$(error No default target)

## Environment Setup & Teardown
.PHONY: venv
venv: ${PYTHON}

${PYTHON}: requirements.txt
	${MAKE} clean
	python3 -mvenv ${VENV}
	${PIP} install --upgrade pip
	${PIP} install --upgrade ${BASE_MODULES}
	${PIP} install --upgrade --requirement ${<}
	
requirements.txt:
	@echo requirements.txt is missing.

.PHONY: clean
clean:
	@echo ---- Cleaning ${PROJ} ----
	@git clean -xfd
	
## Action Targets
.PHONY:nb
nb:
	screen -S ${PROJ} -d -m bin/jupyter-notebook --ip=${HOST}
	
.PHONY:worker
worker:
	${PYTHON} worker.py

.PHONY: lazy
lazy:
	autopep8 --in-place --aggressive --aggressive --aggressive *.py
	isort --apply *.py
	
## File Targets

### Create fake data
Data:
	@echo --- Generating faux data --- 
	${PYTHON} 01_MakeMDF-Data.py
	@echo Done generating faux data.

### Index the data.
.PHONY: index
index: mdf_index.sqlite
mdf_index.sqlite: Data
	${PYTHON} 02_IndexMDF-Data.py

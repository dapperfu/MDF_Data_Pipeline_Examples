VENV?=.venv
PIP?=${VENV}/bin/pip
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

.PHONY: deb
deb:
	apt-get install python3 python3-venv python3-pip

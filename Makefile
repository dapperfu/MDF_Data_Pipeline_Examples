# Config

## Targets
# Do nothing.
.PHONY: null
null:
	@$(error No Default Target).

ifeq ("${MK_DIR}", "${SANDWICH_DIR}")
	@echo Equal
	# ${MK_DIR}
	# ${SANDWICH_DIR}
endif

ifneq ("${MK_DIR}", "${SANDWICH_DIR}")
	@echo Unequal
	# ${MK_DIR}
	# ${SANDWICH_DIR}
endif

.PHONY: env
env:
	${MAKE} -C ${MK_DIR} env.python
	${MAKE} -C ${MK_DIR} env.python

.PHONY: deb
deb:
	apt-get install python3 python3-venv python3-pip

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

include $(realpath .mk_inc/env.mk)

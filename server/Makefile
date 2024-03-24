
ROOT_DIR:=./
CURR_DIR:=$(shell "pwd")
VENV_BIN_DIR:=venv
PYTHON:=$(VENV_BIN_DIR)/bin/python3

.PHONY: venv run migrate

venv:
	source ${ROOT_DIR}$(VENV_BIN_DIR)/bin/activate
run: venv
	 $(PYTHON) $(ROOT_DIR)manage.py runserver 0.0.0.0:8000

migrate: venv
	 $(PYTHON) $(ROOT_DIR)manage.py migrate

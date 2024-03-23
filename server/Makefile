
ROOT_DIR:=./
CURR_DIR:=$(shell "pwd")
VENV_BIN_DIR:=venv
CDM_FROM_ENV:="$(CURR_DIR)$(VENV_BIN_DIR)/activate; which"
PYTHON:=$(VENV_BIN_DIR)/bin/python

.PHONY: runserver migrate
venv:
	source $(VENV_BIN_DIR)/bin/activate
run: venv 
	 $(PYTHON) $(ROOT_DIR)manage.py runserver 0.0.0.0:8000

migrate: venv
	 $(PYTHON) $(ROOT_DIR)manage.py migrate

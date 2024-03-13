VENV_DIR := venv
MAIN_FILE := main.py
REQUIREMENTS_FILE := requirements.txt

.PHONY: all venv check_venv install run

all: venv check_venv install run

venv:
	@echo "Creating virtual environment..."
	@python -m venv $(VENV_DIR)

check_venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Virtual environment is not activated. Please activate to proceed. Type 'source ${VENV_DIR}/bin/activate' to activate."; \
		exit 1; \
	else \
        echo "Virtual environment is activated at: $$VIRTUAL_ENV"; \
	fi

install: venv $(REQUIREMENTS_FILE)
	@echo "Installing dependencies..."
	@pip install -r $(REQUIREMENTS_FILE)

run: $(MAIN_FILE)
	@echo "Running the program..."
	@python $(MAIN_FILE)

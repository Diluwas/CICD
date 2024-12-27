# Define a variable for the Python path 
PYTHONPATH = src

# Command for Unix-like systems 
test-unix: 
	PYTHONPATH=$(PYTHONPATH) pytest tests/

# Command for Windows 
test-windows: 
	set PYTHONPATH=$(PYTHONPATH) && pytest tests/

venv:
	python -m venv .venv
	eacho "Please run 'source .venv/Scripts/activate"

dev:
	pip install -r src/api/requirements.txt
	pip install -r requirements-dev.txt

test:
ifeq ($(OS),Windows_NT)
	$(MAKE) test-windows
else 
	$(MAKE) test-unix endif
endif

lint:
	flake8 src/ tests/
	tflint terraform/
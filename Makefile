lint:
	black . --check --diff
	flake8 src --max-complexity=5 --max-line-length=95
	isort . --check-only --diff

format:
	isort .
	black .

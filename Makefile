.PHONY: check test

check:
	uv run --no-project python -B scripts/check_repository.py

test:
	PYTHONPATH=src uv run --no-project python -B -m unittest discover -s tests

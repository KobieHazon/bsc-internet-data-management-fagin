.PHONY: check test

check: test

test:
	PYTHONPATH=src uv run --no-project python -B -m unittest discover -s tests

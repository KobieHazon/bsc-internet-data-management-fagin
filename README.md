# Internet Data Management: Fagin's Algorithm

- Authors: Kobie Hazon and Adi Eldar.

The supplied exercise files are in `assignment/`. My code is kept separately, along with the data and answers.

## Project Summary

A Python implementation of Fagin's top-k aggregation algorithm with small CSV ranking fixtures and output.

## Tech Stack

Python 3, CSV, top-k aggregation, Fagin algorithm.

## Validate

Run:

```sh
make check
make test
```

No third-party Python packages are required.

The tests execute both ranking algorithms on local inputs and check their results. No network access is required.

## Written answers

My submission with Adi Eldar is in [written-answers.pdf](solution/written-answers.pdf).

## Repository layout

- `src/`: Python implementations.
- `assignment/`: Exercise briefs and supplied inputs.
- `data/`: Input data and test fixtures.
- `solution/`: Written answers.
- `results/`: Submitted output files.
- `tests/`: Executable regression tests.
- `scripts/`: Repository checks and optional live-web tests.

Run `make check` and `make test` from the repository root. The tests use local fixtures; they do not scrape live websites.

Example: `uv run --no-project python src/question2a.py data/data1.csv data/data2.csv data/data3.csv`.

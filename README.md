# Internet Data Management: Fagin's Algorithm

The supplied exercise files are in `assignment/`. My code is kept separately, along with the data and answers.

Submission ZIP files, Apple metadata, official solution PDFs, and exported answer documents and PDFs are not included.

## Project Summary

A Python implementation of Fagin's top-k aggregation algorithm with small CSV ranking fixtures and recovered output.

## Tech Stack

Python 3, CSV, top-k aggregation, Fagin algorithm.

## Validate

Run:

```sh
make check
```

No third-party Python packages are required for the static validator.

The validator is static and does not access the network. Original scraping scripts may require live web access if run directly.

## Repository layout

- `src/`: authored Python scripts, preserving the coursework filenames and sibling imports.
- `data/`: recovered reference data or HTML/CSV fixtures.
- `assignment/`: supplied exercise material, unchanged.
- `tests/` and `scripts/`: offline regression checks and repository validation.
- `results/` or `solution/` (where present): recovered outputs and written/XML answers.
- `run-results/` (where used): ignored output from new runs, separate from recovered evidence.

Run `make check` and `make test` from the repository root. The tests use local fixtures; they do not scrape live websites.

Example: `uv run --no-project python src/question2a.py data/data1.csv data/data2.csv data/data3.csv`.

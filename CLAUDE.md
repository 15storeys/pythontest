# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal scratch/learning space, not a packaged application. There is no git repo, no `requirements.txt`/`pyproject.toml`, no tests, and no build or lint tooling. Contents are unrelated, standalone pieces:

- `converter.py` — a standalone CLI unit-conversion tool.
- `my_favourites.ipynb`, `testnotebook.ipynb` — Jupyter notebooks used for ad-hoc data exploration (pandas/matplotlib), unrelated to `converter.py`.
- `myenv/` — a local Python 3.14 virtualenv with Jupyter, pandas, numpy, and matplotlib installed. Not committed to version control in a normal project; treat as local environment state, not source.

## Running things

Run the converter directly with the system `python3`, no venv needed:

```
python3 converter.py
```

For notebook work, use the `myenv` virtualenv:

```
source myenv/bin/activate
jupyter lab      # or: jupyter notebook
```

## `converter.py` architecture

Menu-driven CLI built around a dispatch table, `CONVERSIONS`, mapping a menu key to `(label, prompt_function)`. `main()` prints the menu from this dict, reads the user's choice, and calls the matching prompt function — there's no other branching logic.

Each conversion is a pair of functions:
- a pure conversion function (e.g. `stones_pounds_to_kg(stones, pounds)`) that does the math and is easy to test/reuse independently of I/O.
- a `_prompt` wrapper (e.g. `stones_pounds_to_kg_prompt()`) that calls `input()`, invokes the conversion function, and prints the result.

To add a new conversion: write the pure conversion function, write its `_prompt` wrapper, and add an entry to `CONVERSIONS` with the next free key and a label.

# Curated Python course/practice notes

This note records the useful learning themes from two older standalone repositories without copying their course assets wholesale.

## `python-mastery-ztm`

Durable themes:
- decorators and functional-style exercises
- exception/error-handling practice
- unittest/pytest-style testing exercises
- small automation scripts such as image conversion and scraping
- introductory Selenium browser automation
- early data-science notebooks

Intentionally not migrated:
- the 9 MB FIFA dataset
- generated/static website assets
- model artefacts
- course-completeness material that is better referenced at its original source

The Selenium exercise is retained conceptually as an example of explicit waits, stable locators, clean teardown and keeping tests independent from public demo sites.

## `hotels_py_intro`

This repository was an early teaching workspace for Python, Jupyter, scraping, stock-data reading and visualisation.

Durable teaching progression:
1. Python syntax and data structures
2. files and external data
3. HTTP/scraping fundamentals
4. tabular analysis
5. visualisation
6. turning notebook experiments into importable/testable modules

Intentionally not migrated:
- `.ipynb_checkpoints`
- rendered HTML output
- bundled CSV datasets
- the external Git cheat-sheet PDF

Modern teaching material should prefer reproducible environments (`uv`/`pyproject.toml`), scripts/modules beside notebooks, and tests for reusable logic.

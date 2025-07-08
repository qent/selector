# Development Guidelines

This repository follows modern Python best practices.

* All new code **must** use explicit type hints and pass `mypy` type checking.
* Format code with `black` and organize imports with `isort`.
* Tests are written with `pytest`. Always run `pytest` before committing.
* Keep functions short and well documented with docstrings.
* Prefer standard library functionality over external dependencies unless required.

Run the following commands before pushing changes:

```bash
isort .
black .
pytest
```

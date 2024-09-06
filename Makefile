
start: install-deps
	poetry run uvicorn main:app

install-deps:
	poetry install

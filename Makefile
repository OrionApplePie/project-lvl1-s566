all: install lint

install:
	@poetry install

lint:
	@poetry run flake8 brain_games

.PHONY: all install lint
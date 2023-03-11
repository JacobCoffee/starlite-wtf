test-examples:  ## Run `examples` tests
	@poetry run pytest examples

test: ## Run `tests` tests
	@poetry run pytest tests

test-all: test test-examples ## Run all tests

clean:       ## remove all build, testing, and static files
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.ipynb_checkpoints' -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache

lint-checkonly:        ## perform non-changing linting and formatting
    @poetry run ruff check .
    @poetry run black . --check

lint:        ## perform linting and formatting
    @poetry run ruff check . --fix
    @poetry run black .

build-release:          ## Build a new release
    clean
    @poetry build

publish-release:          ## Publish a new release on PyPI
    clean
    @poetry publish

release:          ## Build and publish a new release on PyPI
    clean
    @poetry publish --build

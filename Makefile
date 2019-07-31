run:
	pipenv run python -u application.py
test:
	pytest --cov=src --cov-report=term-missing -s
test-report:
	coverage html
lint:
	flake8 src
lint-fix:
	autopep8 --in-place --recursive --aggressive src/ application.py

run:
	pipenv run python -u application.py
test:
	pytest --cov=src --cov-report=term-missing -s
test-report:
	coverage html
lint:
	pycodestyle --show-source src application.py
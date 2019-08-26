run:
	gunicorn -w 1 -b 0.0.0.0:5000 wsgi:instance_app
dev-run:
	python application.py
test:
	pytest --cov=src --cov-report=term-missing -s
test-report:
	coverage html
lint:
	flake8 src
lint-fix:
	autopep8 --in-place --recursive --aggressive src/ application.py

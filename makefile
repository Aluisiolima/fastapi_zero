run:
	uvicorn fastapi_zero.app:app --reload --host 0.0.0.0

test:
	make format
	pytest -v --cov=fastapi_zero --cov-report=term-missing

lint:
	ruff check .

format:
	ruff format .

format: 
	uvx ruff format app/

check: format
	uvx ruff check app/

lint: check
	uv run pyright app/
	
run: lint
	uv run python app/main.py

test:
	uv run pytest -sv

docker-up:
	docker-compose up -d

docker-down-v:
	docker-compose down

docker-down-v:
	docker-compose down -v

docker-logs:
	docker compose logs --tail 100 app


up:
	docker compose up

up-build:
	docker compose up --build

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f

ps:
	docker compose ps

shell:
	docker compose exec api bash

migrate:
	docker compose exec api python manage.py migrate

makemigrations:
	docker compose exec api python manage.py makemigrations

restart:
	docker compose restart && docker compose down && docker compose up -d

createsuperuser:
	docker compose exec api python manage.py createsuperuser
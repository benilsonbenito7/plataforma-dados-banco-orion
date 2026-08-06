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

createsuperuser:
	docker compose exec api python manage.py createsuperuser

restart:
	docker compose down
	docker compose up -d

clean:
	docker compose down --volumes --remove-orphans
	docker system prune -af
	docker volume prune -f
	docker network prune -f

reset:
	docker compose down --volumes --remove-orphans
	docker system prune -af
	docker volume prune -f
	docker network prune -f
	docker compose up --build -d
	docker compose exec api python manage.py migrate
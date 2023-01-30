build:
	docker-compose -f local.yml up --build -d --remove-orphans

up:
	docker-compose -f local.yml up -d


down:
	docker-compose -f local.yml down

logs:
	docker-compose -f local.yml logs

migrate:
	docker-compose -f local.yml run --rm api python3 manage.py migrate

makemigration:
	docker-compose -f local.yml run --rm api python3 manage.py makemigrations

collectstatic:
	docker-compose -f local.yml run --rm api python3 manage.py collectstatic --no-input --clear


superuser:
	docker-compose -f local.yml run --rm api python3 manage.py createsuperuser

down-v:
	docker-compose -f local.yml down -v


volume:
	docker volume inspect authors-src_local_postgres_data

authors-db:
	docker-compose -f local.yml exec postgres psql --username=vince --dbname=authors-live

flake8:
	docker-compose -f local.yml exec api flake8 .

black-check:
	docker-compose -f local.yml exec api black --check --exclude=makemigrations .

black-diff:
	docker-compose -f local.yml exec api black --diff --exclude=makemigrations .

black:
	docker-compose -f local.yml exec api black --exclude=makemigrations .

isort-check:
	docker-compose -f local.yml exec api isort . --check-only --skip env --skip makemigrations


isort-diff:
	docker-compose -f local.yml exec api isort . --diff --skip env --skip makemigrations

isort:
	docker-compose -f local.yml exec api isort . --skip env --skip makemigrations

	
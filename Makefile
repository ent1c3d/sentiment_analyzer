install:
	docker-compose run --rm server pip install -r requirements-dev.txt --user --upgrade

start:
	docker-compose up server

stop:
	docker-compose stop

daemon:
	docker-compose up -d server

tests:
	docker-compose run --rm testserver

lint:
	docker-compose run --rm server bash -c "python -m flake8 ./src ./test"

gc:
	docker exec sentiment_analysis_server python src/manage.py gc

db/connect:
	docker exec -it sentiment_analysis_db psql -Upostgres

db/seed:
	docker-compose run --rm server python src/manage.py seed


db/downgrade:
	docker-compose run --rm server python src/manage.py db downgrade

db/upgrade:
	docker-compose run --rm server python src/manage.py db upgrade

db/migrate:
	docker-compose run --rm server python src/manage.py db migrate

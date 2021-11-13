IMAGE=backend

.PHONY: build
build:
	docker-compose build
start:
	docker-compose up
stop:
	docker-compose stop
down:
	docker-compose down
shell:
	docker-compose exec ${IMAGE} /bin/bash
run:
	docker-compose exec ${IMAGE} ${args}
migrate:
	docker-compose exec ${IMAGE} python manage.py migrate
makemigrations:
	docker-compose exec ${IMAGE} python manage.py makemigrations
createsuperuser:
	docker-compose exec ${IMAGE} python manage.py createsuperuser
collectstatic:
	docker-compose run backend python manage.py collectstatic
clean-mysql:
	./scripts/mysql/reset.sh
format:
	docker-compose exec ${IMAGE} black .
watch:
	docker-compose exec ${IMAGE} watchmedo tricks-from tricks.yml
restart: down start

init : build project app chown

migrate :
	docker-compose run web python manage.py makemigrations myapp
	docker-compose run web python manage.py migrate

project :
	docker-compose run web django-admin.py startproject mysite .

app :
	docker-compose run web python manage.py startapp myapp

chown :
	sudo chown -R francis:francis .

delete :
	docker rmi `docker images -q`

ps :
	docker ps -a
	docker-compose ps

build:
	docker-compose build

up:
	docker-compose up -d

down :
	docker-compose down

start:
	docker-compose start

stop:
	docker-compose stop

shell-nginx:
	docker exec -ti ng01 bash

shell-web:
	docker exec -ti web bash

shell-db:
	docker exec -ti db bash

shell-cron:
	docker exec -ti cron bash

log-nginx:
	docker-compose logs nginx

log-tasker:
	docker-compose logs tasker

log-web:
	docker-compose logs web

log-db:
	docker-compose logs db

collectstatic:
	docker exec dg01 /bin/sh -c "python manage.py collectstatic --noinput"

clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -qr requirements.txt

test: deps clean
	@python manage.py test

jasminedeps: deps
	@pip install -qr test_requirements.txt

jasmine: jasminedeps
	@jasmine-splinter -f `pwd`/pythonbrasil8/static_files/tests/jasmine/SpecRunner.html -b chrome

setup: deps
	@python manage.py syncdb
	@python manage.py migrate
	@python manage.py loaddata pythonbrasil8/fixtures/initial_data.json

settings:
	cp pythonbrasil8/settings_local.py{.example,}

run:
	@python manage.py runserver 0.0.0.0:8000

translate:
	@cd pythonbrasil8 && django-admin.py makemessages -a && django-admin.py compilemessages

remote_migrate:
	@heroku run python manage.py syncdb --noinput
	@heroku run python manage.py migrate

collectstatic:
	@heroku run python manage.py collectstatic --noinput

heroku:
	@git push heroku master

deploy: heroku remote_migrate collectstatic

help:
	@grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'

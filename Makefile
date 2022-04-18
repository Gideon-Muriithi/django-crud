install:
	pipenv install

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python manage.py createsuperuser

# is this necessary without the extra static?
collectstatic:
	python manage.py collectstatic

set_env_vars:
	@[ -f .env ] && source .env

serve:
	python3 manage.py runserver

shell:
	python3 manage.py shell
# startapp:
# python3 manage.py startapp

# why need this and is not a file?
.PHONY: set_env_vars
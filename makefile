run:
	@python manage.py runserver
migrate:
	@python manage.py migrate
migrations:
	@python manage.py makemigrations
shell:
	@python manage.py shell
	
push:
	@git push origin main

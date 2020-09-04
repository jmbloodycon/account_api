#!/usr/bin/bash

python manage.py migrate

if [ ! -f ./second_run ]; then
	python manage.py loaddata initial_data
	touch ./second_run
fi

./autho_hold.sh &
python manage.py runserver serv:8000
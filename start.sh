#!/usr/bin/bash

python manage.py migrate

./autho_hold.sh &
python manage.py runserver serv:8000
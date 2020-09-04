# Django Project Template

Works with PostgreSQL.

##Implement 4 api methods:

* / api / ping (service health)
* / api / add (balance top-up)
* / api / substract (decrease balance)
* / api / status (balance balance, account opened or closed)

For "add" and "substract" methods, the Request must contain data in the form 
```shell
{
    "id": id account (str),
    "money": the amount of money to complete the operation
}
```

## Run project

```shell
$ docker-compose up
```


## Install requirements

```shell
$ pip install -r requirements/development.txt
```

## Run a database

```shell
$ docker-compose up -d postgres
```

## Set up local settings

```shell
$ vi config/settings/local.py
```

Put your local settings in the `local.py`, you can override settings
consider your local environment. Start with lines below:

```python
from .base import *
```


## Apply migrations

```shell
$ ./manage.py migrate
```

### Create Superuser

The project will use E-Mail address as username.

```shell
$ ./manage.py createsuperuser
```

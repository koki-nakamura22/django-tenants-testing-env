# django-tenants-testing-env

## Environment information

Ubuntu 22.04 (WSL2)

## Init

1. Create a Dockerfile with the below codes.

```
FROM python:3.11
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8100
```

2. Create a docker-compose.yml with the below codes.

```yml
version: "3"
services:
  web:
    container_name: python-test-tenants-app-with-docker
    build:
      context: .
      network: host
    command: python3 test_app/manage.py runserver 0.0.0.0:8100
    working_dir: /code
    ports:
      - 8100:8100
    volumes:
      - .:/code
    depends_on:
      - db
  db:
    container_name: python-test-tenants-app-with-docker-db
    image: postgres:15.1
    restart: always
    environment:
      POSTGRES_USER: db-user
      POSTGRES_PASSWORD: db-pass
      PGPASSWORD: password123
      POSTGRES_DB: sample
      TZ: "Asia/Tokyo"
    ports:
      - 5432:5432
    volumes:
      - postgres:/var/lib/postgresql/data
  pgadmin:
    image: dpage/pgadmin4
    restart: always
    ports:
      - 81:80
    environment:
      PGADMIN_DEFAULT_EMAIL: info@mebee.info
      PGADMIN_DEFAULT_PASSWORD: password
    volumes:
      - pgadmin:/var/lib/pgadmin
    depends_on:
      - db
volumes:
  postgres:
  pgadmin:

```

3. Create a requirements.txt then write the following lines.

```
Django==4.1.5
django-tenants==3.4.7
mysqlclient==2.1.1
```

4. Execute the following commands on terminal.

```sh
docker-compose build
docker-compose run web mkdir test_app
docker-compose run web django-admin startproject conf test_app/
docker-compose run -w /code/test_app web python manage.py startapp tenant_only
docker-compose run -w /code/test_app web python manage.py startapp tenant_common
sudo chown -R $USER:$USER .
docker-compose up
```

5. Setting djang_tenants

Read
[django_tenants Docs#Installation](https://django-tenants.readthedocs.io/en/latest/install.html)

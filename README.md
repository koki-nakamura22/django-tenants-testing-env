# django-tenants-testing-env

## Environment information

Ubuntu 22.04 (WSL2)

## Init

1. Create a requirements.txt then write the following lines.

```
Django==4.1.5
django-tenants==3.4.7
mysqlclient==2.1.1
```

2. Execute the following commands on terminal.

```sh
docker-compose build
docker-compose run web django-admin startproject test_app .
sudo chown -R $USER:$USER .
docker-compose up
```

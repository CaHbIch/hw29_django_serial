## Запуск проекта
Установить зависимости: 

1) pip install poetry
2) poetry install
3) Запустить базу данных postgres docker-compose up -d


------------------

### Миграции

- Создать миграции:

python manage.py makemigrations

- Накатить миграцию:

 python manage.py migrate

------------------

### Загрузка данных в БД :

- python manage.py loaddata location.json
- python manage.py loaddata user.json
- python manage.py loaddata category.json
- python manage.py loaddata ad.json

------------------

### Для доступа к админке

Создать администратора набрать команду:

- python manage.py createsuperuser

- Имя: skypro
- пароль: 1234

Запустить серевер:

### python manage.py runserver
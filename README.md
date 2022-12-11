﻿# Python_diploma

### Lesson 37

* Python 3.10
* Django 4.0.1
* PostgreSQL 14.6-alpine
##
#### Файл `"docker-compose.yaml"` содержит контейнер с базой данных Postgres, который разворачивается при вызове в терминале команды `docker-compose up -d`.
#### Файл `"docker-compose-ci.yaml"` для разворачивания приложения на сервере.

#### Также содержится файлы *`".env"`* и *`".env_ci"`* для хранения переменных среды. Файл *`".env_ci"`* содержит в себе переменные окружения, но замененные на плейсхолдеры.
##
#### Активация виртуального окружения:
```.\venv\Scripts\Activate```

##### Описана абстрактная модель пользователя, в Админке изменены названия и заголовки в самой Админке.
##### Создан файл _requirements.txt_ для установки зависимостей в приложении через команду:
```pip freeze > requirements.txt```
#### Установка зависимостей из _requirements.txt_:
```pip install -r requirements.txt```

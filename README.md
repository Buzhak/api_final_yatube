# YATUBE API

## Как запустить проект.
> Эта инструкция актуальная для Linux OS

Клонируем репозиторий и перейти в него в командной строке.

```
git clone git@github.com:Buzhak/api_final_yatube.git
```

```
cd api_final_yatube
```

Создаём и активируем виртуальное окружение

```
python3 -m venv env
```

```
source env/bin/activate
```

Обновляем pip и устанавливаем зависимости из файла

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнем миграции:

```
python3 manage.py migrate
```

Запускаем проект:

```
python3 manage.py runserver
```

## Примеры запросов.

Когда вы запустите проект, по [адресу](http://127.0.0.1:8000/redoc/) будет доступна документация для API Yatube,
в которой можно будет посмотреть примеры запросов и адреса для работы с проектом.

## Примеры регистрация нового пользователя и получение токена.

Что бы создать нового пользователя Вам нужно сделать POST запрос формата

```
{
    "username":"user_name",
    "password":"user_password"
}
```

на адрес: [http://127.0.0.1:8000/api/v1/users/](http://127.0.0.1:8000/api/v1/users/).

Вы получите ответ:

```
{
    "email": "",
    "username": "user_name",
    "id": 1
}
```
Все прошло удачно, теперь вам нужно получить токен.
Делаем POST запрос с теми же данными,
что мы использовали для регистрации на адрес: [http://127.0.0.1:8000/api/v1/jwt/create/](http://127.0.0.1:8000/api/v1/jwt/create/)

в ответ Вы получите что-то подобное:

```
# пример ответа

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2Njg5NTAzMywianRpIjoiNDg1YmY4MWU2Y2EzNGU0Yzg5YmVlMDcxMzYwY2Y5NDIiLCJ1c2VyX2lkIjo0fQ.pkNfgWs4AKoZNllWTfvx9_h33PNsVSMkVWiGvYe3MVk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MjQwNjMzLCJqdGkiOiI2MjkzNDJmMDAyZmE0N2I1ODVmMTA3MGI2MWUwYjkwNiIsInVzZXJfaWQiOjR9.uTOIERYUjeRRBIARUKcj32pYpN-lwE7SIiiJ-bRzvP0"
}
```
Токен вернётся в поле "access", а данные из поля "refresh" пригодятся для обновления токена.

Если ваш токен утрачен, украден или каким-то иным образом скомпрометирован, вам понадобится отключить его и получить новый. Для этого отправьте POST-запрос на тот же адрес [http://127.0.0.1:8000/api/v1/jwt/create/](http://127.0.0.1:8000/api/v1/jwt/create/), а в теле запроса в поле refresh передайте refresh-токен.

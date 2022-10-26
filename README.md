# YATUBE API

## Как запустить проект.
### (Эта инструкция актуальная для Linux OS)

Клонировать репозиторий и перейти в него в командной строке.

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
# Описание проекта
  Проект YaCut - сервис укорачивания ссылок. Результат его работы - сопоставление длинной пользовательской ссылки с короткой, которую рандомно выдаст сервис или самостоятельно введет пользователь

# Запуск проекта
  1) Клонировать репозиторий:
    ```
    git clone https://github.com/mkmmcvrs68/yacut
    ```
  2) Cоздать виртуальное окружение:

    ```
    python3 -m venv venv
    или 
    python -m venv venv(Windows)
    ```
  3) Активировать виртуальное окружение:
    ```
    source venv/bin/activate
    или
    source venv/scripts/activate (Windows)
    ```

  4) Установить зависимости из файла requirements.txt:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
  5) Создать и заполнить файл .env:
    ```
    touch .env
    ```
    Необходимые атрибуты в файле:
      FLASK_APP=yacut_example
      FLASK_ENV=development
      DATABASE_URI=sqlite:///example_dir/db.sqlite3
      SECRET_KEY=_YOUR_Example_SECRET_KEY

# Стек 
  * Python 3.9.10
  * Flask 2.0.2
  * Flask-SQLAlchemy 2.5.1
  * WTForms 3.0.1
  * Jinja 3.0.3
  * SQLAlchemy 1.4.29

# Автор
  https://github.com/Vladislav199912
  vladermakov@mail.ru
  Ермаков Владислав

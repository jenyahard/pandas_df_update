Установка
Клонирование репозитория:

shell
Copy code
$ git clone https://github.com/ваш-username/название-репозитория.git
Перейдите в директорию проекта:

shell
Copy code
$ cd название-репозитория
Создание и активация виртуального окружения:

Windows:

shell
Copy code
$ python -m venv venv
$ venv\Scripts\activate
macOS и Linux:

shell
Copy code
$ python3 -m venv venv
$ source venv/bin/activate
Установка зависимостей:

shell
Copy code
$ pip install -r requirements.txt
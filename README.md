cd test_forms

Для запуска

1 Создайте виртуальное окружение и активируйте его

python -m venv venv

В Windows:

venv\Scripts\activate

В Unix или MacOS:

source venv/bin/activate

2 Установите зависимости

pip install -r requirements.txt


3 Примените миграции

python manage.py migrate

4 Создайте админа

python manage.py createsuperuser

5 Создайте файл .env

touch .env

И добавьте туда секретный ключ например
SECRET_KEY="django-insecure-yymv3d4nhjws9k5ak0^di^5@1j-@351qcac_jmsmup)h^ly)4z"


6 Запустите сервер 

python manage.py runserver


Создание опроса и добавление дерева вопросов

1 Создайте опрос в таблице Poll.

2 Добавьте первый вопрос в таблицу Question с пустыми полями depends_on и depends_on_answer.

3 Создайте возможные ответы на этот вопрос в таблице Answer.

4 Для вопросов с типом ответа Text (когда пользователь вводит свой ответ) оставьте поле depends_on_answer пустым и с помощью depends_on укажите после какого вопроса он будет идти.

5 Для последующих вопросов укажите значения depends_on (зависит от вопроса Х) и depends_on_answer (появляется при ответе Х).


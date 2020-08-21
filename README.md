### Задание

- при открытии должно показать кнопку «авторизоваться»
- по нажатию делает oauth авторизацию Вконтакте
- показывает имя авторизованного пользователя и 5 любых друзей пользователя.

При последующих запусках/заходах на страницу сразу показывает всю информацию т.к. уже понимает, что авторизовано и авторизация запоминается.
Бекенд, если потребуется, на любой технологии на ваш выбор.

Результат предоставить в качестве url (или приложения, которое можно установить на мобильное устройство) где можно протестировать работу и в виде исходных кодов в tar.gz архиве.


### Установка Docker

https://docs.docker.com/engine/install/

### Предварительная настройка

1. Необходимо инициализировать переменные окружения.
В папек `env/` необходимо скопировать шаблоны, удалив при этом расширение `.template`.

2. Примеры переменных:
    
    `back.env`
    
    - DJANGO_SECRET_KEY=!6@%ch8p6o#7u!zx&=@s3kejg483y+8%c#fped_d*fb-v&#*45
    - VK_CLIENT_ID=
    - VK_SECRET_KEY=
    - VK_REDIRECT_URI=http://***/vk-auth

3. В файле `backend/backend/settings.py` в списках `ALLOWED_HOSTS` указать необходимый хост.

4. В файлах в папке `proxy/` указать `server_name`.

#### Создание миграции

    docker-compose run backend python manage.py makemigrations
    docker-compose run backend python manage.py migrate


### Запуск контейнеров

#### dev

    docker-compose up --build


#### prod

    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build

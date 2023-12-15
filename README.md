# **Название Проекта: LMS (Learning Management System)**

## Описание

LMS - это система управления обучением, разработанная на Django. Она включает в себя управление курсами, уроками и пользователями, а также интеграцию с системой оплаты Stripe и Celery для асинхронной обработки задач.

### Технологический стек

Django
PostgreSQL
Redis
Celery
Docker
Stripe API
Установка и настройка

### Требования

Перед началом убедитесь, что у вас установлены:

Python 3.9+
Docker и Docker Compose

### Локальная установка

Клонирование репозитория:

git clone https://your-repository-url.git
cd lms_project

Настройка виртуальной среды:

python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate     # Для Windows

Установка зависимостей:

pip install -r requirements.txt

### Настройка переменных окружения

Создайте файл .env в корне проекта и укажите необходимые переменные:

DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=lms_db
DB_USER=lms_user
DB_PASS=lms_password
REDIS_URL=redis://redis:6379/0
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key

### Запуск с помощью Docker

Сборка и запуск контейнеров:

docker-compose up --build
Эта команда запустит Django-приложение, PostgreSQL, Redis и Celery.


Создание и применение миграций:
Откройте новое окно терминала и выполните:

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

Создание суперпользователя (опционально):
docker-compose exec web python manage.py createsuperuser

Просмотр приложения:
Приложение будет доступно по адресу http://localhost:8000.


### **`Остановка приложения`**

Чтобы остановить и удалить контейнеры, сети, тома и образы, созданные up, используйте команду:
docker-compose down


Документация API

После запуска приложения документация API доступна по адресу: http://localhost:8000/swagger/ и http://localhost:8000/redoc/.

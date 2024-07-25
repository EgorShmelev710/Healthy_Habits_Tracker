# Course_work_7

## Описание

Это трекер привычек.
Создав свом привычки, вы будете получать уведомления о них в телеграм боте!

## Технологии

- Python
- Django
- DRF
- PostgreSQL
- Redis
- Celery

## Настройка проекта

### Клонирование проекта

Для работы с проектом клонируйте репозиторий

  ```sh
  git clone git@github.com:EgorShmelev710/Course_work_7.git
  ```

### Настройка виртуального окружения

Создайте виртуальное окружение командой:

```text
python3 -m venv venv
```

Активируйте виртуальное окружение:

```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавите зависимости командой:

```text
pip install -r requirements.txt
```

### Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    
    BOT_TOKEN=key - токен для подключения бота в Телеграм
  
  
    # URL-адрес брокера сообщений
  CELERY_BROKER_URL = 'redis://localhost:6379' # Например, Redis
  
  # URL-адрес брокера результатов, также Redis  
  CELERY_RESULT_BACKEND = 'redis://localhost:6379' 
  
  # Часовой пояс для работы Celery
  CELERY_TIMEZONE = ваш часовой пояс
  
  # Флаг отслеживания выполнения задач
  CELERY_TASK_TRACK_STARTED = True 
  
  # Максимальное время на выполнение задачи
  CELERY_TASK_TIME_LIMIT = 30 * 60

    
    ENGINE=django.db.backends.postgresql
    NAME=db_name - название базы данных 
    USER=user - имя пользователя базы данных
    PASSWORD=password - пароль пользователя базы данных 
    HOST=host - можно указать localhost
    PORT=port - порт для подключения к базе данных
  
    SECRET_KEY=key - секретный ключ Django
    ```

### Настройка БД и кэширования:

- Создайте миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```
  


- Установите Redis:

    - Linux команда:
   ```text
   sudo apt install redis; 
  или 
  sudo yum install redis;
   ```

    - macOS команда:
   ```text
   brew install redis;
   ```

  Windows инструкция:
    - [Перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)

## Использование

- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  В программе Postman, в админке или на фронтенд сервере 
зарегистрируйтесь и создайте привычки


- В другом терминале запустите celery worker командой:
  ```text
  celery -A config worker -l INFO  # для Mac и Linux
  celery -A config worker -l INFO -P eventlet  # для Windows
  ```
- В третьем терминале запустите celery beat командой:
  ```text
  celery -A config beat -l info -S django
  ```
  

- Зайдите в телеграм бот и нажмите START

## Контакты

Ссылка на репозиторий: [https://github.com/EgorShmelev710](https://github.com/EgorShmelev710)



# Базовый образ
FROM python:3.9

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Создаем директорию для кода
RUN mkdir /code
WORKDIR /code

# Устанавливаем зависимости проекта
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копируем код проекта
COPY . /code/

#RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


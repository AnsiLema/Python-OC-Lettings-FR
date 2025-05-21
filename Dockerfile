FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE 8000

ARG PORT=8000
ENV PORT=${PORT}
CMD ["sh", "-c", "gunicorn app.wsgi:application --bind 0.0.0.0:$PORT"]
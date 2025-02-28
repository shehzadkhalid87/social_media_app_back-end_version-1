FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN mkdir -p /app/media/post_images
RUN chown -R www-data:www-data /app/media
USER www-data
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary
RUN pip install Pillow
RUN pip install watchgod
COPY . /app/

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
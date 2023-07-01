FROM python:3.11.4-slim-bullseye

WORKDIR /usr/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# RUN python manage.py collectstatic
   
EXPOSE 8000

CMD gunicorn davaj.wsgi --bind 0.0.0.0:8000 --workers 3
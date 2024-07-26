#FROM python:3.11.9-slim-bullseye
FROM python:3.11.9-bullseye

#RUN python -m pip install Django aws-opentelemetry-distro gunicorn
RUN python -m pip install Django gunicorn opentelemetry-instrumentation-django
RUN python -m pip install aws-opentelemetry-distro
RUN apt-get install pkg-config && python -m pip install mysqlclient

WORKDIR /app

COPY . .

#CMD ["opentelemetry-instrument", "python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
CMD ["gunicorn", "-c", "gunicorn_config.py", "backend.wsgi:application"]
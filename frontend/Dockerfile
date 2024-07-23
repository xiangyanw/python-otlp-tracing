FROM python:3.11.9-slim-bullseye

#RUN python -m pip install Django aws-opentelemetry-distro gunicorn
RUN python -m pip install Django gunicorn opentelemetry-instrumentation-django
RUN python -m pip install aws-opentelemetry-distro

WORKDIR /app

COPY . .

#CMD ["opentelemetry-instrument", "python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
CMD ["gunicorn", "-c", "gunicorn_config.py", "mysite.wsgi:application"]
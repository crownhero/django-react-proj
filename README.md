# Dockerised Django-React

A modern production-ready boilerplate for Django & React (full-stack) projects. Setup with Docker

 ## Services
 - django: Backend. Served with Gunicorn
 - react: Frontend
 - nginx: Serves production build of the frontend and acts as reverse proxy for the backend.
 - redis: Message broker for Celery
 - celery: Asynchronous task queue
 - db: Postgres database


## Usage

 - `docker compose build` : Build the services.
 - `docker compose up` : Start all the services in their respective containers.
 - `docker compose down`: Stop all services.
 - `docker compose run --rm <service> <command>` : Run one-off commands on any service. For instance: If you want to run migrations in the django service, you can execute `docker compose run --rm django python3 manage.py migrate`

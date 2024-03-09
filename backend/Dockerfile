FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app
#COPY . .
#COPY ./core/ ./core/
#COPY ./backend/ ./backend/
#COPY manage.py manage.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate
COPY ./staticfiles/ ./staticfiles/

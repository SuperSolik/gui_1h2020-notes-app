FROM python:3.8

WORKDIR app

RUN apt-get update && apt-get install -y python3-pyqt5 sqlite3
RUN pip install --upgrade pip setuptools PyQt5

RUN mkdir db
COPY src ./src
COPY *.py ./
COPY *.sql ./

ENV DEV_NOTE_DB /app/db/database.db
RUN sqlite3 /app/db/database.db < create_db.sql
ENTRYPOINT ["python", "main.py"]

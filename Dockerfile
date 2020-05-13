FROM ubuntu:18.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3.8 python3-pip python3-pyqt5 sqlite3
RUN python3.8 -m pip install --upgrade pip setuptools
RUN python3.8 -m pip install PyQt5

COPY src/ ./
COPY main.py ./
COPY create_db.sql ./

ENV DEV_NOTE_DB=/app/database.db
RUN sqlite3 database.db < create_db.sql
ENTRYPOINT python3.8 main.py

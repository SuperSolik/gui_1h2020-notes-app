FROM ubuntu:18.04

RUN apt-get update \
 && apt-get install -y \
    python3.8 \
    python3-pip \
    python3-pyqt5 \
    sqlite3 \
 && python3.8 -m pip install --upgrade pip setuptools \
 && python3.8 -m pip install PyQt5

WORKDIR /app
ENTRYPOINT cat create_db.sql | sqlite3 database.db \
        && export DEV_NOTE_DB=/app/database.db \
        && python3.8 main.py

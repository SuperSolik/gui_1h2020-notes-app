FROM python:3.8

WORKDIR app

RUN apt-get update && apt-get install -y python3-pyqt5 python3-pyqt5.qtwebengine sqlite3

COPY requirements.txt ./

RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

RUN mkdir db
COPY src ./src
COPY *.py ./
COPY *.sql ./

#to make PyQtWebEngine work
ENV QTWEBENGINE_CHROMIUM_FLAGS --no-sandbox

ENV DEV_NOTE_DB /app/db/database.db
RUN sqlite3 /app/db/database.db < create_db.sql
ENTRYPOINT ["python", "main.py"]

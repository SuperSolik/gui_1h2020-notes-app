if [ ! -d "./env" ] 
then
    python3.8 -m venv env
    . ./env/bin/activate
    echo "Installing dependencies"
    pip install -U pip setuptools
    pip install -r requirements.txt
    deactivate
fi
if [ ! -f "./db/local_notes.db" ]
then
    echo "Creating db"
    sqlite3 ./db/local_notes.db < create_db.sql
fi
export DEV_NOTE_DB="./db/local_notes.db"
. ./env/bin/activate
echo "Starting app"
python main.py

NAME="2020_leti_7303_gui_petrov_juskovets_notes_app"

docker build -t $NAME .
xhost + "local:docker@"
docker run --rm \
       -v db:/app/db \
       -v /tmp/.X11-unix:/tmp/.X11-unix \
       -e DISPLAY=unix$DISPLAY \
       $NAME

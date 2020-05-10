NAME="2020_leti_7303_gui_petrov_juskovets_notes_app"

docker build -t $NAME .
xhost + "local:docker@"
docker run --rm \
       -v /tmp/.X11-unix:/tmp/.X11-unix \
       -e DISPLAY=$DISPLAY \
       --device=/dev/snd/controlC0 \
       --device=/dev/snd/pcmC0D0p \
       --device=/dev/snd/seq \
       --device=/dev/snd/timer \
       -it -v "$(pwd)":/app $NAME

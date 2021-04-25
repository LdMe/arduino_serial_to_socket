#! /bin/bash

sudo chown $USER /dev/ttyACM0
source socket_client/bin/activate
pip3 install -r requirements.txt
python3 client.py 
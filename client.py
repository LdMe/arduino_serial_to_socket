import socket
import serial
import time

HOST = '51.75.120.79'
#HOST = '141.94.23.109'  # The server's hostname or IP address
#HOST = '127.0.0.1'
PORT = 9999        # The port used by the server

def sendInfo():
	arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.connect((HOST, PORT))
	    while True:
		    msg = arduino.readline()
		    print(msg)
		    if(msg):
		    	s.sendall(msg)
		    #data = s.recv(1024)
		    time.sleep(0.1)
while True:
	try:
		sendInfo()
	except Exception as e:
		print("reconnecting")
		continue
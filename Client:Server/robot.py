from winsound import Beep
import pyfirmata
import time
import keyboard
import socket



board = pyfirmata.Arduino('com4')


value = 0.5

left_forw = board.get_pin('d:3:p')
left_back = board.get_pin('d:5:p')
right_forw = board.get_pin('d:6:p')
right_back = board.get_pin('d:11:p')


def stop():
	left_forw.write(0)
	left_back.write(0)
	right_forw.write(0)
	right_back.write(0)

def right():
	left_forw.write(value)
	left_back.write(0)
	right_forw.write(0)
	right_back.write(value)


def left():
	left_forw.write(0)
	left_back.write(value)
	right_forw.write(value)
	right_back.write(0)

def back():
	left_forw.write(0)
	left_back.write(value)
	right_forw.write(0)
	right_back.write(value)

def forward():
	left_forw.write(value)
	left_back.write(0)
	right_forw.write(value)
	right_back.write(0)




client = socket. socket(

  socket. AF_INET,
  socket. SOCK_STREAM,
  
)
  
client. connect(
  ("192.168.1.67", 1234)
)  
while True:
    data = client.recv(2048) # receive
    print(data.decode("utf-8"))
    print(data)
   # command = data.deccode("utf-8")
    if(data == b'forward'):
        forward()
    if(data == b'back'):
        back()  
    if(data == b'right'):
        right()               
    if(data == b'left'):
        left()  
    if(data == b'stop'):
        stop()
    if(data == b'beep'):
        Beep()  
    if(data == b'toggle drill'):
        toggledrill()
    if(data == b'read color data'):
        readcolordata()
                            

import socket
import time
from winsound import Beep
import keyboard

server = socket. socket(

   socket. AF_INET,
   socket. SOCK_STREAM,
   
   )
   
server. bind(
 ("192.168.1.67", 1234) # localhost
 )
 
server. listen(5)

while True:
    user_socket, address = server. accept()
    print(f"Connecting to {address}")
    break

time.sleep(1)

#user_socket.send(bytes("Это точно", "utf-8"))
def stop():
	user_socket.send("stop".encode("utf-8"))

def right():
	user_socket.send("right".encode("utf-8"))

def left():
	user_socket.send("left".encode("utf-8"))

def back():
	user_socket.send("backward".encode("utf-8"))

def forward():
	user_socket.send("forward".encode("utf-8"))

def beep():
	user_socket.send("beep".encode("utf-8"))

def toggledrill():
	user_socket.send("toggle drill".encode("utf-8"))

def readcolordata():
	user_socket.send("read color data".encode("utf-8"))

keyboard.add_hotkey('0', stop)
keyboard.add_hotkey('d', right)
keyboard.add_hotkey('a', left)
keyboard.add_hotkey('w', forward)
keyboard.add_hotkey('s', back)
keyboard.add_hotkey('b', beep)
keyboard.add_hotkey('r', toggledrill)
keyboard.add_hotkey('f', readcolordata)
keyboard.add_hotkey('q', quit)




keyboard.wait('Ctrl + Q')


 

import socket
from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

HOST = "10.42.0.1"  # Address to bind/listen to
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    break

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/forward")
def forward():
    conn.sendall(b"forw")
    return


@app.get("/backward")
def backward():
    conn.sendall(b"back")
    return


@app.get("/left")
def left():
    conn.sendall(b"left")
    return


@app.get("/right")
def right():
    conn.sendall(b"righ")
    return


@app.get("/beep")
def beep():
    conn.sendall(b"beep")
    return


@app.get("/drill")
def drill():
    conn.sendall(b"dril")
    return


@app.get("/color")
def color():
    conn.sendall(b"colo")
    return


@app.get("/grab")
def grab():
    conn.sendall(b"grab")
    return


@app.get("/release")
def release():
    conn.sendall(b"rele")
    return


@app.get("/quit")
def quit():
    conn.sendall(b"quit")
    return

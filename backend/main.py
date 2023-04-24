import socket
from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

HOST = "10.42.0.1"  # Address to bind/listen to
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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


@app.get("/drive")
def drive():
    conn.sendall(b"drive")
    return

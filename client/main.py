#!/usr/bin/env pybricks-micropython
import socket

from pybricks.ev3devices import (ColorSensor, GyroSensor, InfraredSensor,
                                 Motor, TouchSensor, UltrasonicSensor)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.

# Initialize the EV3 Brick and Motors
ev3 = EV3Brick()
left_motor = Motor(port=Port.A)
right_motor = Motor(port=Port.C)

left_motor.control.limits(acceleration=1000)
left_motor.control.limits(acceleration=1000)

# Create a DriveBase object
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=192.5)

# Set the speed and turn rate of the robot
speedmod = 50
turn_ratemod = 20

# Write your program here.

# Init socket
HOST = "10.42.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

addr = socket.getaddrinfo(HOST, PORT)[0][-1]
sock = socket.socket()
sock.connect(addr)

ev3.speaker.beep()

while True:
    data = sock.recv(1024)
    print(str(data, 'utf8)'), end='')
    datastr = str(data, 'utf8')
    if datastr == 'drive':
        robot.straight(50)

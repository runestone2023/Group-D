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

# Initialize the EV3 Brick, Motors and Sensors
ev3 = EV3Brick()
left_motor = Motor(port=Port.A)
right_motor = Motor(port=Port.D)
drill_motor = Motor(port=Port.C)
color_sensor = ColorSensor(port=Port.S3)
gripping_motor = Motor(port=Port.B, positive_direction=Direction.COUNTERCLOCKWISE)

left_motor.control.limits(acceleration=1000)
left_motor.control.limits(acceleration=1000)

# Create a DriveBase object
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=192.5)

# Set the speed and turn rate of the robot
speedmod = 100
turn_ratemod = 30
drillspeed = 99999
grabspeed = 400

# Write your program here.

# Init socket
HOST = "10.42.0.1"  # Address of server running backend API
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

addr = socket.getaddrinfo(HOST, PORT)[0][-1]
sock = socket.socket()
sock.connect(addr)

# ev3.speaker.beep()

# Initialize the gripper.
gripping_motor.run_until_stalled(grabspeed, Stop.COAST, 30)
# gripping_motor.reset_angle(0)
gripping_motor.run_time(-grabspeed, 3000)

while True:
    data = sock.recv(1024)
    datastr = str(data, 'utf8')
    print(datastr)
    if datastr == 'forward':
        robot.straight(50)
    elif datastr == 'backward':
        robot.straight(-50)
    elif datastr == 'left':
        robot.turn(45)
    elif datastr == 'right':
        robot.turn(-45)
    elif datastr == 'beep':
        ev3.speaker.beep()
    elif datastr == 'drill':
        drill_motor.run(drillspeed if drill_motor.speed() == 0 else 0)
    elif datastr == 'color':
        color = color_sensor.color()
        print(color)
        ev3.speaker.say(str(color))
    elif datastr == 'grab':
        gripping_motor.run_until_stalled(grabspeed, Stop.COAST, 30)
    elif datastr == 'release':
        gripping_motor.run_time(-grabspeed, 3000)
    elif datastr == 'quit':
        break
    else:
        print("Invalid command: " + datastr)

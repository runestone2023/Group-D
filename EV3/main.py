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
# color_sensor = ColorSensor(port=Port.S3)
gripping_motor = Motor(port=Port.B, positive_direction=Direction.COUNTERCLOCKWISE)

left_motor.control.limits(acceleration=1000)
left_motor.control.limits(acceleration=1000)

# Create a DriveBase object
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=192.5)

# Set the speed and turn rate of the robot
drivelength = 75
turn_angle = 45
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
# gripping_motor.run_until_stalled(grabspeed, Stop.COAST, 30)
# gripping_motor.reset_angle(0)
# gripping_motor.run_time(-grabspeed, 3000)

while True:
    data = sock.recv(1024)
    if len(data) == 0:
        break
    datastr = str(data, 'utf8')
    print(datastr)
    while len(datastr) != 0:
        command = datastr[:4]
        if datastr == 'forw':
            robot.straight(drivelength)
        elif datastr == 'back':
            robot.straight(-drivelength)
        elif datastr == 'left':
            robot.turn(turn_angle)
        elif datastr == 'righ':
            robot.turn(-turn_angle)
        elif datastr == 'beep':
            ev3.speaker.beep()
        elif datastr == 'dril':
            drill_motor.run(drillspeed if drill_motor.speed() == 0 else 0)
        # elif datastr == 'colo':
        #     color = str(color_sensor.color())
        #     if color != "None":
        #         color = color[6:]
        #     print(color)
        #     ev3.speaker.say(color)
        elif datastr == 'grab':
            gripping_motor.run_until_stalled(grabspeed, Stop.COAST, 30)
        elif datastr == 'rele':
            gripping_motor.run_time(-grabspeed, 3000)
        elif datastr == 'quit':
            break
        else:
            print("Invalid command: " + datastr)
        datastr = datastr[4:]

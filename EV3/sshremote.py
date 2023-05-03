#!/usr/bin/env pybricks-micropython
# This is a standalone script that can be run on the EV3 Brick via SSH.
from pybricks.ev3devices import ColorSensor, Motor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick, Motors and Sensors
ev3 = EV3Brick()
left_motor = Motor(port=Port.A)
right_motor = Motor(port=Port.D)
drill_motor = Motor(port=Port.C)
color_sensor = ColorSensor(port=Port.S3)

left_motor.control.limits(acceleration=1000)
left_motor.control.limits(acceleration=1000)

# Create a DriveBase object
robot = DriveBase(left_motor, right_motor, wheel_diameter=35, axle_track=192.5)

# Set the speed and turn rate of the robot
speedmod = 100
turn_ratemod = 30
drillspeed = 99999

# Control the robot with user input from the terminal
print("Use the following keys to control the robot:")
print("w: move forward")
print("s: move backward")
print("a: turn left")
print("d: turn right")
print("b: beep")
print("r: toggle drill")
print("f: read color data")
print("q: quit")

ev3.speaker.beep()

while True:
    # Read user input from the terminal
    command = input("> ")

    (distance, speed, angle, turn_rate) = robot.state()

    # Interpret the user input and control the robot
    if command == "w":
        robot.drive(speed+speedmod, 0)
    elif command == "s":
        robot.drive(speed-speedmod, 0)
    elif command == "a":
        robot.drive(speed, turn_rate+turn_ratemod)
    elif command == "d":
        robot.drive(speed, turn_rate-turn_ratemod)
    elif command == "e":
        robot.stop()
    elif command == "b":
        ev3.speaker.beep()
    elif command == "r":
        drill_motor.run(drillspeed if drill_motor.speed() == 0 else 0)
    elif command == "f":
        color = color_sensor.color()
        print(color)
        ev3.speaker.say(str(color))
    elif command == "q":
        break
    else:
        print("Invalid command. Use w, s, a, d, or q.")
        continue

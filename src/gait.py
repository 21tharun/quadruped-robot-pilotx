from time import sleep
from robot_actions import move_servo
from poses import base_position

def walk_cycle():
    move_servo(2,115)
    move_servo(0,165)
    sleep(0.2)

    move_servo(6,90)
    move_servo(4,90)
    sleep(0.4)

    move_servo(1,75)
    move_servo(3,25)
    sleep(0.4)

    move_servo(1,50)
    move_servo(3,50)

def walk(steps=5):
    base_position()
    for _ in range(steps):
        walk_cycle()
    base_position()

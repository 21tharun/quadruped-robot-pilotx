from time import sleep
from robot_actions import move_servo

def base_position():
    angles = [140, 50, 140, 50, 90, 90, 90, 90]
    for i, a in enumerate(angles):
        move_servo(i, a)
    sleep(1)

def sitting():
    move_servo(0, 0)
    move_servo(1, 180)
    move_servo(2, 0)
    move_servo(3, 180)
    sleep(1)

def sit_to_stand():
    base_position()

def attack():
    move_servo(4,110)
    move_servo(5,110)
    move_servo(6,70)
    move_servo(7,70)
    move_servo(0,160)
    move_servo(3,20)
    sleep(2)
    base_position()

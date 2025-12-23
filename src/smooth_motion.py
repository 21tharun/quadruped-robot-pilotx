from time import sleep
from robot_actions import move_servo

def smooth_move_servo(servo_id, start, target, step=5, delay=0.02):
    if start < target:
        for angle in range(start, target+1, step):
            move_servo(servo_id, angle)
            sleep(delay)
    else:
        for angle in range(start, target-1, -step):
            move_servo(servo_id, angle)
            sleep(delay)

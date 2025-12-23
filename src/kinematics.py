import math

THIGH = 4.0
SHIN = 4.31

def inverse_kinematics(x, y):
    d = math.sqrt(x**2 + y**2)
    if d > THIGH + SHIN:
        raise ValueError("Out of reach")

    knee = math.acos((THIGH**2 + SHIN**2 - d**2) / (2*THIGH*SHIN))
    hip = math.atan2(y, x) - math.acos((THIGH**2 + d**2 - SHIN**2) / (2*THIGH*d))
    return math.degrees(hip), math.degrees(knee)


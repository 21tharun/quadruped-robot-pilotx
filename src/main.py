from poses import base_position, sitting
from gait import walk

def main():
    base_position()
    walk(steps=10)
    sitting()

if __name__ == "__main__":
    main()

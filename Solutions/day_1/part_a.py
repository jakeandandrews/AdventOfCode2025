import re
from numpy import genfromtxt
from pathlib import Path

# Prerequisites
 
dial = range(100)
START = 50
DIAL_SIZE = len(dial)
FEELS_THE_CLICK = 0


# Christmas combination cracking code

def gauge_the_twist(twist_notation): #->vector
    notation_unpacked = re.split(r"(\d+)", twist_notation)
    twist_direction = 1 if notation_unpacked[0] ==  "R" else  -1
    twist_strength = int(notation_unpacked[1])
    twist = twist_strength * twist_direction
    return twist

def twist_the_dial(dial_position, twist): #->end_position
    return (dial_position + twist) % DIAL_SIZE

def crack_the_combination(twist_list):
    clicks_felt = 0
    dial_position = START
    for twist_notation in twist_list:
        twist = gauge_the_twist(twist_notation)
        dial_position = twist_the_dial(dial_position, twist)
        if dial_position == FEELS_THE_CLICK:
            clicks_felt += 1
    return clicks_felt

if __name__ == "__main__":
    data_path = Path(__file__).parent / "data" / "day_1.txt"
    data = genfromtxt(data_path, 'str')
    print("THE SOLUTION IS...", crack_the_combination(data))
    

import math, re
from pathlib import Path
from typing import Sequence

from numpy import genfromtxt

class ChristmasCracker:
    _dial_direction_lookup = {"R": 1, "L": -1}
    _letter_digit_split_regex = re.compile(r"(\d+)")

    def __init__(self, start, dial, clicks=0): 
        self._dial = dial
        self._dial_position = start
        self._clicks = clicks
        self._dial_min = min(dial)
        self._dial_max = max(dial)

    @property
    def dial(self) ->Sequence[int]:
        return self._dial

    @property
    def dial_size(self) ->int:
        return len(self._dial)

    @property
    def dial_position(self) -> int:
        return self._dial_position

    @dial_position.setter
    def dial_position(self, value: int) -> None:
        if not (self._dial_min <= value <= self._dial_max):
            raise ValueError(f"Dial position invalid")
        self._dial_position = value

    @property
    def clicks(self) -> int:
        return self._clicks
    
    @clicks.setter
    def clicks(self, value: int) -> None:
        self._clicks = value

    def reset_clicks(self) -> None:
        self.clicks = 0

    def _gauge_the_twist(self, twist_notation: str) -> int:
        notation_unpacked = self._letter_digit_split_regex.split(twist_notation)
        twist_direction = self._dial_direction_lookup[notation_unpacked[0]]
        twist_strength = int(notation_unpacked[1])
        return twist_strength * twist_direction

    def _twist_the_dial(self, twist: int) -> None:
        self.dial_position = (self.dial_position + twist) % self.dial_size

class LandsOnClicks(ChristmasCracker):
    FEELS_THE_CLICK = 0

    def run(self, twist_list: list[str]) -> int:
        self.reset_clicks()
        for twist_notation in twist_list:
            twist = self._gauge_the_twist(twist_notation)
            self._twist_the_dial(twist)
            if self.dial_position == self.FEELS_THE_CLICK:
                self.clicks += 1
        return self.clicks    

class PassesThroughClicks(ChristmasCracker):
    def _twisted_through_click(self, twist: int) -> int:
        if twist > 0:
            distance_to_click = self.dial_size - self.dial_position
            if distance_to_click > twist:
                return 0
            return math.floor((twist + self.dial_position)/ self.dial_size) 
        else:
            twist_mag = abs(twist)
            if self.dial_position > twist_mag:
                return 0
            return 1 + math.floor((twist_mag - self.dial_position)/ self.dial_size)

    def run(self, twist_list: list[str]) -> int:
        self.reset_clicks()
        for twist_notation in twist_list:
            twist = self._gauge_the_twist(twist_notation)
            self.clicks += self._twisted_through_click(twist)
            self._twist_the_dial(twist)
        return self.clicks
    

if __name__ == "__main__":
    data_path = Path(__file__).parent / "data" / "part_a.txt"
    data = genfromtxt(data_path, 'str')

    dial = range(100)
    start = 50

    lands_on_clicks = LandsOnClicks(start, dial)
    passes_through_clicks = PassesThroughClicks(start, dial)


    print("THE SOLUTION TO PART A IS...", lands_on_clicks.run(data))
    print("THE SOLUTION TO PART B IS...", passes_through_clicks.run(data))

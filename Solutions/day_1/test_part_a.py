from numpy import genfromtxt
from pathlib import Path

from solution import LandsOnClicks

dummy_data_path = Path(__file__).parent / "data" / "part_a_test.txt"
dummy_data = genfromtxt(dummy_data_path, 'str')

dial = range(100)    
start = 50           

def test_dummy():
    lands_on_clicks = LandsOnClicks(start, dial)
    expected_clicks = lands_on_clicks.run(dummy_data)
    assert expected_clicks == 3

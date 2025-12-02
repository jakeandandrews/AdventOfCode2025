from numpy import genfromtxt
from pathlib import Path

from part_a import count_the_clicks

dummy_data_path = Path(__file__).parent / "data" / "part_a_test.txt"
dummy_data = genfromtxt(dummy_data_path, 'str')

def test_dummy():
    assert count_the_clicks(dummy_data) == 3

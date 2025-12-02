from numpy import genfromtxt
from pathlib import Path

from part_a import lands_on_click

dummy_data_path = Path(__file__).parent / "data" / "part_a_test.txt"
dummy_data = genfromtxt(dummy_data_path, 'str')

def test_dummy():
    assert lands_on_click(dummy_data) == 3

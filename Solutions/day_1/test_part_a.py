from numpy import genfromtxt
from pathlib import Path

from part_a import crack_the_combination

dummy_data_path = Path(__file__).parent / "data" / "part_a_test.txt"
dummy_data = genfromtxt(dummy_data_path, 'str')

def test_dummy():
    assert crack_the_combination(dummy_data) == 3

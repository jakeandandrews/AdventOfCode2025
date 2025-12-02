from numpy import genfromtxt
from pathlib import Path

from part_a import solution

dummy_data_path = Path(__file__).parent / "data" / "test.txt"
dummy_data = genfromtxt(dummy_data_path, 'str')

def test_dummy():
    assert solution(dummy_data) == 3

from aocd import get_data
from datetime import date
import os

def main():
    today = date.today()
    day = today.day
    year = today.year
    folder = "data"
    os.makedirs(folder, exist_ok=True)  
    filename = os.path.join(folder, f"{today.isoformat()}.txt")

    if os.path.exists(filename):
        return

    puzzle_input = get_data(day=day, year=year)

    with open(filename, "w") as f:
        f.write(puzzle_input)

if __name__ == "__main__":
    main()
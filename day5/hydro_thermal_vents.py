import sys
from typing import List
import numpy as np

def avoid_danger(filename, part):
    with open(filename) as file:
        lines = file.readlines()
        horizontal_vents = get_horizontal_lines(lines)
        print(horizontal_vents)
        max_x = max([[x[0] for x in pair] for pair in horizontal_vents])[0]
        max_y = max([[y[1] for y in pair] for pair in horizontal_vents])[0]

        grid = np.zeros((max_x,max_y))
        # didn't finish

    return 0

def get_horizontal_lines(lines : List[str]):
    coordinates = []
    for line in lines:
        (x1y1, x2y2) = create_line_coords(line)
        if (x1y1[0] == x2y2[0] or x1y1[1] == x2y2[1]):
            coordinates.append((x1y1,x2y2))

    #print(coordinates)
    return coordinates

def create_line_coords(line: str):
    pairs = line.split('->')
    line_start = pairs[0].strip()
    line_end = pairs[1].strip()
    x1y1 = create_coordinate(line_start)
    x2y2 = create_coordinate(line_end)

    return (x1y1, x2y2)


def create_coordinate(line: str):
    # print(line)
    return [int(coord) for coord in line.split(',')]

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    num_overlapping_lines = avoid_danger(file,part)
    print(f"There are {num_overlapping_lines} areas where hydrothermal vents overlap. Be careful!")

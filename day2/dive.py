# Day 2 - Dive
# The submarine will execute a series of commands while moving along a planned course:

# Part 1
# 'forward X' increases the horizontal position by X units
# 'down X' increases the depth by X units
# 'up X' decreases the depth by X units.

# Part 2
# 'forward X' increases horizontal position by X units AND increases depth by 'aim' * 'X'
# 'down X' increases your aim by X units
# 'up X' decreases your aim by X units

# Multiply final horizontal position with final depth
import sys

def calculate_submarine_position(filename, part):
    final_horizontal_pos = 0
    final_depth = 0
    aim = 0

    with open(filename) as file:
        lines = file.readlines()

        if (part == '1'):

            horizontal_pos_lines = [line for line in lines if line.startswith('forward')]
            depth_lines = [line for line in lines if line.startswith('up') or line.startswith('down')]

            #print(horizontal_pos_lines)
            #print(depth_lines)

            final_horizontal_pos = calc_horizontal_pos(horizontal_pos_lines)
            final_depth = calc_depth(depth_lines)

        else: # part 2
            for line in lines:
                (command,paces) = parse_command(line)
                if (command == 'up'):
                    aim -= paces
                elif (command == 'down'):
                    aim += paces
                else: #command == forward
                    final_horizontal_pos += paces
                    final_depth += (aim*paces)

    return (final_horizontal_pos, final_depth)

def parse_command(line: str):
    (command, paces) = line.split(' ')
    return (command, int(paces))

def calc_horizontal_pos(lines: list[str]):
    positions = [parse_command(pos)[1] for pos in lines]
    #print(positions)

    return sum(positions)

def calc_depth(lines: list[str]):
    depth = 0
    for i in lines:
        (direction, paces) = parse_command(i)
        if direction == 'up':
            depth -= paces
        elif direction == 'down':
            depth += paces
    return depth


if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    (final_horizontal_pos, final_depth) = calculate_submarine_position(file, part)
    print(f'FINAL HORIZONTAL POS * FINAL DEPTH')
    print(f'{final_horizontal_pos} * {final_depth} = {final_horizontal_pos * final_depth}')

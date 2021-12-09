import sys

def find_low_points(filename, part):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        location_groups = get_locations(lines)
        low_points = []
        for group in location_groups:
            length = len(group[0])
            for i in range(length):
                current = group[1][i]
                if (i == 0):
                    left = 9
                else:
                    left = group[1][i-1]

                if (i == length-1):
                    right = 9
                else:
                    right = group[1][i+1]

                up = group[0][i]
                down = group[2][i]

                # print(f'current = {current}\nleft = {left}\nright = {right}\ndown = {down}')
                lowest = min([current,left,right,up,down])
                if current == lowest and lowest != 9:
                    # print(f'Low point = {current}')
                    low_points.append(current)

    return low_points

def get_locations(lines):
    it = iter(lines)
    length = len(lines[0])
    previous = [9]*length
    current = next(it)

    for next_item in it:
        yield (list(int(p) for p in previous),list(int(c) for c in current),list(int(n) for n in next_item))
        previous = current
        current = next_item

    yield(list(int(p) for p in previous),list(int(c) for c in current),list([9]*length))

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    low_points = find_low_points(file,part)
    print(low_points)
    risk_level = [i+1 for i in low_points]
    print(f'total risk level = {sum(risk_level)}')

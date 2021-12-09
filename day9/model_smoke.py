import sys

def find_low_points(filename, part):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
        location_groups = get_locations(lines)
        # [print(loc) for loc in locations]
        for group in location_groups:
            group_len = len(group[1]) #should always have values

            if (group[0]):
                h1 = [h for h in group[0]]
                print(h1)

            h2 = [h for h in group[1]]
            print(h2)

            if (group[2]):
                h3 = [h for h in group[2]]
                print(h3)
            # for loc in range(group_len):
            #     print()

    return [0]

def get_locations(lines):
    it = iter(lines)
    previous = None
    current = next(it)

    for next_item in it:
        yield (previous,current,next_item)
        previous = current
        current = next_item

    yield(previous,current,None)

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    low_points = find_low_points(file,part)
    risk_level = [i+1 for i in low_points]

# Day 1 - Sonar Sweep
# Count the number of times a depth measurement recorded in depth_measurements.txt increases from its previous value
# First measurement does not count
from io import TextIOWrapper
import sys

def track_depth_measurments(filename, measurment_metric):
    with open(filename) as file:
        if (measurment_metric == "singular"):
            return singular_depth_measurement_increases(file)
        elif (measurment_metric == "sliding"):
            return sliding_depth_measurement_increases(file)

def singular_depth_measurement_increases(file: TextIOWrapper):
    num_times_increased = 0
    num_times_decreased = 0
    distance_traveled = 0

    first_line = file.readline().rstrip()
    previous_measurement = int(first_line)
    print(f'{previous_measurement} (N/A First measurement)')

    while (line := file.readline().rstrip()):
        current_measurement = int(line)
        distance_traveled = current_measurement - int(first_line)
        status = str(current_measurement)

        if (current_measurement > previous_measurement):
            status += ' (increased!)'
            num_times_increased += 1

        elif (current_measurement < previous_measurement):
            status += ' (decreased!)'
            num_times_decreased += 1

        else:
            status += ' (No Change)'

        previous_measurement = current_measurement
        print(status)

    return (num_times_increased, num_times_decreased, distance_traveled)

def sliding_depth_measurement_increases(file: TextIOWrapper):
    num_times_increased = 0
    num_times_decreased = 0
    distance_traveled = 0

    measurements = [int(line) for line in file.readlines()]
    windows = []

    for i in range(len(measurements)):
        try:
            window = [measurements[i], measurements[i+1], measurements[i+2]]
            windows.append(window)
        except IndexError:
            #print("No more groups")
            break

    print(f'NUM WINDOWS = {len(windows)}')
    previous_window = sum(windows[0])
    print(f'({windows[0]}) = {previous_window}')
    rest_of_windows = windows[1:]

    for i in range(len(rest_of_windows)):
        current_window = sum(rest_of_windows[i])
        distance_traveled = current_window - sum(windows[0])
        has_increased = compare(current_window, previous_window)
        message = f'({windows[i]}) = {current_window}'

        if (has_increased > 0):
            num_times_increased += 1
            message += ' (increased!)'
        elif (has_increased < 0):
            num_times_decreased += 1
            message += ' (decreased!)'
        else:
            message += ' (no change)'

        previous_window = current_window
        print (message)

    return (num_times_increased, num_times_decreased, distance_traveled)

# returns 0 if n1 = n2
# returns 1 if n1 > n2
# returns -1 if n1 < n2
def compare(n1, n2):
    if (n1 == n2):
        return 0
    if (n1 > n2):
        return 1
    if (n1 < n2):
        return -1

if __name__ == '__main__':

    if (len(sys.argv) < 3):
        raise Exception("YOU FORGET SOMETHING?")

    file = sys.argv[1]
    measurement_metric = sys.argv[2]

    if (measurement_metric not in ["singular", "sliding"]):
        raise Exception("Set a measurement metric")

    (num_times_increased, num_times_decreased, total_distance_traveled) = track_depth_measurments(file, measurement_metric)

    print(f'\nNUM TIMES INCREASED = {num_times_increased}')
    print(f'\nNUM TIMES DECREASED = {num_times_decreased}')
    print(f'\nTOTAL DISTANCE TRAVELED = {total_distance_traveled}')
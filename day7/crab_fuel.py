import sys

def align_crab_subs(filename, part):
    with open(filename) as file:
        positions = [int(pos) for pos in file.readline().rstrip().split(',')]
        fuel_cost_dict = {}
        max_pos = max(positions)
        min_pos = min(positions)
        fuel_at_max = calc_fuel(max_pos, positions, part)

        for pos in range(min_pos,max_pos):
            fuel = calc_fuel(pos, positions, part)
            fuel_cost_dict[pos] = fuel
            best_fuel_cost = min(fuel_at_max, fuel)

        best_fuel_cost = min(fuel_cost_dict.values())
        print(best_fuel_cost)

        cheapest_pos = [key for key in fuel_cost_dict if fuel_cost_dict[key] == best_fuel_cost]

    return (cheapest_pos[0], best_fuel_cost)

def calc_fuel(pos, positions, part):
    if (part == '2'):
        return sum([step_cost(abs(num - pos)) for num in positions])
    else:
        return sum([abs(num - pos) for num in positions])

def step_cost(num_steps):
    return (num_steps*(num_steps+1))/2

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    (pos,fuel) = align_crab_subs(file,part)
    print(f"Crabs should align at horizontal position {pos} and will use {fuel} fuel units")

import sys

def simulate_lanternfish(filename, num_days):
    age_counts = [0,0,0,0,0,0,0,0,0]
    with open(filename) as file:
        fish_ages = [int(age) for age in file.readline().rstrip().split(',')]
        for age in fish_ages:
            age_counts[age]+=1

        print(age_counts)
        for day in range(int(num_days)):
            new_fish = age_counts.pop(0)
            print(new_fish)
            age_counts.append(new_fish)
            age_counts[6]+=new_fish
            print(age_counts)
            # fish_ages = [calc_age(age) for age in fish_ages] + [8 for num in range(num_new_fish)]
            # print(f'After {day} days. Adds {num_new_fish} new fish')
            # print(fish_ages)
    # print(age_counts)
    return sum(age_counts)


def calc_age(age: int):
    if (age == 0):
        return 6
    else:
        return age-1

if __name__ == '__main__':
    file = sys.argv[1]
    num_days = sys.argv[2]

    num_lanternfish = simulate_lanternfish(file,num_days)
    print(f"NUM LANTERNFISH AFTER {num_days} Days")
    print(num_lanternfish)

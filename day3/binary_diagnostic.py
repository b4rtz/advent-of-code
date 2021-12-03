import sys
from types import coroutine
from typing import BinaryIO

def check_power_consumption(filename, part):
    gamma_bits = [] #most common bit of each index of every line from the diagnostic report
    epsilon_bits = [] #least common bit of each index of every line from the diagnostic report
    bits_dict : dict[int,list[str]] = {} # key = line nr, value = list of bits at column index
    num_columns = 12

    with open(filename) as file:
        diagnostics = file.readlines()

        if (part == '1'):
            for i in range(len(diagnostics)):
                bits_list = [bit for bit in diagnostics[i].rstrip()]
                # print(f'bits list len = {len(bits_list)}')
                for j in range(len(bits_list)+1):
                    bits_dict[i] = bits_list[:j]

            for i in range(num_columns):
                column_bits = [bit[i] for bit in bits_dict.values()]
                print(column_bits)
                (most_common, least_common) = divide_bits(column_bits)
                gamma_bits.append(most_common)
                epsilon_bits.append(least_common)

            gamma_rate = convert_binary_to_decimal(gamma_bits)
            epsilon_rate = convert_binary_to_decimal(epsilon_bits)
            return (gamma_rate, epsilon_rate)

        if (part == '2'):
            oxygen_rate = 1
            co2_rate = 1
            for i in range(len(diagnostics)):
                bits_list = [bit for bit in diagnostics[i].rstrip()]
                # print(f'bits list len = {len(bits_list)}')
                for j in range(len(bits_list)+1):
                    bits_dict[i] = bits_list[:j]

            oxy_filter_list = bits_dict.values()
            # print(oxy_filter_list)
            #oxy_filter_list[0] = ['0', '1', '0', '1', '1', '1', '1', '1', '1', '0', '1', '1']
            for i in range(num_columns):
                # values = oxy_filter_list
                column_bits = [bit[i] for bit in oxy_filter_list]
                (most_common, least_common) = divide_bits(column_bits)
                bit_to_filter = most_common

                if (bit_to_filter == ''):
                    print("equal!")
                    bit_to_filter = 1
                else:
                    bit_to_filter = int(most_common)

                oxy_filter_list = [''.join(item) for item in oxy_filter_list if int(item[i]) == bit_to_filter]

                print(f'len of list = {len(oxy_filter_list)}')

                if len(oxy_filter_list) == 1:
                    oxygen_rate = convert_binary_to_decimal(oxy_filter_list)
                    print(f'oxy rate = {oxygen_rate}')
                    break

            co2_filter_list = bits_dict.values()
            print(f'len of list = {len(co2_filter_list)}')
            for i in range(num_columns):
                # values = co2_filter_list
                column_bits = [bit[i] for bit in co2_filter_list]
                (most_common, least_common) = divide_bits(column_bits)
                bit_to_filter == least_common

                if (bit_to_filter == ''):
                    print("equal!")
                    bit_to_filter = 0

                co2_filter_list = [''.join(item) for item in co2_filter_list if int(item[i]) == int(bit_to_filter)]

                print(f'len of list = {len(co2_filter_list)}')

                if len(co2_filter_list) == 1:
                    co2_rate = convert_binary_to_decimal(co2_filter_list)
                    print(f'co2 rate = {co2_rate}')
                    break

        return (oxygen_rate, co2_rate)

def keep_func(index, bit_to_filter, row):
    if (row[index] == bit_to_filter):
        return True
    else:
        return False

def divide_bits(bit_column: list[str]):

    # print(bit_column)
    ones = bit_column.count('1')
    zeros = bit_column.count('0')

    if ones > zeros:
        return ('1','0')
    elif zeros > ones:
        return ('0','1')
    else:
        return ('','')

def convert_binary_to_decimal(bin_list: list[str]):
    #print("probs like 10")
    binary_str = ''.join(bin_list)
    print(binary_str)
    dec = int(binary_str, 2)
    # print(dec)
    return dec

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    (diagnostic1, diagnostic2) = check_power_consumption(file, part)
    print(f'{diagnostic1} * {diagnostic2} = {diagnostic1 * diagnostic2}')

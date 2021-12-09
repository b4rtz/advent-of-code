import sys

# Segment Signals
# 0 => has len 6 && does not contain all signals from 4 && has all signals from 1
# 1 => has len 2
# 2 => has len 5 && is not a subset of 6
# 3 => has len 5 && is a subset of 7
# 4 => has len 4
# 5 => has len 5 && is a subset of 6
# 6 => has len 6 && does not contain signals from 4
# 7 => has len 3
# 8 => has len 7
# 9 => has len 6 & contains signals from 1 and 7 (or just not a 6)

def decode_segments(filename, part):
    with open(filename) as file:
        lines = file.readlines()
        signal_patterns = []
        output_digits = []
        for line in lines:
            entry = line.split('|')
            signal_patterns.append([signal for signal in entry[0].split(' ')])
            output_digits.append([digits for digits in entry[1].strip().split(' ')])

        if part == '1':
            encoded_digits_flat = [digit for four_digits in output_digits for digit in four_digits]
            count_easy = len([digit for digit in encoded_digits_flat if can_identify(digit)])
            print(f"Found {count_easy}")
        else:
            signals_decoded = []
            for signals in signal_patterns:
                signal_dict = decode_signals(signals)
                signals_decoded.append(signal_dict)

            output_sum = 0
            for o in range(len(output_digits)):
                decoded_outputs = decode_output(output_digits[o], signals_decoded[o])
                print(decoded_outputs)
                # print(output_digits[0])
                output_sum+=decoded_outputs

            print(f'OUTPUT SUM = {output_sum}')

def decode_output(output_digits, signal_dict):
    decoded = ''
    for digit in output_digits:
        chars_d = set([char for char in digit])
        # print(chars_d)
        num = [str(k) for k,v in signal_dict.items() if chars_d == set([char for char in v])][0]
        decoded+=num
    return int(decoded)

def decode_signals(signals):
    signal_dict = {get_num(signal):signal for signal in signals if can_identify(signal)}
    for signal in signals:
        length = len(signal)
        if (length == 6 and (is_not_subset_signal(signal, signal_dict[4]) and is_subset_signal(signal, signal_dict[1]))):
            signal_dict[0] = signal
        elif (length == 5 and is_subset_signal(signal, signal_dict[7])):
            signal_dict[3] = signal
        elif (length == 6 and is_not_subset_signal(signal, signal_dict[4])):
            signal_dict[6] = signal
        elif (length == 6 and is_subset_signal(signal, signal_dict[4])):
            signal_dict[9] = signal

    remainder = [signal for signal in signals if signal not in signal_dict.values() and len(signal) > 0]
    for r in remainder:
        if (is_subset_signal(signal_dict[6], r)):
            signal_dict[5] = r
        else:
            signal_dict[2] = r

    # for i in sorted(signal_dict.keys()):
    #     print(f'{i}:{signal_dict[i]}')
    return signal_dict

def is_not_subset_signal(signal, known_entry):
    return len([s for s in known_entry if s not in signal]) > 0

def is_subset_signal(signal, known_entry):
    return len([s for s in known_entry if s not in signal]) == 0

def can_identify(digit: str):
    known_lengths = [2,3,4,7]
    return len(digit) in known_lengths

def get_num(signal):
    length = len(signal)
    if length == 2:
        return 1
    elif length == 3:
        return 7
    elif length == 4:
        return 4
    elif length == 7:
        return 8

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    decode_segments(file,part)

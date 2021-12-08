import sys

# Segment Signals
# 0 = a,b,c,e,f,g
# 1 = c,f
# 2 = a,c,d,e,g
# 3 = a,c,d,f,g
# 4 = b,c,d,f
# 5 = a,b,d,f,g
# 6 = a,b,d,e,f,g
# 7 = a,c,f
# 8 = a,b,c,d,e,f,g
# 9 = a,b,c,d,f,g

def decode_segments(filename, part):
    a = ['a','c','e','d']
    with open(filename) as file:
        lines = file.readlines()
        signal_patterns = []
        output_digits = []
        for line in lines:
            entry = line.split('|')
            signal_patterns.append([signal for signal in entry[0].split(' ')])
            output_digits.append([digits for digits in entry[1].strip().split(' ')])

        output_digits = [digit for four_digits in output_digits for digit in four_digits]
        signal_patterns = [signal for signals in output_digits for signal in signals]
        # print(output_digits)
        count_easy = len([digit for digit in output_digits if can_identify(digit)])
        print(count_easy)


def can_identify(digit: str):
    known_lengths = [2,3,4,7]
    print(f'{digit} has len {len(digit)}')
    return len(digit) in known_lengths

if __name__ == '__main__':
    file = sys.argv[1]
    part = sys.argv[2]

    decode_segments(file,part)

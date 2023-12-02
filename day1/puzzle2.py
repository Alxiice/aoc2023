import re

digitsMapper = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def find_digits(sub):
    digits = [(i, x) for i, x in enumerate(sub) if x.isdigit()]
    for spelledDigit, nb in digitsMapper.items():
        digits += [(m.start(), str(nb)) for m in re.finditer(spelledDigit, sub)]
    return sorted(digits, key=lambda x: x[0])        

def get_value(_file):
    with open(_file, 'r') as fo:
        lines = [x for x in fo.read().split('\n') if x]
    total = 0
    for line in lines:
        digits = find_digits(line)
        total += int('{}{}'.format(digits[0][1], digits[-1][1]))
    return total

def test():
    return get_value('puzzle2_test.txt')

def main():
    return get_value('input.txt')

print("Test result : " + str(test()))
print("Result : " + str(main()))

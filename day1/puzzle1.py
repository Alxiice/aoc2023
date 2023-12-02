
def get_value(_file):
    with open(_file, 'r') as fo:
        lines = [x for x in fo.read().split('\n') if x]
    total = 0
    for line in lines:
        digits = [x for x in line if x.isdigit()]
        total += int('{}{}'.format(digits[0], digits[-1]))
    return total

def test():
    return get_value('puzzle1_test.txt')

def main():
    return get_value('input.txt')

print("Test result : " + str(test()))
print("Result : " + str(main()))

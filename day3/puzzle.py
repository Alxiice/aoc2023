
def build_symbol_map(content):
    symbol_map = {}
    for line_index, line in enumerate(content.split('\n')):
        for column_index, symbol in enumerate(line):
            if not symbol.isdigit() and symbol != '.':
                symbol_map[(line_index, column_index)] = True
    return symbol_map


def get_numbers(line):
    numbers = []
    current = []
    current_number = ''
    for col_index, symbol in enumerate(line):
        if symbol.isdigit():
            current.append(col_index)
            current_number += symbol
        elif current:
            current.append(int(current_number))
            numbers.append(tuple(current))
            current = []
            current_number = ''
    if current:
        current.append(int(current_number))
        numbers.append(tuple(current))
    return numbers


def is_position_adjacent_to_symbol(position, symbol_map):
    line, col = position
    # Test locations around the position
    # X -----X----- X
    # X (line, col) X
    # X -----X----- X
    positions_to_explore = [(i, j) for j in range(col - 1, col + 2) for i in range(line - 1, line + 2)]
    for position_candidate in positions_to_explore:
        if position_candidate in symbol_map.keys():
            return True


def is_adjacent_symbols(line_index, col_indices, symbol_map):
    for col_index in col_indices:
        position = (line_index, col_index)
        if is_position_adjacent_to_symbol(position, symbol_map):
            return True


def get_sum(_file):
    with open(_file, 'r') as fo:
        content = fo.read()
    # Build symbol map
    symbol_map = build_symbol_map(content)
    # Explore numbers
    sum_numbers = 0
    for line_index, line in enumerate(content.split('\n')):
        # [(0, 1, 2, 467), (5, 6, 7, 114)] ...
        numbers = get_numbers(line)
        for number in numbers:
            if is_adjacent_symbols(line_index, number[:-1], symbol_map):
                sum_numbers += number[-1]
    return sum_numbers


def test():
    puzzle_sum = get_sum('puzzle1_test.txt')
    assert(puzzle_sum == 4361)


def main():
    puzzle_sum = get_sum('input.txt')
    print('result : {}'.format(puzzle_sum))


if __name__ == '__main__':
    test()
    main()

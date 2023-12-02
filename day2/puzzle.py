


def min_nb_cubes(sub):
    subsets = sub.split(':')[1].split(';')
    minNbRed, minNbGreen, minNbBlue = 0, 0, 0
    for subset in subsets:
        colors = [x.strip() for x in subset.split(',')]
        # [(n, colorname), ...]
        colors = [(x.split(' ')[0], x.split(' ')[1]) for x in colors]
        for nbColor, colorName in colors:
            nbColor = int(nbColor)
            if colorName == 'red' and minNbRed < nbColor:
                minNbRed = nbColor
            if colorName == 'green' and minNbGreen < nbColor:
                minNbGreen = nbColor
            if colorName == 'blue' and minNbBlue < nbColor:
                minNbBlue = nbColor
    return (minNbRed, minNbGreen, minNbBlue)
    

def is_game_possible(sub, redCubes, greenCubes, blueCubes):
    minNbRed, minNbGreen, minNbBlue = min_nb_cubes(sub)
    if redCubes < minNbRed or greenCubes < minNbGreen or blueCubes < minNbBlue:
        return False
    if redCubes + greenCubes + blueCubes < minNbRed + minNbGreen + minNbBlue:
        return False
    return True


def which_game_is_possible(_file):
    with open(_file, 'r') as fo:
        games = [x for x in fo.read().split('\n') if x]
    sumGamePassed = 0
    for game in games:
        gameNb = int(game.split(':')[0].split(' ')[1].strip())
        gamePossible = is_game_possible(game, 12, 13, 14)
        if gamePossible: 
            sumGamePassed += gameNb
    return sumGamePassed


def get_game_power(sub):
    minRed, minGreen, minBlue = min_nb_cubes(sub)
    return minRed * minGreen * minBlue


def get_sum_games_power(_file):
    with open(_file, 'r') as fo:
        games = [x for x in fo.read().split('\n') if x]
    sum_game_powers = 0
    for game in games:
        gameNb = int(game.split(':')[0].split(' ')[1].strip())
        gamePower = get_game_power(game)
        sum_game_powers += gamePower
        # print('game {} : power = {}'.format(gameNb, gamePower))
    return sum_game_powers


def part1():
    # Test
    sum_ids = which_game_is_possible('testInput.txt')
    assert (sum_ids == 8)
    print('test passed')
    # Real
    print('real game : {}'.format(which_game_is_possible('input.txt')))


def part2():
    # Test
    sum_game_powers = get_sum_games_power('testInput.txt')
    assert (sum_game_powers == 2286)
    print('test passed')
    # Real
    print('real game : {}'.format(get_sum_games_power('input.txt')))


if __name__ == '__main__':
    print('PUZZLE 1')
    part1()
    print('\nPUZZLE 2')
    part2()
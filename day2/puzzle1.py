


def is_game_possible(sub, redCubes, greenCubes, blueCubes):
    subsets = sub.split(':')[1].split(';')
    maxNbRed, maxNbGreen, maxNbBlue = 0, 0, 0
    for subset in subsets:
        colors = [x.strip() for x in subset.split(',')]
        # [(n, colorname), ...]
        colors = [(x.split(' ')[0], x.split(' ')[1]) for x in colors]
        for nbColor, colorName in colors:
            nbColor = int(nbColor)
            if colorName == 'red' and maxNbRed < nbColor:
                maxNbRed = nbColor
            if colorName == 'green' and maxNbGreen < nbColor:
                maxNbGreen = nbColor
            if colorName == 'blue' and maxNbBlue < nbColor:
                maxNbBlue = nbColor
    if redCubes < maxNbRed or greenCubes < maxNbGreen or blueCubes < maxNbBlue:
        return False
    if redCubes + greenCubes + blueCubes < maxNbRed + maxNbGreen + maxNbBlue:
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


# Test
sum_ids = which_game_is_possible('puzzle1_test.txt')
assert (sum_ids == 8)
print('test passed')
# Real
print('real game : {}'.format(which_game_is_possible('input.txt')))

from functools import reduce 


def get_gain(input):
    with open(input, "r") as fo:
        lines = [x for x in fo.read().split('\n') if x]
    total = 0
    for line in lines:
        winning_numbers = [int(x) for x in line.split(":")[1].split("|")[0].split(" ") if x]
        actual_numbers  = [int(x) for x in line.split(":")[1].split("|")[1].split(" ") if x]
        nb_winning = len([x for x in actual_numbers if x in winning_numbers])
        card_value = 2 ** (nb_winning - 1) if nb_winning >= 1 else 0
        total += card_value
    return total


def get_pile_scratchcards(input):
    with open(input, "r") as fo:
        lines = [x for x in fo.read().split('\n') if x]
    cards_iterations = {}
    for line in lines:
        card_nb = int(line.split(":")[0].split(" ")[-1])
        # Add original card copy
        if card_nb not in cards_iterations:
            cards_iterations[card_nb] = 0
        cards_iterations[card_nb] += 1
        winning_numbers = [int(x) for x in line.split(":")[1].split("|")[0].split(" ") if x]
        actual_numbers  = [int(x) for x in line.split(":")[1].split("|")[1].split(" ") if x]
        nb_winning = len([x for x in actual_numbers if x in winning_numbers])
        won_cards = list(range(card_nb + 1, card_nb + 1 + nb_winning))
        for won_card in won_cards:
            if won_card not in cards_iterations:
                cards_iterations[won_card] = 0
            cards_iterations[won_card] += cards_iterations[card_nb]
    return sum(cards_iterations.values())


def part1():
    print("=== PART 1 ===")
    out = get_gain("test.txt")
    assert(out == 13)
    print("Test passed !")
    out = get_gain("input.txt")
    print("Result : {}".format(out))


def part2():
    print("=== PART 2 ===")
    out = get_pile_scratchcards("test.txt")
    assert(out == 30)
    print("Test passed !")
    out = get_pile_scratchcards("input.txt")
    print("Result : {}".format(out))


if __name__ == "__main__":
    part1()
    part2()
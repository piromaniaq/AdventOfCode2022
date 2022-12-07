def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def total(rounds):
    outcomes = {
        "A X":3, "A Y":4, "A Z":8,
        "B X":1, "B Y":5, "B Z":9,
        "C X":2, "C Y":6, "C Z":7
    }
    points = 0
    for round in rounds:
        points += outcomes[round]
    return points


if __name__ == '__main__':
    input = get_data('input.txt')
    answer = total(input)
    print(answer)

    #OUTCOMES
    # A vs X = LOSE = 3 + 0 = 3
    # A vs Y = DRAW = 1 + 3 = 4
    # A vs Z = WIN  = 2 + 6 = 8
    # B vs X = LOSE = 1 + 0 = 1
    # B vs Y = DRAW = 2 + 3 = 5
    # B vs Z = WIN  = 3 + 6 = 9
    # C vs X = LOSE = 2 + 0 = 2
    # C vs Y = DRAW = 3 + 3 = 6
    # C vs Z = WIN  = 1 + 6 = 7

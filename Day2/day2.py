def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def total(rounds):
    outcomes = {
        "A X":4, "A Y":8, "A Z":3,
        "B X":1, "B Y":5, "B Z":9,
        "C X":7, "C Y":2, "C Z":6
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
    # A vs X = DRAW = 1 + 3 = 4
    # A vs Y = WIN  = 2 + 6 = 8
    # A vs Z = LOSE = 3 + 0 = 3
    # B vs X = LOSE = 1 + 0 = 1
    # B vs Y = DRAW = 2 + 3 = 5
    # B vs Z = WIN  = 3 + 6 = 9
    # C vs X = WIN  = 1 + 6 = 7
    # C vs Y = LOSE = 2 + 0 = 2
    # C vs Z = DRAW = 3 + 3 = 6

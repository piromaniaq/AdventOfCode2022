def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def carry(food):
    count = 0
    fat = 0
    for calories in food:
        if calories == '':
            count = 0
        else:
            caloriesint = int(calories)
            count += caloriesint

        if count > fat:
            fat = count
    return fat


if __name__ == '__main__':
    input = get_data('input.txt')
    print(carry(input))
def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


def carry(hungry):
    sumFat = 0
    listFatSums = []
    for line in hungry:
        if line.strip() == "":
            listFatSums.append(sumFat)
            sumFat = 0
        else:
            sumFat += int(line)
    listFatSums.sort(reverse=True)
    return listFatSums[0] + listFatSums[1] + listFatSums[2]


if __name__ == '__main__':
    input = get_data('input.txt')
    print(carry(input))
def get_data(file):
    with open(file, 'r') as f:
        data = f.read().splitlines()
    return data


if __name__ == '__main__':
    input = get_data('input.txt')
    print(type(input))
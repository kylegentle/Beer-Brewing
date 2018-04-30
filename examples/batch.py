def main():
    batch = BeerBatch()
    abv = batch.ABV()
    print(f'ABV for this batch is {abv}%')


class BeerBatch:
    def __init__(self):
        self.OG = get_float('Enter Original Gravity: ')
        self.FG = get_float('Enter Final Gravity: ')

    def ABV(self):
        return round(131.25 * (self.OG - self.FG), 2)


def get_float(message):
    user_input = input(message)
    try:
        return float(user_input)
    except ValueError:
        print('Invalid input; gravity measurement must be a number.')
        return get_float(message)
        

if __name__ == '__main__':
    main()

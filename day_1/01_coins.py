import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(['heads', 'tails'])  # random: heads/tails
        return self.side

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
def list_of_coins(length):
    list = []
    for i in range(length):
        list.append(Coin.flip(Coin))
    return(list)

# выведите соотношение выпавших орлов и решек в процентах
def coins_proportion(count_of_coins):
    list_1 = list_of_coins(count_of_coins)
    heads = int(len([coin for coin in list_1 if coin == 'heads'])/len(list_1)*100)
    tails = 100 - heads
    print(f'монеты: {", ".join(map(str,list_1))}')
    print(f'heads {heads}%')
    print(f'tails {tails}%')


coins_proportion(10)
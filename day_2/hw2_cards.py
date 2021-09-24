import itertools
import random
import time

from deck_total import Card, Desk

'''
создадим имитацию одного хода в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 6 карт
3. Второй игрок берет сверху 6 карт.
4. Игрок-1 ходит:
    1. игрок-1 выкладывает самую маленькую карту по значению
    2. игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
    3. Если игрок-2 не может побить карту, то он проигрывает.
    4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Выведите в консоль максимально наглядную визуализацию данного игрового хода.
'''


class Cards_on_hands(object):
    def __init__(self):
        self.cards_on_hands = []
        self.turn = None
        self.origin = None
        self.check_continue = None
        self.last_card = None

    def get_var_name(self):
        for k, v in globals().items():
             if v is self:
                return k

    # вывод карт игрока
    def printer_cards(self):
        print("Игрок " + self.get_var_name() + " имеет карты " + " ".join([str(elem) for elem in self.cards_on_hands]))

    # игрок берет карту
    def adds(self, cards):
        self.cards_on_hands.append(cards)

    # определение минимальной карты
    def min_card(self, origin):
        self.origin = origin
        minimum = self.origin[0]
        for card in self.origin:
            if card < minimum:
                minimum = card
        return minimum

    def first_turn(self):
        self.turn = self.min_card(self.cards_on_hands)
        self.cards_on_hands.remove(self.turn)
        print("Игрок " + self.get_var_name() + " делает ход " + self.turn.to_str())

    def fight_back(self, other):
        possible = []
        for card in self.cards_on_hands:
            if card.equal_suit(other) and card > other:
                possible.append(card)
        if not possible:
            print("Игрок " + self.get_var_name() + " проиграл")
            self.check_continue = 0
        else:
            self.last_card = self.min_card(possible)
            print("Игрок " + self.get_var_name() + " отбивается " + self.last_card.to_str())
            self.cards_on_hands.remove(self.last_card)
            self.check_continue = 1

    def throw(self, enemy):
        if enemy.check_continue == 1:
            same_suit = []
            for i in self.cards_on_hands:
                if i.value == enemy.last_card.value:
                    same_suit.append(i)
            if same_suit:
                print("Игрок " + self.get_var_name() + " подкидывает " + " ".join([str(elem) for elem in same_suit]))

# Создаем колоду из 52 карт и перемешиваем ее
deck_of_cards = []
deck = Desk()

for card in itertools.product(deck.values, deck.suits):
    deck_of_cards.append(Card(card[0], card[1]))

# перемешаем карты
random.shuffle(deck_of_cards)

# Игроки берут карты
player1 = Cards_on_hands()
for card in deck_of_cards[0:6]:
    player1.adds(card)

player2 = Cards_on_hands()
for card in deck_of_cards[6:12]:
    player2.adds(card)

# оставшиеся карты в колоде
deck_of_cards = deck_of_cards[12:]

if __name__ == '__main__':
    time.sleep(1.5)
    player1.printer_cards()
    time.sleep(1.5)
    player2.printer_cards()
    time.sleep(1.5)
    player1.first_turn()
    time.sleep(1.5)
    player2.fight_back(player1.turn)
    time.sleep(1.5)
    player1.throw(player2)



class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        out = ''
        if self.suit == 'Hearts':
            out = '\u2665'
        if self.suit == 'Diamonds':
            out = '\u2666'
        if self.suit == 'Clubs':
            out = '\u2663'
        if self.suit == 'Spades':
            out = '\u2660'
        return self.value + out

    def __str__(self):
        suits = {'Hearts': '\u2665',
                 'Diamonds': '\u2666',
                 'Clubs': '\u2663',
                 'Spades': '\u2660'}
        return self.value + suits[self.suit]

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    # more method
    def __gt__(self, other_card):
        if Desk.values.index(self.value) == Desk.values.index(other_card.value):
            return Desk.suits.index(self.suit) > Desk.suits.index(other_card.suit)
        else:
            return Desk.values.index(self.value) > Desk.values.index(other_card.value)

    # less method
    def __lt__(self, other_card):
        if Desk.values.index(self.value) == Desk.values.index(other_card.value):
            return Desk.suits.index(self.suit) < Desk.suits.index(other_card.suit)
        else:
            return Desk.values.index(self.value) < Desk.values.index(other_card.value)


class Desk:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

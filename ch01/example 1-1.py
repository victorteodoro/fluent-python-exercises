import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades clubs diamonds hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# Play around with the class possibilities
deck = FrenchDeck()

print("The size of the deck is", len(deck), "cards")
print("The first card is", deck[0])
print("The last card is", deck[-1])

print("A random card from the deck:", choice(deck))
print("Another random card from the deck:", choice(deck))
print("Yet antoher random card from the deck:", choice(deck))

print("A slice of the 3 first cards of the deck:", deck[:3])

print("Is the queen of hearts in the deck?", Card('Q', 'hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


print("The cards in sorted order are:")
for card in sorted(deck, key=spades_high):
    print(card)

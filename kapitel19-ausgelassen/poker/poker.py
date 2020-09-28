#!/usr/bin/env python3
"""
Würfelpoker
===========

Demonstriert ein Objektorientiertes Programm.

Spielen Sie eine Runde Würfelpoker. Die Regeln entsprechen dem
"Würfelpoker" Minispiel aus dem Computerspiel "The Witcher".

https://witcher.fandom.com/wiki/The_Witcher_dice_poker

Regeln
------

 - Jeder Spieler hat 5 Würfel
 - Das Ziel ist es, die Höchste Punktzahl zu erreichen
 - Nach dem Würfeln einer Hand darf der Spieler eine beliebige Zahl Würfel
   erneut würfeln
 - Lesen Sie die Tests, um die möglichen Punkte einer Hand zu erlernen

"""
import secrets
from collections import Counter
from animation import DieRollAnimation


class Die:
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return f'<Die: {self._value}>'

    def __str__(self):
        return str(self._value)

    def __hash__(self):
        return self._value

    def __eq__(self, other):
        return self._value == other._value

    def __lt__(self, other):
        return self._value < other._value

    def __int__(self):
        '''PIPS'''
        return self._value

    @classmethod
    def roll(cls):
        return Die(secrets.choice((1, 2, 3, 4, 5, 6)))


class _Hand:
    _RANK = 0
    _ICON = ' '

    def __init__(self, dice):
        self._dice = dice

    def __lt__(self, other):
        """
        Compare this hand to another.

        Hands outrank each other, e.g. "Five of a Kind" outranks a "Full House"
        When the ranks are tied, the higher sum wins.
        """
        # if isinstance(self, type(other)):

        return (self._RANK, self.sum()) < (other._RANK,  other.sum())

    def __iter__(self):
        yield from sorted(self._dice or [])

    def loose_dice(self):
        """
        Returns the dice that do not contribute to the hand.
        E.g. A in a hand of "One Pair" 5,5,1,2,3 the dice 1,2,3 are loose
        """
        raise NotImplemented

    def reroll_loose_dice(self):
        loose = self.loose_dice()
        for die in self:
            if die not in loose:
                yield die
            else:
                yield Die.roll()

    def sum(self):
        return sum(int(die) for die in self)

    def __str__(self):
        icon = self._ICON
        name = self.__class__.__name__
        dice = ','.join([str(die) for die in sorted(self._dice)])
        return f'{icon} {name}: {dice}'


class FiveOfAKind(_Hand):
    """
    E.g. 5,5,5,5,5
    """
    _RANK = 9
    _ICON = '🖐️'

    @staticmethod
    def test(dice):
        return len(set(dice)) == 1

    def loose_dice(self):
        return []


class FourOfAKind(_Hand):
    """
    E.g. 5,5,5,5,1
    """
    _RANK = 8
    _ICON = '🍀'

    @staticmethod
    def test(dice):
        head, *_ = Counter(dice).most_common()
        die, count = head
        return count == 4

    def loose_dice(self):
        dice = Counter(self._dice).most_common()
        return [die for die, count in dice if count != 4]


class FullHouse(_Hand):
    """
    One Triplet, One Pair, e.g. 5,5,5,1,1
    """
    _RANK = 7
    _ICON = '🏠'

    @staticmethod
    def test(dice):
        dist = Counter(dice).most_common()
        if len(dist) != 2:
            return False
        first, second = dist
        die_, count_first = first
        die_, count_second = second
        return count_first == 3 and count_second == 2

    def loose_dice(self):
        return []


class HighStraight(_Hand):
    """
    i.e. 6,5,4,3,2
    """
    _RANK = 6
    _ICON = '🏎️'

    @staticmethod
    def test(dice):
        return set(dice) == {Die(6), Die(5), Die(4), Die(3), Die(2)}

    def loose_dice(self):
        return []


class LowStraight(_Hand):
    """
    i.e. 5,4,3,2,1
    """
    _RANK = 5
    _ICON = '🚗'

    @staticmethod
    def test(dice):
        return set(dice) == {Die(5), Die(4), Die(3), Die(2), Die(1)}

    def loose_dice(self):
        return []


class ThreeOfAKind(_Hand):
    """
    e.g. 5,5,5,1,2
    """
    _RANK = 4
    _ICON = '☘️'

    @staticmethod
    def test(dice):
        head, *tail = Counter(dice).most_common()
        die, count = head
        return count == 3 and len(tail) == 2

    def loose_dice(self):
        dist = Counter(self._dice).most_common()
        return [die for die, count in dist if count != 3]


class TwoPairs(_Hand):
    """
    e.g. 5,5,3,3,3
    """
    _RANK = 3
    _ICON = '🌟'

    @staticmethod
    def test(dice):
        dist = Counter(dice).most_common()
        return len(dist) == 3 and dist[0][1] == 2 and dist[1][1] == 2

    def loose_dice(self):
        dist = Counter(self._dice).most_common()
        return [die for die, count in dist if count == 1]


class OnePair(_Hand):
    """
    e.g. 5,5,3,2,1
    """
    _RANK = 2
    _ICON = '⭐'

    @staticmethod
    def test(dice):
        dist = Counter(dice).most_common()
        return len(dist) == 4 and dist[0][1] == 2

    def loose_dice(self):
        dist = Counter(self._dice).most_common()
        return [die for die, count in dist if count != 2]


class Runt(_Hand):
    """
    e.g. 6,5,3,2,1
    """
    _RANK = 1
    _ICON = '💩'

    @staticmethod
    def test(dice):
        raise NotImplemented()

    def loose_dice(self):
        return self._dice


class Dice:
    _hands = [
        FiveOfAKind,
        FourOfAKind,
        FullHouse,
        HighStraight,
        LowStraight,
        ThreeOfAKind,
        TwoPairs,
        OnePair
    ]

    def __init__(self, dice):
        self._dice = dice

    def hand(self):
        for Hand in self._hands:
            if Hand.test(self._dice):
                return Hand(self._dice)
        return Runt(self._dice)

    @classmethod
    def roll(cls):
        dice = [Die.roll() for _ in range(5)]
        return Dice(dice).hand()


class Player:
    """
    A human player who gets to choose what to do.
    """

    def first_hand(self):
        return Dice.roll()

    def _reroll_dice(self, dice_indices, first_hand):
        for i, die in enumerate(first_hand, start=1):
            if i in dice_indices:
                yield Die.roll()
            else:
                yield die

    def _choice(self, first_hand):
        print("You've got:", first_hand)
        s = input("> ").strip()
        if not s:
            return first_hand

        if 'all' in s:
            return Dice.roll()

        dice_indices = {int(d) for d in s.split(' ')}
        dice = list(self._reroll_dice(dice_indices, first_hand))
        return Dice(dice).hand()

    def second_hand(self, first_hand):
        return self._choice(first_hand)
        # while True:
        #     try:
        #     except:
        #         pass


class Novice:
    """
    Rerolls every time.

    The novice doesn't know any combinations
    and simply playes by chance.
    """

    def __init__(self):
        pass

    def first_hand(self):
        return Dice.roll()

    def second_hand(self, first_hand):
        # Better: Rerolling all each time:
        # Improves 4_871_709 times out of 10_000_000

        # Worse: Rerolling all when there are loose dice:
        # Improves 4_836_385 times out of 10_000_000
        return Dice.roll()


class Adept(Novice):
    """
    Rerolls only dice that don't contribute to actual hand,
    in hopes to improve their hand.
    """

    def second_hand(self, first_hand):
        # Improves 6_981_030 out of 10_000_000
        if first_hand.loose_dice():
            dice = list(first_hand.reroll_loose_dice())
            return Dice(dice).hand()
        return first_hand


class SmartPlayer(Novice):
    """
    Smart Player also checks
    if a runt can be made into a Straight
    """
    pass


class VigilantPlayer(Novice):
    """
    Vigilant Player considers your hand, too
    """
    pass


ANIMATION_DURATION_S = 0.5


def animate(label, dice):
    print(label)
    DieRollAnimation(ANIMATION_DURATION_S).animate(dice)


if __name__ == '__main__':

    # Ändern Sie den Adepten zu einer anderen Klasse
    # Oder implementieren Sie Ihre eigene Strategie!
    player, opponent = Player(), Adept()

    p1 = player.first_hand()
    e1 = opponent.first_hand()

    animate('🐮 You:', p1)
    animate('🤖 Opponent:', e1)

    p2 = player.second_hand(p1)
    e2 = opponent.second_hand(e1)

    if p1 is not p2:
        animate('🐮 You:', p2)

    print(f"🐮 You: {p2}")

    if e1 is not e2:
        animate('🤖 Opponent:', e2)

    print(f"🤖 Opponent: {e2}")

    if p2 > e2:
        print('👑👑👑 YOU WIN 👑👑👑')
        exit()

    if p2 < e2:
        print('💩💩💩 YOU LOSE 💩💩💩')
        exit()

    print('👉👉👉 TIE 👈👈👈')


'''
Suggestions for Player icons
https://emojipedia.org/nature/
'''


'''
Suggestions for Opponent Icons
⚔️ Crossed Swords
👻 Ghost
👽 Alien
👾 Alien Monster
🤖 Robot
'''

from poker import *
import unittest


class Hands(unittest.TestCase):
    # https://de.wikipedia.org/wiki/Poker_Dice
    def test_five_of_a_kind(self):
        # '4,4,4,4,4'
        dice = [Die(1), Die(1), Die(1), Die(1), Die(1)]
        self.assertTrue(FiveOfAKind.test(dice))

        dice = [Die(2), Die(1), Die(1), Die(1), Die(1)]
        self.assertFalse(FiveOfAKind.test(dice))

    def test_four_of_a_kind(self):
        # '4,4,4,4,1'
        dice = [Die(1), Die(1), Die(1), Die(1), Die(1)]
        self.assertFalse(FourOfAKind.test(dice))

        dice = [Die(2), Die(1), Die(1), Die(1), Die(1)]
        self.assertTrue(FourOfAKind.test(dice))

        dice = [Die(2), Die(2), Die(1), Die(1), Die(1)]
        self.assertFalse(FourOfAKind.test(dice))

    def test_full_house(self):
        # 4,4,4,2,2
        dice = [Die(2), Die(2), Die(1), Die(1), Die(1)]
        self.assertTrue(FullHouse.test(dice))

        dice = [Die(2), Die(2), Die(2), Die(1), Die(1)]
        self.assertTrue(FullHouse.test(dice))

        dice = [Die(2), Die(2), Die(2), Die(2), Die(1)]
        self.assertFalse(FullHouse.test(dice))

    def test_high_straight(self):
        # 6,5,4,3,2
        dice = [Die(6), Die(5), Die(4), Die(3), Die(2)]
        self.assertTrue(HighStraight.test(dice))

        dice = [Die(5), Die(5), Die(4), Die(2), Die(2)]
        self.assertFalse(HighStraight.test(dice))

    def test_low_straight(self):
        # 5,4,3,2,1
        dice = [Die(5), Die(4), Die(3), Die(2), Die(1)]
        self.assertTrue(LowStraight.test(dice))

        dice = [Die(5), Die(5), Die(4), Die(2), Die(2)]
        self.assertFalse(LowStraight.test(dice))

    def test_three_of_a_kind(self):
        # 5,5,5,2,1
        dice = [Die(5), Die(5), Die(5), Die(2), Die(1)]
        self.assertTrue(ThreeOfAKind.test(dice))

        dice = [Die(5), Die(5), Die(5), Die(1), Die(1)]
        self.assertFalse(ThreeOfAKind.test(dice))

        dice = [Die(1), Die(2), Die(3), Die(4), Die(5)]
        self.assertFalse(ThreeOfAKind.test(dice))

    def test_two_pairs(self):
        # e.g. 5,5,2,2,1
        dice = [Die(5), Die(5), Die(2), Die(2), Die(1)]
        self.assertTrue(TwoPairs.test(dice))

        dice = [Die(5), Die(5), Die(5), Die(1), Die(1)]
        self.assertFalse(TwoPairs.test(dice))

        dice = [Die(1), Die(2), Die(3), Die(4), Die(5)]
        self.assertFalse(TwoPairs.test(dice))

    def test_one_pair(self):
        # e.g. 5,5,3,2,1
        dice = [Die(5), Die(5), Die(3), Die(2), Die(1)]
        self.assertTrue(OnePair.test(dice))

        dice = [Die(5), Die(5), Die(2), Die(2), Die(1)]
        self.assertFalse(OnePair.test(dice))

        dice = [Die(1), Die(2), Die(3), Die(4), Die(5)]
        self.assertFalse(OnePair.test(dice))

    def test_one_pair_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,5,3,2,1 --> 3,2,1
        a, b, c, d, e = Die(5), Die(5), Die(3), Die(2), Die(1)
        dice = (a, b, c, d, e)
        loose_dice = OnePair(dice).loose_dice()
        self.assertFalse(a in loose_dice)
        self.assertFalse(b in loose_dice)
        self.assertTrue(c in loose_dice)
        self.assertTrue(d in loose_dice)
        self.assertTrue(e in loose_dice)

    def test_two_pairs_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,5,3,3,1 --> 1
        a, b, c, d, e = Die(5), Die(5), Die(3), Die(3), Die(1)
        dice = (a, b, c, d, e)
        loose_dice = TwoPairs(dice).loose_dice()
        self.assertFalse(a in loose_dice)
        self.assertFalse(b in loose_dice)
        self.assertFalse(c in loose_dice)
        self.assertFalse(d in loose_dice)
        self.assertTrue(e in loose_dice)

    def test_three_of_a_kind_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,5,5,3,1 --> 3,1
        a, b, c, d, e = Die(5), Die(5), Die(5), Die(3), Die(1)
        dice = (a, b, c, d, e)
        loose_dice = ThreeOfAKind(dice).loose_dice()
        self.assertFalse(a in loose_dice)
        self.assertFalse(b in loose_dice)
        self.assertFalse(c in loose_dice)
        self.assertTrue(d in loose_dice)
        self.assertTrue(e in loose_dice)

    def test_low_straight_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,4,3,2,1 --> {}
        a, b, c, d, e = Die(5), Die(5), Die(3), Die(2), Die(1)
        dice = (a, b, c, d, e)
        loose_dice = LowStraight(dice).loose_dice()
        self.assertEqual(loose_dice, [])

    def test_high_straight_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 6,5,4,3,2 --> {}
        a, b, c, d, e = Die(5), Die(5), Die(3), Die(2), Die(1)
        dice = (a, b, c, d, e)
        loose_dice = HighStraight(dice).loose_dice()
        self.assertEqual(loose_dice, [])

    def test_full_house_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,5,5,3,3 --> {}
        a, b, c, d, e = Die(5), Die(5), Die(5), Die(3), Die(3)
        dice = (a, b, c, d, e)
        loose_dice = FullHouse(dice).loose_dice()
        self.assertEqual(loose_dice, [])

    def test_four_of_a_kind_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,5,5,5,3 --> 3
        a, b, c, d, e = Die(5), Die(5), Die(5), Die(5), Die(3)
        dice = (a, b, c, d, e)
        loose_dice = FourOfAKind(dice).loose_dice()
        self.assertFalse(a in loose_dice)
        self.assertFalse(b in loose_dice)
        self.assertFalse(c in loose_dice)
        self.assertFalse(d in loose_dice)
        self.assertTrue(e in loose_dice)

    def test_five_of_a_kind_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,5,5,5,5 --> {}
        a, b, c, d, e = Die(5), Die(5), Die(5), Die(5), Die(5)
        dice = (a, b, c, d, e)
        loose_dice = FiveOfAKind(dice).loose_dice()
        self.assertEqual(loose_dice, [])

    def test_runt_loose_dice(self):
        # Returns the dice that can be rerolled
        # e.g. 5,5,5,5,5 --> {}
        a, b, c, d, e = Die(5), Die(5), Die(5), Die(5), Die(5)
        dice = [a, b, c, d, e]
        loose_dice = Runt(dice).loose_dice()
        self.assertEqual(loose_dice, dice)

    def test_hand_ranks(self):
        dice = None
        self.assertTrue(
            FiveOfAKind(dice) >
            FourOfAKind(dice) >
            FullHouse(dice) >
            HighStraight(dice) >
            LowStraight(dice) >
            ThreeOfAKind(dice) >
            TwoPairs(dice) >
            OnePair(dice) >
            Runt(dice)
        )

    def test_tied_ranks(self):
        '''
        If it is a tie, the higher sum wins
        '''

        self.assertTrue(
            FiveOfAKind((Die(5), Die(5), Die(5), Die(5), Die(5))) >
            FiveOfAKind((Die(3), Die(3), Die(3), Die(3), Die(3)))
        )

        self.assertTrue(
            FourOfAKind((Die(5), Die(5), Die(5), Die(5), Die(1))) >
            FourOfAKind((Die(3), Die(3), Die(3), Die(3), Die(1)))
        )

        self.assertTrue(
            FullHouse((Die(5), Die(5), Die(5), Die(2), Die(2))) >
            FullHouse((Die(3), Die(3), Die(3), Die(1), Die(1)))
        )

        # Can't decide on sum for high straight
        self.assertFalse(
            HighStraight((Die(6), Die(5), Die(4), Die(3), Die(2))) >
            HighStraight((Die(6), Die(5), Die(4), Die(3), Die(2)))
        )

        # Can't decide on sum for low straight
        self.assertFalse(
            LowStraight((Die(5), Die(4), Die(3), Die(2), Die(1))) >
            LowStraight((Die(5), Die(4), Die(3), Die(2), Die(1)))
        )

        self.assertTrue(
            TwoPairs((Die(5), Die(5), Die(3), Die(3), Die(1))) >
            TwoPairs((Die(3), Die(3), Die(2), Die(2), Die(1)))
        )

        self.assertTrue(
            OnePair((Die(5), Die(5), Die(3), Die(2), Die(1))) >
            OnePair((Die(4), Die(4), Die(3), Die(2), Die(1)))
        )

        self.assertFalse(
            Runt((Die(6), Die(4), Die(3), Die(2), Die(1))) >
            Runt((Die(6), Die(4), Die(3), Die(2), Die(1)))
        )

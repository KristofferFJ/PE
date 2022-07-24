import operator
import unittest
from typing import List

strengths = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["C", "S", "H", "D"]
hand_strengths = ["HIGH_CARD", "ONE_PAIR", "TWO_PAIRS", "THREE_OF_A_KIND", "STRAIGHT", "FLUSH", "FULL_HOUSE",
                  "FOUR_OF_A_KIND", "STRAIGHT_FLUSH", "ROYAL_FLUSH"]


class Card:
    def __init__(self, card: str):
        assert len(card) == 2
        self.size = card[0]
        self.suit = card[1]
        self.strength = strengths.index(self.size)


class Hand:
    def __init__(self, cards: List[Card]):
        assert len(cards) == 5
        self.cards: List[Card] = cards
        self.cards.sort(key=operator.attrgetter('strength'), reverse=True)

    def get_hand_strength(self) -> int:
        return hand_strengths.index(self.get_hand())

    def get_hand(self):
        if self.has_royal_flush():
            return "ROYAL_FLUSH"
        if self.has_straight_flush():
            return "STRAIGHT_FLUSH"
        if self.has_four_of_a_kind():
            return "FOUR_OF_A_KIND"
        if self.has_full_house():
            return "FULL_HOUSE"
        if self.has_flush():
            return "FLUSH"
        if self.has_straight():
            return "STRAIGHT"
        if self.has_three_of_a_kind():
            return "THREE_OF_A_KIND"
        if self.has_two_pair():
            return "TWO_PAIRS"
        if self.has_one_pair():
            return "ONE_PAIR"
        return "HIGH_CARD"

    def has_royal_flush(self):
        return self.has_straight_flush() and self.high_card() == "A"

    def has_straight_flush(self) -> bool:
        return self.has_flush() and self.has_straight()

    def has_four_of_a_kind(self) -> bool:
        return self._has_x_of_a_kind_or_more(4)

    def has_full_house(self) -> bool:
        return self._has_x_of_a_kind(3) and self._has_x_of_a_kind(2)

    def has_flush(self):
        return self.cards[0].suit == self.cards[1].suit and \
               self.cards[1].suit == self.cards[2].suit and \
               self.cards[2].suit == self.cards[3].suit and \
               self.cards[3].suit == self.cards[4].suit

    def has_straight(self) -> bool:
        return self.cards[0].strength == self.cards[1].strength + 1 and \
               self.cards[1].strength == self.cards[2].strength + 1 and \
               self.cards[2].strength == self.cards[3].strength + 1 and \
               self.cards[3].strength == self.cards[4].strength + 1

    def has_three_of_a_kind(self) -> bool:
        return self._has_x_of_a_kind_or_more(3)

    def has_two_pair(self) -> bool:
        sizes = [card.size for card in self.cards]
        pairs = 0
        for size in strengths:
            if sizes.count(size) >= 2:
                pairs += 1
                if pairs == 2:
                    return True
        return False

    def has_one_pair(self) -> bool:
        return self._has_x_of_a_kind_or_more(2)

    def high_card(self) -> str:
        if self._has_card_of_size("A"):
            return "A"
        if self._has_card_of_size("K"):
            return "K"
        if self._has_card_of_size("Q"):
            return "Q"
        if self._has_card_of_size("J"):
            return "J"
        if self._has_card_of_size("T"):
            return "T"
        if self._has_card_of_size("9"):
            return "9"
        if self._has_card_of_size("8"):
            return "8"
        if self._has_card_of_size("7"):
            return "7"
        if self._has_card_of_size("6"):
            return "6"
        if self._has_card_of_size("5"):
            return "5"
        if self._has_card_of_size("4"):
            return "4"
        if self._has_card_of_size("3"):
            return "3"
        if self._has_card_of_size("2"):
            return "2"

    def get_pairs(self) -> List[int]:
        sizes = [card.size for card in self.cards]
        pairs = []
        for size in strengths:
            if sizes.count(size) >= 2:
                pairs.append(size)
        pairs.reverse()
        return pairs

    def _has_card_of_size(self, size: str):
        for card in self.cards:
            if card.size == size:
                return True
        return False

    def _has_x_of_a_kind_or_more(self, x) -> bool:
        sizes = [card.size for card in self.cards]
        for size in sizes:
            if sizes.count(size) >= x:
                return True
        return False

    def _has_x_of_a_kind(self, x) -> bool:
        sizes = [card.size for card in self.cards]
        for size in sizes:
            if sizes.count(size) == x:
                return True
        return False


class Poker:
    # return 1 if hand_1 wins, 0 otherwise
    @staticmethod
    def compare_hands(hand_1: Hand, hand_2: Hand) -> int:
        if hand_1.get_hand_strength() > hand_2.get_hand_strength():
            return 1
        if hand_2.get_hand_strength() > hand_1.get_hand_strength():
            return 0
        return Poker.compare_equal_hands(hand_1, hand_2)

    @staticmethod
    def compare_equal_hands(hand_1: Hand, hand_2: Hand) -> int:
        if hand_1.has_royal_flush():
            return 0
        if hand_1.has_straight_flush():
            return Poker.compare_high_cards(hand_1.cards, hand_2.cards)
        if hand_1.has_four_of_a_kind():
            return Poker.compare_middle_card(hand_1, hand_2)
        if hand_1.has_full_house():
            return Poker.compare_middle_card(hand_1, hand_2)
        if hand_1.has_flush():
            return Poker.compare_high_cards(hand_1.cards, hand_2.cards)
        if hand_1.has_straight():
            return Poker.compare_high_cards(hand_1.cards, hand_2.cards)
        if hand_1.has_three_of_a_kind():
            return Poker.compare_middle_card(hand_1, hand_2)
        if hand_1.has_two_pair():
            return Poker.compare_two_pairs(hand_1, hand_2)
        if hand_1.has_one_pair():
            return Poker.compare_one_pairs(hand_1, hand_2)
        return Poker.compare_high_cards(hand_1.cards, hand_2.cards)

    @staticmethod
    def compare_two_pairs(hand_1: Hand, hand_2: Hand) -> int:
        pairs_1 = hand_1.get_pairs()
        pairs_2 = hand_2.get_pairs()
        assert len(pairs_1) == 2
        assert len(pairs_2) == 2
        if strengths.index(pairs_1[0]) > strengths.index(pairs_2[0]):
            return 1
        if strengths.index(pairs_1[0]) < strengths.index(pairs_2[0]):
            return 0
        if strengths.index(pairs_1[1]) > strengths.index(pairs_2[1]):
            return 1
        if strengths.index(pairs_1[1]) < strengths.index(pairs_2[1]):
            return 0
        return Poker.compare_high_cards(hand_1.cards, hand_2.cards)

    @staticmethod
    def compare_one_pairs(hand_1: Hand, hand_2: Hand) -> int:
        pairs_1 = hand_1.get_pairs()
        pairs_2 = hand_2.get_pairs()
        assert len(pairs_1) == 1
        assert len(pairs_2) == 1
        if strengths.index(pairs_1[0]) > strengths.index(pairs_2[0]):
            return 1
        if strengths.index(pairs_1[0]) < strengths.index(pairs_2[0]):
            return 0
        return Poker.compare_high_cards(hand_1.cards, hand_2.cards)

    @staticmethod
    def compare_middle_card(hand_1: Hand, hand_2: Hand) -> int:
        if hand_1.cards[2].strength > hand_2.cards[2].strength:
            return 1
        return 0

    @staticmethod
    def compare_high_cards(cards_1: List[Card], cards_2: List[Card]) -> int:
        if len(cards_1) == 0:
            return 0
        if cards_1[0].strength > cards_2[0].strength:
            return 1
        if cards_1[0].strength < cards_2[0].strength:
            return 0
        return Poker.compare_high_cards(cards_1[1:], cards_2[1:])


class Test(unittest.TestCase):
    def test_hand_sorting_and_straight_flush(self):
        cards = [Card("2D"), Card("3D"), Card("5D"), Card("4D"), Card("6D")]
        hand = Hand(cards)
        assert hand.cards[0].size == "6" and hand.cards[0].strength == 4
        assert hand.cards[1].size == "5" and hand.cards[1].strength == 3
        assert hand.cards[2].size == "4" and hand.cards[2].strength == 2
        assert hand.cards[3].size == "3" and hand.cards[3].strength == 1
        assert hand.cards[4].size == "2" and hand.cards[4].strength == 0
        assert hand.has_straight_flush()
        assert hand.has_flush()
        assert hand.has_straight()
        assert not hand.has_royal_flush()

    def test_has_four_of_a_kind(self):
        cards = [Card("2D"), Card("6C"), Card("6S"), Card("6H"), Card("6D")]
        hand = Hand(cards)
        assert hand.has_four_of_a_kind()
        hand.cards[1] = Card("QC")
        assert not hand.has_four_of_a_kind()

    def test_has_full_house_and_2_pairs(self):
        cards = [Card("KD"), Card("KH"), Card("AS"), Card("AH"), Card("AD")]
        hand = Hand(cards)
        assert hand.has_full_house()
        hand.cards[0] = Card("QH")
        assert not hand.has_full_house()
        assert hand.has_two_pair()

    def test_hand(self):
        assert Hand([Card("KD"), Card("AD"), Card("QD"), Card("JD"), Card("TD")]).get_hand() == "ROYAL_FLUSH"
        assert Hand([Card("KD"), Card("9D"), Card("QD"), Card("JD"), Card("TD")]).get_hand() == "STRAIGHT_FLUSH"
        assert Hand([Card("AH"), Card("AD"), Card("AC"), Card("AS"), Card("TD")]).get_hand() == "FOUR_OF_A_KIND"
        assert Hand([Card("AD"), Card("AH"), Card("AC"), Card("2D"), Card("2H")]).get_hand() == "FULL_HOUSE"
        assert Hand([Card("5D"), Card("2D"), Card("QD"), Card("JD"), Card("TD")]).get_hand() == "FLUSH"
        assert Hand([Card("KD"), Card("AD"), Card("QS"), Card("JC"), Card("TH")]).get_hand() == "STRAIGHT"
        assert Hand([Card("2S"), Card("AD"), Card("TH"), Card("TC"), Card("TD")]).get_hand() == "THREE_OF_A_KIND"
        assert Hand([Card("KD"), Card("QS"), Card("QD"), Card("TC"), Card("TD")]).get_hand() == "TWO_PAIRS"
        assert Hand([Card("KD"), Card("KS"), Card("QD"), Card("JD"), Card("TD")]).get_hand() == "ONE_PAIR"
        assert Hand([Card("KD"), Card("AD"), Card("QD"), Card("5C"), Card("TS")]).get_hand() == "HIGH_CARD"

    def test_two_pairs(self):
        hand_1 = Hand([Card("KD"), Card("KS"), Card("QC"), Card("QH"), Card("TD")])
        hand_2 = Hand([Card("KH"), Card("KC"), Card("QD"), Card("QS"), Card("AD")])
        assert Poker.compare_hands(hand_1, hand_2) == 0

    def test_one_pair(self):
        hand_1 = Hand([Card("TH"), Card("8H"), Card("5C"), Card("QS"), Card("TC")])
        hand_2 = Hand([Card("9H"), Card("4D"), Card("JC"), Card("KS"), Card("JS")])
        assert Poker.compare_hands(hand_1, hand_2) == 0



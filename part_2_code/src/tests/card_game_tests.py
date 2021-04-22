import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Ace", 1)
        self.card2 = Card("Hearts", 8)  
        self.card_game = CardGame()

    def test_check_for_ace_returns_True_when_card_is_ace(self):
        actual_value = self.card_game.check_for_ace(self.card1)
        self.assertTrue(actual_value)

    def test_check_for_ace_returns_False_when_card_is_not_ace(self):
        actual_value = self.card_game.check_for_ace(self.card2)
        self.assertFalse(actual_value)

    def test_highest_card(self):
        actual_card = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2.value, actual_card.value)

    def test_cards_total(self):
        expected_total = "You have a total of 9"
        actual_total = self.card_game.cards_total([self.card1, self.card2])
        self.assertEqual(expected_total, actual_total)


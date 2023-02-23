import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spade", 1)
        self.card2 = Card("Diamond", 7)
        self.cards = [self.card1, self.card2]
        self.game = CardGame
    
    def test_check_for_ace__true(self):
        expected = True
        actual = self.game.check_for_ace(self, self.card1)
        self.assertEqual(expected, actual)

    def test_check_for_ace__false(self):
       expected = False
       actual = self.game.check_for_ace(self, self.card2)
       self.assertEqual(expected, actual)

    def test_highest_card(self):
       expected = self.card2
       actual = self.game.highest_card(self, self.card1, self.card2)
       self.assertEqual(expected, actual)

    def test_cards_total(self):
       expected = "You have a total of 8"
       actual = self.game.cards_total(self, self.cards)
       self.assertEqual(expected, actual)
  
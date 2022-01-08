from typing import Union
import unittest

from bowling import Bowling

class BowlingTest(unittest.TestCase):

    def test_bowling(self):
        self.game == Bowling.Bowling()
    
    def test_gutter_game(self):
        self.rollMany(0, 20)
        assert self.game.score() == 0

    def test_all_ones(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20
    
    def test_one_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16
    
    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24
    
    def test_perfect_game(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300
    
    def test_all_spares(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150
    
    def test_roll_many(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)
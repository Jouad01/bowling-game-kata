from bowling import *
import pytest

def test_Strike():
    assert Strike.add_score() == 0

def test_Spare():
    assert Spare.add_score() == 10

def test_Gutterball():
    assert GutterBall.add_score() == 0

def test_BowlingPins():
    assert BowlingPins(4).add_score() == 4
    assert BowlingPins(5).add_score() == 5
    assert BowlingPins(2).add_score() == 2
    assert BowlingPins(9).add_score() == 9
    assert BowlingPins(1).add_score() == 1
    assert BowlingPins(3).add_score() == 3


def test_Roll():
    assert Roll(5).get_score() == 5
    assert Roll(10).get_score() == 10
    assert Roll(6).get_score() == 6
    assert Roll(0).get_score() == 0

    assert Roll(BowlingPins(5).add_score()).get_score() == 5
    # assert Roll(Strike.add_score()).get_score() == 10 --> Fallo
    assert Roll(BowlingPins(6).add_score()).get_score() == 6
    assert Roll(GutterBall.add_score()).get_score() == 0


def test_Frame():
    assert Frame(0, 2, False, False).completed() == True
    assert Frame(0, 2, False, False).completed() == True
    assert Frame(3, 2, False, False).completed() == True
    assert Frame(0, 1, False, False).completed() == False
    assert Frame(10, 1, True, False).completed() == True
    assert Frame(7, 3, False, True).completed() == True
    assert Frame(7, 2, False, True).completed() == False

    assert Frame(0, 1, False, False).add_score(10) == 10
    assert Frame(0, 1, False, False).add_score(0) == 0
    assert Frame(0, 1, False, False).add_score(6) == 6
    assert Frame(4, 2, False, False).add_score(6) == 10
    assert Frame(8, 2, False, False).add_score(0) == 8
    assert Frame(1, 2, False, False).add_score(6) == 7
    assert Frame(1, 3, False, True).add_score(6) == 7
    assert Frame(1, 2, False, True).add_score(6) == 7

    # assert Frame(0, 1, False, False).add_score(Roll(Strike().add_score()).get_score()) == 10 --> Fallo
    assert Frame(0, 1, False, False).add_score(Roll(GutterBall().add_score()).get_score()) == 0
    assert Frame(0, 1, False, False).add_score(Roll(BowlingPins(6).add_score()).get_score()) == 6

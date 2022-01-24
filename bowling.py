class Game:
        def __init__(self, player, player_score, player_turns):
            self.player = player
            self.player_score = player_score
            self.player_turns = player_turns

class Frame:
    def __init__(self, frame_score, rolls, strike, last_frame):
        self.frame_score = frame_score
        self.rolls = rolls
        self.strike = strike
        self.last_frame = last_frame
    
    def completed(self):
        if self.strike == True or self.rolls == 2 and self.last_frame == False or self.rolls == 3 and self.last_frame == True:
            return True
        return False

    def add_score(self, score):
        self.frame_score += score
        return self.frame_score

class GutterBall:
        @staticmethod
        def add_score():
            return 0

class BowlingPins:
    def __init__(self, pins):
        self.pins = pins
    
    def add_score(self):
        return self.pins

class Roll:
    def __init__(self, roll_score):
        self.roll_score = roll_score
    
    def get_score(self):
        return self.roll_score

class Spare:
    @staticmethod
    def add_score():
        return 10

class Strike:
    @staticmethod
    def add_score():
        return 0












''' def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
'''
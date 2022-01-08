class Bowling:
    
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        resultado = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.strike(rollIndex):
                resultado += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.spare(rollIndex):
                resultado += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                resultado += self.frameScore(rollIndex)
                rollIndex += 2
        return resultado
    
    def strike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    
    def spare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10
    
    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]
    
    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]
    
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
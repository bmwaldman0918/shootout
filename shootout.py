import random


class Shootout:
    def __init__(self, score_prob: int, initial_shots: int):
        assert(0 < score_prob < 100)
        self.score_prob = score_prob
        self.initial_shots = initial_shots
        self.team1_score, self.team2_score, self.length = 0, 0, 0

    def shoot(self, x: int):
        prob = random.randrange(100)
        if prob < self.score_prob:
            return x + 1
        else:
            return x

    def shot_pair(self):
        self.team1_score = self.shoot(self.team1_score)
        self.team2_score = self.shoot(self.team2_score)
        self.length = self.length + 1

    def insurmountable_lead(self, rounds_remaining: int):
        return abs(self.team1_score - self.team2_score) > rounds_remaining

    def run(self):
        for i in range(self.initial_shots):
            self.shot_pair()
            if self.insurmountable_lead(self.initial_shots - self.length):
                return
        while self.team1_score == self.team2_score:
            self.shot_pair()

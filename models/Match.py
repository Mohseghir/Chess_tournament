import random


class Match:

    def __init__(self, player_1, player_2, score_1=0, score_2=0):
        score_1 = random.choice([0, 0.5, 1])
        if score_1 == 0:
            score_2 = 1
        elif score_1 == 1:
            score_2 = 0
        else:
            score_2 = 0.5
        self.__match = ([player_1, score_1], [player_2, score_2])  # creates a new tuple for each match

    # getter method to get the properties using an object
    def get_match(self):
        return self.__match



"""match = ([Match.player_1, self.score_1], [self.player_2, self.score_2])


def init_match(self):
    match = ([self.player_1, self.score_1], [self.player_2, self.score_2])


class MatchList(Match):
    def __init__(self, player_1, player_2, score_1, score_2):
        super().__init__(player_1, player_2, score_1, score_2)
        match = ([self.player_1, self.score_1], [self.player_2, self.score_2])
"""
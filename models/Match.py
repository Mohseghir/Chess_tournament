class Match:
    """modele pour un match"""

    def __init__(self, player_1, player_2, score_1, score_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    @staticmethod
    def match_serialisation(self):
        return self.__dict__


'''
class MatchList(list):
    def __init__(self):
        super().__init__()
        self.player_1 = None
        match = ([self.player_1, self.score_1], [self.player_2, self.score_2])
'''

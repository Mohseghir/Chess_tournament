import json

matchs = dict()

with open("../data_joueur.json", "r") as f:
    data = json.load(f)

for name in data['players']:
    last_names = name['last_name']
    score = name['score']
    matchs[last_names] = score

print(matchs)


class MatchView:
    @staticmethod
    def add_match():
        player_1 = player_1
        player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

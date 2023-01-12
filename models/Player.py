from tinydb import TinyDB

from views.MatchView import score


class Player:
    """model pour un joueur"""

    def __init__(self, last_name, first_name, birthday,
                 gender, player_id, ranking, score):
        """initialiser un joueur"""
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.player_id = player_id
        self.ranking = ranking
        self.score = score

        self.player_data = TinyDB('players_data.json')

    def __str__(self):
        """format lisible de la class"""
        return f"{self.last_name} {self.first_name} Id : {self.player_id}"

    def player_serialisation(self):
        return self.__dict__

    def save_player(self):

        player = Player(last_name=self.last_name,
                        first_name=self.first_name,
                        birthday=self.birthday,
                        gender=self.gender,
                        player_id=self.player_id,
                        ranking=int(self.ranking),
                        score=int(self.score)
                        )
        player_data = self.player_data
        player_data.insert(player.player_serialisation())

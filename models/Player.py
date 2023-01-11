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

    def __str__(self):
        """format lisible de la class"""
        return f"{self.last_name} {self.first_name}"

    def __repr__(self):
        return str(self)

    @staticmethod
    def player_serialisation(self):
        return self.__dict__


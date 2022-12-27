import json


# player model


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
        return f"Nom : {self.last_name}, Prénom :  {self.first_name}"

    def __repr__(self):
        return str(self)

    @staticmethod
    def player_serialisation(self):
        """sérialiser les info d'un joueur avant utilisation avec json"""
        self.serialised_player = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "gender": self.gender,
            "player_id": self.player_id,
            "ranking": self.ranking,
            "score": self.score
        }
        return self.serialised_player


class PlayerView:
    @staticmethod
    def add_player():
        """saisis des informations d'un joueur """
        last_name = input("Nom : ")
        first_name = input("Prènom : ")
        birthday = input("Date de naissance sous la forme JJ/MM/AAAA : ")
        gender = input("Genre M / F : ")
        player_id = input("ID du joueur : ")
        ranking = input("Classement : ")
        score = input("Score : ")
        return Player(last_name=last_name, first_name=first_name, birthday=birthday,
                      gender=gender, player_id=player_id, ranking=int(ranking), score=int(score))


player = PlayerView.add_player()

data = player.player_serialisation(player)

with open("data_joueur.json", "w") as write_file:
    json.dump(data, write_file, indent=2)

print(player)

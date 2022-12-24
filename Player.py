# player model
class Player:
    """model pour un joueur"""
    def __init__(self, last_name, first_name, birthday, gender, player_id, ranking: int, score=0):
        """initialiser un joueur"""
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.player_id = player_id
        self.ranking = int(ranking)
        self.score = score

    def __str__(self):
        """representer un joueur"""
        return f"{self.last_name} le {self.first_name}"

    def __repr__(self):
        """Représentation de l'objet"""
        return f"les informations du joueur sont :  {self.last_name}, {self.first_name}"


# player view

class PlayerView:
    @classmethod
    def add_player(self):
        """saisis des informations d'un joueur """
        last_name = input("Nom : ")
        first_name = input("Prènom : ")
        birthday = input("Date de naissance sous la forme JJ/MM/AAAA : ")
        gender = input("Genre M / F : ")
        ranking = input("Classement : ")
        score = input("Score : ")
        return Player(last_name=last_name, first_name=first_name, birthday=birthday,
                      gender=gender, ranking=ranking, score=score)

# controler


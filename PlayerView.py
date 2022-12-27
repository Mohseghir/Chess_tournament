from Player import Player


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

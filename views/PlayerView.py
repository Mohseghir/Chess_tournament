from models.Player import Player


class PlayerView:
    @staticmethod
    def add_player():
        """saisis des informations d'un joueur
         ECRIR UNE fct pour afficher la saisi et
         demander confirmation ou reprise de saisir"""
        last_name = input("Nom : ")
        first_name = input("Prènom : ")
        birthday = input("Date de naissance sous la forme JJ/MM/AAAA : ")
        gender = input("Genre M / F : ")
        player_id = input("ID du joueur : ")

        return Player(last_name=last_name, first_name=first_name, birthday=birthday,
                      player_id=player_id)

    @staticmethod
    def num_of_participant():  # nbr par defaut 8
        participant_count = int(input("combien de joueurs voulez-vous ajouter à la base de données ?  : "))
        return participant_count

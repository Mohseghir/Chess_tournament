import datetime
import random

from models.Player import Player
from models.Match import Match
from models.Round import Round
from models.Tournament import Tournament
import json

participants = 2


def create_player():
    global participants
    choix = input("le numbre de joueurs par defaut est de 8, voulez vous le changer ? : n/y")
    if choix == "y":
        participants = int(input("combien de joueurs voulez-vous ajouter à la base de données ?  : "))
    try:
        with open('players.json', 'r') as f:
            players = json.load(f)
    except json.decoder.JSONDecodeError:
        players = {"player": []}

    for i in range(0, participants):
        player = {}
        last_name = input("Nom : ")
        player["last_name"] = last_name
        first_name = input("Prènom : ")
        player["first_name"] = first_name
        birthday = input("Date de naissance sous la forme JJ/MM/AAAA : ")
        player["birthday"] = birthday

        players["player"].append(player)
        print(players)

    with open('players.json', 'w') as f:
        json.dump(players, f)


def create_round_1():
    try:
        with open('players.json', 'r') as f:
            players = json.load(f)
    except json.decoder.JSONDecodeError:
        print("problème au niveau de la lecture du fichier players.json")

    converted_players = [Player(player_data['last_name'],
                                player_data['first_name'],
                                player_data['birthday']
                                ) for player_data in
                         players["player"]]

    # players_tuple = [(player.get_first_name(),
    #                   player.get_last_name(),
    #                   player.get_birthday()
    #                   ) for player in
    #                  converted_players]
    #
    # print(players_tuple)
    #
    # random_players_for_match = random.sample(players_tuple, 2)
    # print(random_players_for_match)

    # premier round, mélange de tous les joueurs de façon aléatoire.
    converted_players = random.sample(converted_players, 8)

    i = 0
    round = Round(1, "Round1", "12/12/1212", "13/12/1212")
    for i in range(i, 4):
        two_random_player_for_match = random.sample(converted_players, 2)
        match = Match(two_random_player_for_match[0],
                      two_random_player_for_match[1])
        round.add_match(match)

        # print(two_random_player_for_match[0],two_random_player_for_match[1])
        print("Taille de la liste = ", len(converted_players))

        print(round.get_match_list()[i].get_match()[0][0],
              "",
              round.get_match_list()[i].get_match()[0][1],
              " -#- ",
              round.get_match_list()[i].get_match()[1][0],
              "",
              round.get_match_list()[i].get_match()[1][1])

        converted_players = [i for i in converted_players if i not in two_random_player_for_match]

    try:
        with open('rounds.json', 'r') as f:
            rounds = json.load(f)
    except json.decoder.JSONDecodeError:
        rounds = {"round": []}

    tour = {"round_num": round.get_round_num(), "name": round.get_name(),
            "start_date_time": round.get_start_date_time(), "end_date_time": round.get_end_date_time()}

    matchs = {"match": []}
    # le i = 0
    for i in range(0, 4):
        match = {}
        player_1 = {"last_name": round.get_match_list()[i].get_match()[0][0].get_last_name(),
                    "first_name": round.get_match_list()[i].get_match()[0][0].get_first_name(),
                    "birthday": round.get_match_list()[i].get_match()[0][0].get_birthday()}
        match["player_1"] = player_1
        player_2 = {"last_name": round.get_match_list()[i].get_match()[1][0].get_last_name(),
                    "first_name": round.get_match_list()[i].get_match()[1][0].get_first_name(),
                    "birthday": round.get_match_list()[i].get_match()[1][0].get_birthday()}
        match["player_2"] = player_2
        match["score_1"] = round.get_match_list()[i].get_match()[0][1]
        match["score_2"] = round.get_match_list()[i].get_match()[1][1]
        matchs["match"].append(match)

    tour["matchs"] = matchs
    rounds["round"].append(tour)
    print(rounds)

    with open('rounds.json', 'w') as f:
        json.dump(rounds, f)

    return round


# =======================================================================

def create_round_2(round):
    i = 0
    list_joueurs = []

    for i in range(i, 4):
        joueur_score_1 = [round.get_match_list()[i].get_match()[0][0].get_last_name(), round.get_match_list()[i].get_match()[0][1]]
        joueur_score_2 = [round.get_match_list()[i].get_match()[1][0].get_last_name(), round.get_match_list()[i].get_match()[1][1]]
        list_joueurs.append(joueur_score_1)
        list_joueurs.append(joueur_score_2)

    print(list_joueurs)
    sorted_players = sorted(list_joueurs, key=lambda x: x[1], reverse=True)
    print(sorted_players)

    # list_joueurs_tri


def create_tournament():
    i = 0
    tournament = Tournament("First_tournament", "Alger", "12/12/2023", "12/12/2023", "Round_1",
                            ["jack", "patric", "sami", "vincent", "MOMO", "fred", "gautier", "stef"], "RAS")
    for i in range(i, 4):
        round = create_round_1()
        tournament.add_round(round)
    print(tournament.get_regestred_players())
    return tournament


if __name__ == "__main__":
    # running controller function
    """create_tournament()"""
    """create_player()"""
    # create_player()
    round = create_round_1()
    create_round_2(round)

"""from views.PlayerView import PlayerView
from tinydb import TinyDB

db = TinyDB('data.json')
players_table = db.table('players')

participant_count = PlayerView.num_of_participant()
players_list = []
for i in range(0, participant_count):
    player = PlayerView.add_player()
    data = player.player_serialisation(player)
    players_list.append(data)
    print(f" {player} a été ajouté en tant que joueur numéro {i + 1} ! ")

for player in players_list:
    players_table.insert(player)
    print(player)




with open("../player.json", "w") as write_file:
   json.dump({"players": players_list}, write_file, indent=2)"""

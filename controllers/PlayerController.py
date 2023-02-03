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


def create_tour():
    global player
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

    # premier tour, mélange de tous les joueurs de façon aléatoire.
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
    return round


def create_tournament():
    i = 0
    tournament = Tournament("First_tournament", "Alger", "12/12/2023", "12/12/2023", "Round_1",
                            ["jack", "patric", "sami", "vincent", "MOMO", "fred", "gautier", "stef"], "RAS")
    for i in range(i, 4):
        round = create_tour()
        tournament.add_round(round)
    print(tournament.get_regestred_players())
    return tournament


if __name__ == "__main__":
    # running controller function
    """create_tournament()"""
    """create_player()"""
    # create_player()
    create_tour()

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

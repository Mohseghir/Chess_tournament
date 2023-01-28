import datetime
import random

from models.Player import Player
from models.Match import Match
from models.Round import Round
from models.Tournament import Tournament
import json

participants = 8


def create_player():
    global participants
    choix = input("le numbre de joueurs par defaut est de 8, voulez vous le changer ? : n/y")
    if choix == "y":
        participants = int(input("combien de joueurs voulez-vous ajouter à la base de données ?  : "))
    try:
        with open('players.json', 'r') as f:
            players = json.load(f)
    except json.decoder.JSONDecodeError:
        players = {}

    for i in range(0, participants):
        player = {}
        last_name = input("Nom : ")
        player["last_name"] = last_name
        first_name = input("Prènom : ")
        player["first_name"] = first_name
        birthday = input("Date de naissance sous la forme JJ/MM/AAAA : ")
        player["birthday"] = birthday
        players[i+len(players)-1] = player
        print(players)

    with open('players.json', 'w') as f:
        json.dump(players, f)

    """player1 = Player("DUBOIT", "Patric", "23/10/1988")
    player2 = Player("BAGHAOUI", "Mohamed", "29/10/1989")
    player3 = Player("BEKKA", "SABI", "12/01/1992")
    player4 = Player("SAMI", "MIKA", "04/12/1989")
    player5 = Player("FANNY", "Steph", "17/12/1980")
    player6 = Player("LECLERC", "Marck", "12/03/1960")
    player7 = Player("FIFI", "max", "12/12/2000")
    player8 = Player("MARTIN", "Seb", "01/12/2001")
    # print(player8)
    return player8, player7"""


def create_match():
    players = create_player()
    match = Match(players[0], players[1], "0", "0")
    # match = Match(random.shuffle(players[0]), random.shuffle(players[1]), "0", "0")
    # print(match.get_match()[0][0], match.get_match()[1][0])
    # print(players[0])
    return match


def create_tour():
    with open('players.json', 'r') as f:
        players = json.load(f)
        print(players)

    # for i in range(0, 9):
    rand = random.randint(0, len(players) - 1)
    # print(players[rand])

    i = 0
    round = Round("1", "Round1", "12/12/1212", "13/12/1212")
    for i in range(i, 4):
        match = create_match()
        round.add_match(match)
    # print(round.get_match_list()[0].get_match()[0][0])
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
    create_player()
    # create_tour()

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

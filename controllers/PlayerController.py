import datetime
import random

# Import the classes from the models module

from models.Player import Player
from models.Match import Match
from models.Round import Round
from models.Tournament import Tournament
import json

participants = 8


# This function is used to create players and store them in a JSON file

def create_player():
    global participants
    # Allow user to change the default number of players (8)

    choix = input("le numbre de joueurs par defaut est de 8, voulez vous le changer ? : n/y")
    if choix == "y":
        participants = int(input("combien de joueurs voulez-vous ajouter à la base de données ?  : "))
    # Try to load existing players from the players.json file

    try:
        with open('players.json', 'r') as f:
            players = json.load(f)
    except json.decoder.JSONDecodeError:
        # If the file is empty or not found, create an empty list
        players = {"player": []}
    # Prompt user to enter information for each player and append the player to the list of players

    for i in range(0, participants):
        player = {}
        last_name = input("Nom : ")
        player["last_name"] = last_name
        first_name = input("Prènom : ")
        player["first_name"] = first_name
        birthday = input("Date de naissance sous la forme JJ/MM/AAAA : ")
        player["birthday"] = birthday
        id = input("id du joueur : ")
        player["id"] = id

        players["player"].append(player)
        print(players)
    # Save the updated list of players to the players.json file

    with open('players.json', 'w') as f:
        json.dump(players, f, indent=2)


# This function is used to create the first round of matches

def create_round_1():
    try:
        # Try to load players from the players.json file

        with open('players.json', 'r') as f:
            players = json.load(f)
    except json.decoder.JSONDecodeError:
        # If the file is empty or not found, print an error message and return
        print("problème au niveau de la lecture du fichier players.json")

    # Convert player data into Player objects and randomly select 8 players for the first round

    converted_players = [Player(player_data['last_name'],
                                player_data['first_name'],
                                player_data['birthday']
                                ) for player_data in
                         players["player"]]

    # premier round, mélange de tous les joueurs de façon aléatoire.
    converted_players = random.sample(converted_players, 8)

    i = 0
    # Create a Round object with the round number, name, start date, and end date

    round = Round(1, "Round1", "12/12/1212", "13/12/1212")
    for i in range(i, 4):
        # Select two random players from the list of converted players and create a Match object with them

        two_random_player_for_match = random.sample(converted_players, 2)
        match = Match(two_random_player_for_match[0],
                      two_random_player_for_match[1])
        # Add the Match object to the Round object

        round.add_match(match)

        # Print the match and remove the two players from the list of converted players

        print("Taille de la liste = ", len(converted_players))

        print(round.get_match_list()[i].get_match()[0][0],
              "",
              round.get_match_list()[i].get_match()[0][1],
              " -#- ",
              round.get_match_list()[i].get_match()[1][0],
              "",
              round.get_match_list()[i].get_match()[1][1])
# il faut expliquer la ligne si dessous __________________________________________________________
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
        score_1_R1 = round.get_match_list()[i].get_match()[0][1]
        match["score_2"] = round.get_match_list()[i].get_match()[1][1]
        score_2_R1 = round.get_match_list()[i].get_match()[1][1]
        matchs["match"].append(match)

    tour["matchs"] = matchs
    rounds["round"].append(tour)
    print(rounds)

    with open('rounds.json', 'w') as f:
        json.dump(rounds, f, indent=2)

    return round


# =======================================================================

def create_round_2(round):
    i = 0
    list_joueurs = []

    for i in range(i, 4):
        joueur_score_1 = [round.get_match_list()[i].get_match()[0][0].get_last_name(),
                          round.get_match_list()[i].get_match()[0][1]]
        joueur_score_2 = [round.get_match_list()[i].get_match()[1][0].get_last_name(),
                          round.get_match_list()[i].get_match()[1][1]]
        list_joueurs.append(joueur_score_1)
        list_joueurs.append(joueur_score_2)

    print(list_joueurs)
    sorted_players = sorted(list_joueurs, key=lambda x: x[1], reverse=True)
    print(sorted_players)

    round = Round(2, "Round2", "14/12/1212", "15/12/1212")
    for i in range(0, len(sorted_players), 2):
        print("{} vs. {}".format(sorted_players[i], sorted_players[i + 1]))
        verify = has_played(sorted_players[i], sorted_players[i + 1], round)
        print(verify)
        if not has_played(sorted_players[i], sorted_players[i + 1], round):
            match = Match(sorted_players[i], sorted_players[i + 1])
            round.add_match(match)
        else:
            match = Match(sorted_players[i], sorted_players[i + 2])
            round.add_match(match)

    for i in range(0, 4):
        print(round.get_match_list()[i].get_match()[0][0],
              "",
              round.get_match_list()[i].get_match()[0][1],
              " -#- ",
              round.get_match_list()[i].get_match()[1][0],
              "",
              round.get_match_list()[i].get_match()[1][1])

    try:
        with open('rounds.json', 'r') as f:
            rounds = json.load(f)
    except json.decoder.JSONDecodeError:
        rounds = {"round": []}

    tour = {"round_num": round.get_round_num(), "name": round.get_name(),
            "start_date_time": round.get_start_date_time(), "end_date_time": round.get_end_date_time()}
    # extract the scores from round 1
    round1_scores = [match['score_1'] + match['score_2'] for match in rounds['round'][0]['matchs']['match']]

    matchs = {"match": []}
    # le i = 0
    for i in range(0, 4):
        match = {}
        player_1 = {"last_name": round.get_match_list()[i].get_match()[0][0],
                    "first_name": round.get_match_list()[i].get_match()[0][0],
                    "birthday": round.get_match_list()[i].get_match()[0][0]}
        match["player_1"] = player_1
        player_2 = {"last_name": round.get_match_list()[i].get_match()[1][0],
                    "first_name": round.get_match_list()[i].get_match()[1][0],
                    "birthday": round.get_match_list()[i].get_match()[1][0]}
        match["player_2"] = player_2
        match["score_1"] = round.get_match_list()[i].get_match()[0][1] + round1_scores[i]
        match["score_2"] = round.get_match_list()[i].get_match()[1][1] + round1_scores[i]
        matchs["match"].append(match)

    tour["matchs"] = matchs
    rounds["round"].append(tour)
    print(rounds)

    with open('rounds.json', 'w') as f:
        json.dump(rounds, f, indent=2)


def has_played(player_1, player_2, round):
    for match in round.get_match_list():
        if (player_1 in match.get_match()[0] or player_1 in match.get_match()[1]
        ) and (player_2 in match.get_match()[0] or player_2 in match.get_match()[1]):
            # print("True")
            return True
    # print("False")
    return False


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
    create_player()
    # create_player()
    # round = create_round_1()
    # create_round_2(round)

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

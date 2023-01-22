from models.Player import Player
from models.Match import Match
from models.Round import Round


def create_player():
    player1 = Player("jack", "toto", "12/12/2012")
    player2 = Player("patric", "toto", "12/12/2012")
    player3 = Player("sami", "toto", "12/12/2012")
    player4 = Player("vincent", "toto", "12/12/2012")
    player5 = Player("MOMO", "toto", "12/12/2012")
    player6 = Player("fred", "toto", "12/12/2012")
    player7 = Player("gautier", "toto", "12/12/2012")
    player8 = Player("stef", "toto", "12/12/2012")
    # print(player8)
    return player8, player7


def create_match():
    players = create_player()
    match = Match(players[0], players[1], "0", "0")
    # print(match.get_match()[0][0], match.get_match()[1][0])
    # print(players[0])
    return match


def create_tour():
    i = 0
    round = Round("1", "Round1", "12/12/1212", "13/12/1212")
    for i in range(i, 4):
        match = create_match()
        round.add_match(match)
    print(round.get_match_list()[0].get_match()[0][0])


if __name__ == "__main__":
    # running controller function
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

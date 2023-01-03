import json
from views.TournamentView import *
from views.PlayerView import *

players_list = []

participant_count = PlayerView.num_of_participant()

for i in range(0, participant_count):
    player = PlayerView.add_player()
    data = player.player_serialisation(player)
    players_list.append(data)
    print(f" {player} a été ajouté en tant que joueur numéro {i + 1} ! ")

with open("../data_joueur.json", "w") as write_file:
    json.dump({"players": players_list}, write_file, indent=2)

tournament_list = []

tournament = TournamentView.add_tournament()
data_tournament = tournament.tournament_serialisation(tournament)
tournament_list.append(data_tournament)
print(f"{tournament} a été ajouté, les match peuvent commencer")

with open("../data_tournament.json", "w") as write_file:
    json.dump({"tournaments": tournament_list}, write_file, indent=2)


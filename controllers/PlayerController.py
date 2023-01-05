import json
from views.PlayerView import *

participant_count = PlayerView.num_of_participant()

players_list = []
for i in range(0, participant_count):
    player = PlayerView.add_player()
    data = player.player_serialisation(player)
    players_list.append(data)
    print(f" {player} a été ajouté en tant que joueur numéro {i + 1} ! ")

with open("../data_joueur.json", "w") as write_file:
    json.dump({"players": players_list}, write_file, indent=2)
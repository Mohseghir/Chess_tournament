import json
from PlayerView import *

player = PlayerView.add_player()

data = player.player_serialisation(player)

with open("data_joueur.json", "w") as write_file:
    json.dump(data, write_file, indent=2)

print(player)

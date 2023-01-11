import json
from views.TournamentView import *
from controllers.PlayerController import *
from tinydb import TinyDB, Query, where
tournament_list = []

tournament = TournamentView.add_tournament()
data_tournament = tournament.tournament_serialisation(tournament)
tournament_list.append(data_tournament)
print(f"{tournament.name} a été ajouté, les match peuvent commencer")

with open("../data_tournament.json", "w") as write_file:
    json.dump({"tournaments": tournament_list}, write_file, indent=2)

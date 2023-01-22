from models.Tournament import *
from views.TournamentView import TournamentView
from tinydb import TinyDB

db = TinyDB('data.json')
tournaments_table = db.table('tournaments')

tournament_list = []

tournament = TournamentView.add_tournament()
tournament.create_rounds_list('participants_ids')
#tournament.play_tournament()

"""for round in tournament.rounds:
    print(f'Round {round.round_num} - {round.name}')
    for match in round.matches:
        print(f'{match.player1.name} vs {match.player2.name}')
"""
data_tournament = tournament.tournament_serialisation(tournament)
tournament_list.append(data_tournament)
print(f"{tournament.name} a été ajouté, les match peuvent commencer")

for tournament in tournament_list:
    tournaments_table.insert(tournament)
    print(tournament)




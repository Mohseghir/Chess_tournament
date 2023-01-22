from tinydb import TinyDB, Query, where
from pprint import pprint
"""
# cration de la base de données
db = TinyDB('db.json')

# creation de la table (clé) fruits
fruits = db.table('fruits')
fruits.truncate()
# insertion des données dans la table fruits (le données doit étre sous formation json)
# sérialisées
fruits.insert({'type': 'fraise', 'quantite': 4})
fruits.insert({'type': 'orange', 'quantite': 1})
fruits.insert({'type': 'banane', 'quantite': 7})
# récuperation de la liste des fruit dans la table fruit
# les données sont sous format de liste de dictionnaire ou de liste de json
list_fruits = fruits.all() # fruits = la table fruits , .all() = récuperation de tout les données
print(list_fruits)

# mettre à jour une valeure
fruits.update({'quantite': 8}, where('type') == 'fraise')


# récuperer les fruits avec le type fraise
fraise = fruits.search(where('type') == 'fraise')
print(fraise)


players = db.table('players')
players.truncate()
players.insert({'name': 'X', 'age': 20})
players.insert({'name': 'Y', 'age': 30})

"""
class ChessTournament:
    def __init__(self, db_file):
        # Create an instance of TinyDB using the specified file
        self.db = TinyDB(db_file)

    def create_tournament(self):
        # Ask the user to enter the tournament name
        name = input("Enter tournament name: ")
        # Ask the user to enter a comma-separated list of participant IDs
        participant_ids = input("Enter comma-separated list of participant IDs: ")
        # Convert the entered participant IDs into a list of integers
        participant_ids = [int(x) for x in participant_ids.split(",")]
        # Get the participants list from the Players table
        participants = self.get_participants(participant_ids)
        # Insert the tournament name and the list of participants into the Tournaments table
        self.db.table('tournaments').insert({'name': name, 'participants': participants})

    def get_participants(self, participant_ids):
        # Search for players with the specified IDs in the "Players" table
        participants = self.db.table('players').search(where('player_id').one_of(participant_ids))
        # Extract the participant information from the returned player data
        participant_list = [{'name': p['name'], 'player_id': p['player_id'], 'score': p['score']} for p in participants]
        return participant_list


# Create an instance of the ChessTournament class
tournament = ChessTournament('data.json')
# Call the create_tournament method to create a new tournament
tournament.create_tournament()





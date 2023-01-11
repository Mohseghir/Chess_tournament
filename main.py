from tinydb import TinyDB, Query, where
from pprint import pprint

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





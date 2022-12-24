class Tournament:

    def __init__(self, name, place, start_end_dates, current_round, players_list,
                 time_controller, description, rounds_number=4):
        self.name = name
        self.place = place
        self.start_end_dates = start_end_dates
        self.rounds_number = rounds_number
        self.current_round = current_round
        self.rounds = []
        self.players_list = players_list
        self.time_controller = time_controller
        self.description = description



#tournament View
@staticmethod
def add_tournament():
    name = input("Nom du tournois : ")
    place = input("Ce tournois se déroule à : ")
    date = input("Date de début du tournois : ")
    rounds_number = input("Nombre de tours : ")
    rounds = []
    players = players
    time_controler = time_controler
    description = description
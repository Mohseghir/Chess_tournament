class Tournament:

    def __init__(self, name, place, date, rounds_number, players, time_controler, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = rounds_number
        self.rounds = []
        self.players = players
        self.time_controler = time_controler
        self.description = description



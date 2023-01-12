from tinydb import TinyDB


class Tournament:

    def __init__(self, name, place, start_date, end_date, number_of_rounds, current_round_number, players,
                 rounds_list, time_controller, description):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round_number = current_round_number
        self.players = players
        self.rounds_list = rounds_list
        self.time_controller = time_controller
        self.description = description

        self.tournament_data = TinyDB('tournament_data.json')

    def __str__(self):
        """format lisible de la class"""
        return f"Le tournois {self.name} à {self.place}"

    def tournament_serialisation(self):
        return self.__dict__

    def save_tournament(self):

        tournament = Tournament(name=self.name,
                                place=self.place,
                                start_date=self.start_date,
                                end_date=self.end_date,
                                number_of_rounds=self.number_of_rounds,
                                current_round_number=self.current_round_number,
                                players=self.players,
                                rounds_list=self.rounds_list,
                                time_controller=self.time_controller,
                                description=self.description
                                )
        tournament_data = self.tournament_data
        tournament_data.insert(tournament.tournament_serialisation())



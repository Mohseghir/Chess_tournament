from controller import players_list


class Tournament:

    def __init__(self, name, place, start_date, end_date, rounds_number, current_round_number,
                 rounds_list, time_controller, description):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_number = rounds_number
        self.current_round_number = current_round_number
        self.players_list = players_list
        self.rounds_list = rounds_list
        self.time_controller = time_controller
        self.description = description

    def __str__(self):
        """format lisible de la class"""
        return f"Le tournois {self.name} à {self.first_name}"

    def __repr__(self):
        return str(self)


# tournament View
@staticmethod
def add_tournament():
    name = input("Nom du tournois : ")
    place = input("Ce tournois se déroule à : ")
    start_date = input("Date de début : ")
    end_date = input("Date de fin : ")
    rounds_number = input("Nombre de tours (4 par défaut) : ")
    current_round_number = input("tour en cours : ")
    players = players_list
    rounds_list = rounds_list
    time_controller =  input(" choisiser votre contolle du temps : un bullet, un blitz ou un coup rapide ?"
    description = input(" saisisser vos remarques : ")


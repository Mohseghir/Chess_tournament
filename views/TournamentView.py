from models.Tournament import *
from controllers.PlayerController import *


# tournament View

class TournamentView:
    @staticmethod
    def add_tournament():
        name = input("Nom du tournois : ")
        place = input("Ce tournois se déroule à : ")
        start_date = input("Date de début : ")
        end_date = input("Date de fin : ")
        number_of_rounds = input("Nombre de tours (4 par défaut) : ")
        current_round_number = []
        players = players_list
        rounds_list = []
        time_controller = input(" choisiser votre contolle du temps : un bullet, un blitz ou un coup rapide ?")
        description = input(" saisisser vos remarques : ")
        return Tournament(name=name, place=place,
                          start_date=start_date,
                          end_date=end_date,
                          number_of_rounds=number_of_rounds,
                          current_round_number=current_round_number,
                          players=players,
                          rounds_list=rounds_list,
                          time_controller=time_controller,
                          description=description)

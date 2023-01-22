from models.Tournament import Tournament
from tinydb import TinyDB, where


NUM_PARTICIPANT = 8
db = TinyDB('data.json')
participants = db.table('players')
participant_list = [{'last_name': p['last_name'], 'player_id': p['player_id']} for p in participants]


class TournamentView:
    @staticmethod
    def add_tournament():
        name = input("Nom du tournois : ")
        place = input("Ce tournois se déroule à : ")
        start_date = input("Date de début : ")
        end_date = input("Date de fin : ")
        number_of_rounds = input("Nombre de tours (4 par défaut) : ")
        current_round = []
        print("veuilez selectionnner des joueurs depuis la base de données suivante : ")
        print(participant_list)
        participants_ids = ["AZ0001", "AZ00002", "AZ00003", "AZ00004", "AZ00005", "AZ00006", "AZ00007", "AZ00008"]
        """participants_ids = []
        for i in range(NUM_PARTICIPANT):
            participant_id = input(f"veuillez saisir l'ID du participant numéro {i + 1} : ")
            participants_ids.append(participant_id)
        print(len(participants_ids))"""
        rounds_list = []
        time_controller = input(" choisiser votre contolle du temps : un bullet, un blitz ou un coup rapide ? : ")
        description = input(" saisisser vos remarques : ")
        return Tournament(name=name, place=place,
                          start_date=start_date,
                          end_date=end_date,
                          current_round=current_round,
                          participants_ids=participants_ids,
                          rounds_list=rounds_list,
                          time_controller=time_controller,
                          description=description)

class Round:

    def __init__(self, name, start_date_time, end_date_time):
        self.name = name # round_1 round_2..etc
        self.start_date_time = start_date_time # doit étre remplis automatiquement des la creation du tour
        self.end_date_time = end_date_time # doit étre remplis automatiquement quand le tour est terminé
        self.matchs_list = [(P1,S1), (P2,S2)]


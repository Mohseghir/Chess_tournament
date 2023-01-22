class Tournament:

    def __init__(self, name, place, start_date, end_date, current_round, regestred_players, director_description):
        self.__name = name
        self.__place = place
        self.__start_date = start_date
        self.__end_date = end_date
        self.__number_of_rounds = 4
        self.__current_round = current_round
        self.__rounds_list = []
        self.__regestred_players = regestred_players
        self.__director_description = director_description

    def add_round(self, round):
        self.__rounds_list.append(round)

    ## getter method to get the properties using an object
    def get_name(self):
        return self.__name

    ## setter method to change the value 'self.__name = name' using an object
    def set_name(self, name):
        self.__name = name

    ## getter method to get the properties using an object
    def get_place(self):
        return self.__place

    ## setter method to change the value 'place' using an object
    def set_place(self, place):
        self.__place = place

    ## getter method to get the properties using an object
    def get_start_date(self):
        return self.__start_date

    ## setter method to change the value 'start date ' using an object
    def set_start_date(self, start_date):
        self.__start_date = start_date

    ## getter method to get the properties using an object
    def get_end_date(self):
        return self.__end_date

    ## setter method to change the value 'end date' using an object
    def set_end_date(self, end_date):
        self.__end_date = end_date

    ## getter method to get the properties using an object
    def get_number_of_rounds(self):
        return self.__number_of_rounds

    ## setter method to change the value 'num of round' using an object
    def set_number_of_rounds(self, number_of_rounds):
        self.__number_of_rounds = number_of_rounds

    ## getter method to get the properties using an object
    def get_current_round(self):
        return self.__current_round

    ## setter method to change the value 'current round' using an object
    def set_current_round(self, current_round):
        self.__current_round = current_round

    ## getter method to get the properties using an object
    def get_rounds_list(self):
        return self.__rounds_list

    ## setter method to change the value 'round list' using an object
    def set_rounds_list(self, rounds_list):
        self.__rounds_list = rounds_list

    ## getter method to get the properties using an object
    def get_regestred_players(self):
        return self.__regestred_players

    ## setter method to change the value 'regesterd player using an object
    def set_regestred_players(self, regestred_players):
        self.__regestred_players = regestred_players

    ## getter method to get the properties using an object
    def get_director_description(self):
        return self.__director_description

    ## setter method to change the value 'director desc' using an object
    def set_director_description(self, director_description):
        self.__director_description = director_description

    def __str__(self):
        """format lisible de la class"""
        return f"Le tournois {self.__name} à {self.__place}"


"""   
    @staticmethod
   def tournament_serialisation(self):
       return self.__dict__


def create_rounds_list(self, participants_ids):
       for round_num in range(1, self.number_of_rounds + 1):
           current_round = Round(round_num, f'Round {round_num}', datetime.now(), datetime.now())
           if round_num == 1:
               # shuffle participant randomly for the first round
               random.shuffle(self.participants_ids)
               for i in range(0, len(self.participants_ids) // 2):
                   player_1 = self.participants_ids[i]
                   player_2 = self.participants_ids[len(self.participants_ids)-i-1]
                   match = MatchList(player_1, player_2, score_1=0, score_2=0)
                   current_round.add_match(match)
               print(current_round)

           else:  # sort the participant base en their score from the Round 1
               sorted_participants = sorted(self.participants_ids, key=lambda x: x.score,
                                            reverse=True)
               for i in range(0, len(sorted_participants) // 2):
                   player_1 = self.participants_ids[i]
                   player_2 = self.participants_ids[len(self.participants_ids) - i - 1]
                   match = MatchList(player_1, player_2, score_1=0, score_2=0)
                   current_round.add_match(match)
                   self.rounds_list.append(current_round)

   def play_tournament(self):
       for round in self.rounds_list:
           for match in round.match_list:
               if match.score_1 > match.score_2:
                   match.player_1.score += 1
               elif match.score_1 < match.score_2:
                   match.player_2.score += 1
               else:
                   match.player_1.score += 0.5
                   match.player_2.score += 0.5
"""

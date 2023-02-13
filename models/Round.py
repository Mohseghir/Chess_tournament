from models.Player import *


class Round:

    def __init__(self, round_num, name, start_date_time, end_date_time):
        self.__round_num = round_num
        self.__name = name  # round_1 round_2 etc
        self.__start_date_time = start_date_time  # doit étre remplis automatiquement des la creation du tour
        self.__end_date_time = end_date_time  # doit étre remplis automatiquement quand le tour est terminé
        self.__match_list = []  # creates a new empty list for each round

    def add_match(self, match):
        self.__match_list.append(match)

    ## getter method to get the properties using an object
    def get_name(self):
        return self.__name

    ## setter method to change the value 'start_date_time' using an object
    def set_round_num(self, round_num):
        self.__round_num = round_num

    ## getter method to get the properties using an object
    def get_round_num(self):
        return self.__round_num

    ## setter method to change the value 'start_date_time' using an object
    def set_name(self, name):
        self.__name = name




    ## getter method to get the properties using an object
    def get_start_date_time(self):
        return self.__start_date_time

    ## setter method to change the value 'start_date_time' using an object
    def set_start_date_time(self, start_date_time):
        self.__start_date_time = start_date_time

    ## getter method to get the properties using an object
    def get_end_date_time(self):
        return self.__end_date_time

    ## setter method to change the value 'end_date_time' using an object
    def set_end_date_time(self, end_date_time):
        self.__end_date_time = end_date_time

    ## getter method to get the properties using an object
    def get_match_list(self):
        return self.__match_list

    ## setter method to change the value 'start_date_time' using an object
    def set_match_list(self, match_list):
        self.__match_list = match_list

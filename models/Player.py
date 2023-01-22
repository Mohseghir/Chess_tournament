class Player:
    """model pour un joueur"""

    def __init__(self, last_name, first_name, birthday):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__birthday = birthday

    def __str__(self):
        """format lisible de la class"""
        return f"{self.__last_name} {self.__first_name}"

    ## getter method to get the properties using an object
    def get_last_name(self):
        return self.__last_name

    ## setter method to change the value '_last_name' using an object
    def set_last_name(self, last_name):
        self.__last_name = last_name

    ## getter method to get the properties using an object
    def get_first_name(self):
        return self.__first_name

    ## setter method to change the value 'first_name' using an object
    def set_first_name(self, first_name):
        self.__first_name = first_name

    ## getter method to get the properties using an object
    def get_birthday(self):
        return self.__birthday

    ## setter method to change the value '_birthday_name' using an object
    def set_birthday(self, birthday):
        self.__birthday = birthday




"""
@staticmethod
def player_serialisation(self):
    return self.__dict__"""

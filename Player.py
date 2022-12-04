class Player:

    def __init__(self, last_name, first_name, birthday, gender, ranking: int, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = int(ranking)
        self.score = score

    def __str__(self):
        return f"{self.last_name},{self.first_name}"

    def __repr__(self):
        return str(self)




class Player:
    def __init__(self, last_name, first_name, birthday, gender, ranking: int, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = int(ranking)
        self.score = score


player = Player()

player.last_name = "Dupont"
player.first_name = "Michel"
player.birthday = "29/10/1989"
player.gender = "homme"
player.ranking = 0

print(player)

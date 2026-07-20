class Player:
    def __init__(self, name, score=0, level=1):
        self.name  = name
        self.score = score
        self.level = level
 
    def increase_score(self, points):
        self.score += points
        print("+", points, "Points! Total Score:", self.score)
 
    def level_up(self):
        self.level += 1
        print("Level Up! Current Level:", self.level)
 
    def show_progress(self):
        print("Player:", self.name)
        print("Score:", self.score)
        print("Level:", self.level)

player = Player("Mihir")
player.show_progress()
player.increase_score(50)
player.level_up()
player.increase_score(100)
player.level_up()
player.show_progress()



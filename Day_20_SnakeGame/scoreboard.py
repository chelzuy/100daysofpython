from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read()) 
        # self.highscore = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)        
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align= ALIGNMENT, font= FONT)

#This method is use to keep track of the high score, added on Day 24 
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score 
            with open("data.txt", mode= "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

#This method is use if the snake hits the wall or its self, originally created on Day 20
    # def game_over(self):
    #     self.goto(0, 0)  
    #     self.write("GAME OVER", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1 
        # self.clear() --> moved to def updated_scoreboard, because game_over is commented out
        self.update_scoreboard()
        
        
        



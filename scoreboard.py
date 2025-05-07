from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('latest_score.txt') as file1:
            self.high_score = int(file1.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Courier', 15, 'normal'))

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score} \t High Score : {self.high_score}', move=False, align='center', font=('Courier', 15, 'normal'))

    def reset_scores(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open('latest_score.txt', mode='w') as file:
            contents = file.write(f'{self.high_score}')

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



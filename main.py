import turtle
import pandas as pd
game_is_on = True

df = pd.read_csv("50_states.csv")
states = df["state"].tolist()

screen = turtle.Screen()
screen.title("U.S States Game")
count = 0
count_1 = 0
guessed_states = []
learn_list = []

screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")


while game_is_on:

    answer = screen.textinput(title=f"{count}/50 States Correct", prompt="Whats another state name: ").title()

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        count += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(df[df.state == answer].x), int(df[df.state == answer].y))
        t.pendown()
        t.write(answer)

    if answer == "Exit":
        game_is_on = False

    if count == 50:
        game_is_on = False

for s in states:
    if s not in guessed_states:
        learn_list.append(s)

with open("highscore.txt","r") as file:
    score = int(file.readline())
    if score < count:
        open("highscore.txt","w").write(f"{count}")

df1 = pd.DataFrame(learn_list)
df1.to_csv("states_to_learn.csv")


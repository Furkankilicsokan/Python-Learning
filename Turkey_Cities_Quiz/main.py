import turtle
import pandas

screen = turtle.Screen()
screen.title("Turkey Cities Quiz")
screen.setup(1000, 600)
screen.bgpic("turkey.gif")
screen.bgcolor("Cyan")

turtle.penup()
turtle.hideturtle()

correct_answer = 0
guessed_cities = []

df = pandas.read_csv("cities.csv")

while correct_answer < len(df):
    answer_city = screen.textinput(title=f"{correct_answer}/81 Guess the City", prompt="What's another city's name?")
    titled_answer_city = answer_city.title()

    if titled_answer_city == "Exit":
        break
    if titled_answer_city in df["city"].values:
        city = df[df["city"] == titled_answer_city]
        x_cor = int(city.x.iloc[0])
        y_cor = int(city.y.iloc[0])

        turtle.goto(x_cor, y_cor)
        turtle.write(titled_answer_city)
        correct_answer += 1
        guessed_cities.append(titled_answer_city)


data = pandas.DataFrame(guessed_cities)
data.to_csv("learned_cities.csv")

screen.exitonclick()

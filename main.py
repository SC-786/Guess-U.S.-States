import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

count = 0
correct_guess = []
while count != 50:
    answer_state = screen.textinput(title=f"{count}/50 the State",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in data.state:
            if state not in correct_guess:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv('missing_states.txt')
        break
    if answer_state in all_states and answer_state not in correct_guess:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[answer_state == data.state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        count += 1
        correct_guess.append(answer_state)

#states to learn.csv


screen.mainloop()

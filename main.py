from turtle import Turtle, Screen
import pandas
from state_manger import State_manger

state_manger = State_manger()
screen = Screen()
tim = Turtle()

screen.title("U.S. state Games")
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)

states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()


correct_guess = []


while len(correct_guess) < 50:
    answer_state = screen.textinput(
        f"{len(correct_guess)}/50 Guess the state", "what is another state ?"
    ).capitalize()

    if answer_state == "Exit":
        remaining_states = [state for state in states_list if state not in correct_guess]
        data = pandas.DataFrame(remaining_states)
        data.to_csv("remaining_csv.csv")
        break

    if answer_state in states_list:
        answer = states[states["state"] == answer_state]
        answer_name = answer["state"].item()
        answer_x = answer["x"].item()
        answer_y = answer["y"].item()
        print(answer_y)
        state_manger.locate_state(answer_name, answer_x, answer_y)
        correct_guess.append(answer_name)
        print(correct_guess)

# states to learn csv

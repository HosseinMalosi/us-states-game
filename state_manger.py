import turtle


class State_manger:

    def __init__(self):
        self.state = turtle.Turtle()
        self.state.hideturtle()
        self.state.penup()
    

    def locate_state(self,state_name,statex , statey):
        self.state.goto(statex , statey)
        self.state.write(state_name)
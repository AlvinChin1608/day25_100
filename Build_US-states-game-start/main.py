import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=750, height=500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # The image is technically turtle
turtle.shape(image) # now just have to load the recently added turtle object

# this is how you get the screen coordinate on your turtle window
# https://stackoverflow.com/questions/42878641/get-mouse-click-coordinates-in-python-turtle

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit" or "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states you missed")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item()) # the item() is to fetch the actual name in the CSV

# Keeping the window open
turtle.mainloop()
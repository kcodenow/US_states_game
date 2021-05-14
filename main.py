import pandas as pd
import turtle

FONT = ('Courier', 10, 'normal')
data = pd.read_csv('50_states.csv', delimiter=',', encoding="utf-8-sig", index_col='state')

screen = turtle.Screen()
screen.title('US States Quiz')

img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

def get_mouse_coor(x, y):
	print(x, y)
turtle.onscreenclick(get_mouse_coor)

guessed_states = []
while len(guessed_states)<50:
	answer_state = screen.textinput(f'{len(guessed_states)}/50 correct', 'Got any more?').title()

	if(answer_state.lower() == 'q'):
		break
	if(answer_state in data.index):
		guessed_states.append(answer_state)
		x=turtle.Turtle()
		x.hideturtle()
		x.penup()
		x.goto(data.loc[answer_state, 'x'], data.loc[answer_state, 'y'])
		x.write(answer_state, align='center', font=FONT)
	else:
		pass

states_to_learn = [state for state in data.index if state not in guessed_states]
learning_csv = pd.DataFrame(states_to_learn).to_csv('states_to_learn')
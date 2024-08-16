# THIS DOES NOT RUN IN PYTHON. THIS IS SIMPLY MY ASSIGNMENT IN REEBORG'S WORLD

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    count = 0
    turn_left()
    while wall_on_right():
        move()
        count += 1
    turn_right()
    move()
    turn_right()
    for i in range(count):
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    elif front_is_clear():
        move()
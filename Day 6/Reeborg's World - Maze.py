def turn_right():
    turn_left()
    turn_left()
    turn_left()

count = 0

while not at_goal():
    if count == 4:
        move()
        count = 0
    if right_is_clear():
        turn_right()
        move()
        count += 1
    elif wall_on_right() and front_is_clear():
        count = 0
        move()
    elif wall_on_right() and wall_in_front():
        count = 0
        turn_left()

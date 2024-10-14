
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if not front_is_clear():
        turn_left()
        hurdle()
    else:
        move()
    



    
    
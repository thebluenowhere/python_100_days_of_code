# Solution in python for all Reeborg maps and problem maps on the site:
# https://reeborg.ca/index_en.html

# Define function to turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Follow right side of map when able
while right_is_clear() and not at_goal():
        turn_right()
        while front_is_clear():
            move()

# Another while loop for the rare positions where you're boxed in          
while not at_goal():
    if front_is_clear():
        move()
    else:
        turn_left()

# This is the main file for MyPong.

from tkinter import *
import table, ball, bat

# initialise global variables
x_velocity = 10
y_velocity = 10

# order a window from the tkinter window factory
window = Tk()
window.title("MyPong")
       
# order a table from the table class
my_table = table.Table(window, net_colour="green", vertical_net=True)

# order a ball from the ball factory
my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=288, y_start=188)

# order a left and right bat from the bat class


#### functions:
def game_flow():
    # detect if ball has hit the bats:
    
    
    my_ball.move_next()
    window.after(50, game_flow)

# bind the controls of the bats to keys on the keyboard


# call the game_flow loop
game_flow()

# start the tkinter loop process
window.mainloop()

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
bat_L = bat.Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, colour="blue")
bat_R = bat.Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, colour="yellow")


#### functions:
def game_flow():
    # detect if ball has hit the bats:
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)
    
    my_ball.move_next()
    window.after(50, game_flow)

# bind the controls of the bats to keys on the keyboard
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

# call the game_flow loop
game_flow()

# start the tkinter loop process
window.mainloop()

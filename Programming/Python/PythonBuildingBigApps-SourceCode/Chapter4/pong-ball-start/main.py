# This is the main file for MyPong.

from tkinter import *
import table   #### <--- do not forget to import ball here ####

# initialise global variables


# order a window from the tkinter window factory
window = Tk()
window.title("MyPong")
       
# order a table from the table class
my_table = table.Table(window, net_colour="green", vertical_net=True)

# order a ball from the ball factory

#### functions:

# call the game_flow loop


# start the tkinter loop process
window.mainloop()

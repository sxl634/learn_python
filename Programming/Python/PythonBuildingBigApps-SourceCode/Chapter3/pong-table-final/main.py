# This is the main file for MyPong.

from tkinter import *
import table

# order a window from the tkinter window factory
window = Tk()
window.title("MyPong")
       
# order a table from the table class
my_table = table.Table(window, net_colour="green", vertical_net=True)

# start the animation loop
window.mainloop()

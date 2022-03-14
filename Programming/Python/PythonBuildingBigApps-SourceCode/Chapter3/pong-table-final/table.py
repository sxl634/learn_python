# This is the Table class originally created for MyPong.
# This class defines a Table that is a 2D rectangle that is a play area.

from tkinter import *

class Table:
    #### constructor
    def __init__(self, window, colour="black", net_colour="green",
                 width=600, height=400, vertical_net=False, horizontal_net=False):
        self.width = width
        self.height = height
        self.colour = colour
        
        # order a canvas to draw on from tkinter's Canvas class:
        self.canvas = Canvas(window, bg=self.colour, height=self.height, width=self.width)
        self.canvas.pack()

        # add a net to the canvas using its create_line method:
        if(vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_colour, dash=(15, 23))
        if(horizontal_net):
            self.canvas.create_line(0, self.height/2, self.width, self.height/2, width=2, fill=net_colour, dash=(15, 23))

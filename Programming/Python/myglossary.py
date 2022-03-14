# myGlossary_Start.py

from tkinter import *

# key press function:

def click():
    entered_text = entry.get() # collect text from text entry box
    output.delete(0.0, END) # clear text box
    definition = my_glossary[entered_text]
    ouput.insert(END, definition)
    
##### main:

window = Tk()
window.title("My Coding Club Glossary")

# create label

Label(window, text="Enter the word you want defining:").grid(row=0, column=0, sticky=W)

# create text entry box

entry=Entry(window, width=20, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# Add a submit button:

Button(window, text="SUBMIT", width=5, command=click).grid(row=2, column=0, sticky=W)

# create another label

Label(window, text="\nDefinition:").grid(row=3, column=0, sticky=W)

# create text box

output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# The dictionary:

my_glossary = {
    'algorithm': 'Step by step instructions to perform a task that a computer could understand.',
    'bug': 'A piece of code that is causing a program to fail to run or at all.',
    'binary number': 'A number represented in base 2.'
    }

##### Run mainloop
window.mainloop()

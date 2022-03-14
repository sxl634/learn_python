# myCalculator.py

from tkinter import *
import calc_functions

# key press function:
def click(key):
    # pressing equals key means calculate:
    if key == "=":
        try:
            result = str(eval(display.get()))[0:10]
            display.insert(END, " = " + result)
        except:
            display.insert(END, " --> Error!")

    # pressing C key means clear screen:           
    elif key == "C":
        display.delete(0, END)

    # now for the constant buttons:
    elif key == constants_list[0]:
        display.insert(END, "3.141592654")
    elif key == constants_list[1]:
        display.insert(END, "300000000")
    elif key == constants_list[2]:
        display.insert(END, "330")
    elif key == constants_list[3]:
        display.insert(END, "149597887.5")

    # now for the function buttons:
    elif key == functions_list[0]:
        n = display.get() # collect display value
        display.delete(0, END) # clear display
        display.insert(END, calc_functions.factorial(n))
    elif key == functions_list[1]:
        n = display.get() # collect display value
        display.delete(0, END) # clear display
        display.insert(END, calc_functions.to_roman(n))
    elif key == functions_list[2]:
        n = display.get() # collect display value
        display.delete(0, END) # clear display
        display.insert(END, calc_functions.to_binary(n))
    elif key == functions_list[3]:
        n = display.get() # collect display value
        display.delete(0, END) # clear display
        display.insert(END, calc_functions.from_binary(n))


    # add other key-pressed values to end of current entry:
    else:
        display.insert(END, key)

##### main:
window = Tk()
window.title("MyCalculator")

# create top_row frame
top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# use Entry widget for an editable display
display = Entry(top_row, width=45, bg="light green")
display.grid()

# create num_pad_frame
num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky=W)

num_pad_list = [
'7',  '8',  '9',
'4',  '5',  '6',
'1',  '2',  '3',
'0',  '.',  '=' ]

# create num_pad buttons with a loop
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r+1

# create operator_frame
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)

operator_list = [
'*', '/',  
'+', '-',
'(', ')',
'C' ]

# create operator buttons with a loop
r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text=btn_text, width=5, command=cmd).grid(row=r,column=c)
    c = c+1
    if c > 1:
        c = 0
        r = r+1

# create constants_frame
constants = Frame(window)
constants.grid(row=3, column=0, sticky=W)

constants_list = [
'pi',
'speed of light(m/s)',
'speed of sound (m/s)',
'ave dist to sun (km)' ]

# create constants buttons with a loop
r = 0
c = 0
for btn_text in constants_list:
    def cmd(x=btn_text):
        click(x)
    Button(constants, text=btn_text, width=22, command=cmd).grid(row=r, column=c)
    r = r+1

# create functions_frame
functions = Frame(window)
functions.grid(row=3, column=1, sticky=E)

functions_list = [
'factorial (!)',
'-> roman',
'-> binary',
'binary -> 10' ]

# create functions buttons with a loop
r = 0
c = 0
for btn_text in functions_list:
    def cmd(x=btn_text):
        click(x)
    Button(functions, text=btn_text, width=13, command=cmd).grid(row=r, column=c)
    r = r+1

##### Run mainloop
window.mainloop()

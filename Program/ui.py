# ui.py
# Importing libraries and module 
import tkinter
from buttons import create_buttons

# Starting to write the code
# Create the window
window = tkinter.Tk()
window.title('Grillmaster Calculator')  # Name of the calculator
window.geometry("800x600")
window.resizable(False, False)  # This will be used so that the size of the window cannot be changed
window.configure(background='gray20')  # background
operator = ''  # we will need a variable

global display_text, display_aux, display_aux2, main_display, aux_display, aux_display2, aux_display3
# With this we create the variables of the text inputs
display_text = tkinter.StringVar()
display_aux = tkinter.StringVar()
display_aux2 = tkinter.StringVar()

# We will use the screen
main_display = tkinter.Entry(window, font=('arial', 20), width=23, borderwidth=5, textvariable=display_text, justify=tkinter.RIGHT)
main_display.place(x=25, y=50, width=360, height=70)

aux_display = tkinter.Entry(window, font=('arial', 20), textvariable=display_aux, width=24, borderwidth=None)
aux_display.place(x=410, y=335, relheight=0.26)

aux_display2 = tkinter.Entry(window, width=60, borderwidth=None)
aux_display2.place(x=410, y=25, relheight=0.5)

aux_display3 = tkinter.Entry(window, font=('arial', 20), textvariable=display_aux2, width=24, borderwidth=1)
aux_display3.place(x=410, y=335, relheight=None)

title_label = tkinter.Label(window, text="Grillmaster Calculator", font=('Cascadia Code', 17), bg='gray20', fg='white')
title_label.place(x=25, y=10)

create_buttons(window)

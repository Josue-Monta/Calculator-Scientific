# buttons.py
# Importing libraries and modules
import tkinter as tk
from operations import clear_all, add_character, delete_last, handle_operations, evaluate, approximate, show_roots
from plotting_2d import plot_graph
from plotting_3d import plot_3d_graph
from calculus_operations import differentiate, integrate_indefinitely, calculate_limits

def create_buttons(window):
    # Buttons of the first row
    tk.Button(window, text='x', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('x')).place(x=25, y=140)
    tk.Button(window, text='log()', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('log')).place(x=117, y=140)
    tk.Button(window, text='x^', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('**')).place(x=210, y=140)
    tk.Button(window, text='π', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('pi')).place(x=301, y=140)

    # Buttons of the second row
    tk.Button(window, text='√', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('sqrt')).place(x=25, y=190)
    tk.Button(window, text='sin', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('sin')).place(x=117, y=190)
    tk.Button(window, text='cos', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('cos')).place(x=209, y=190)
    tk.Button(window, text='tan', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('tan')).place(x=301, y=190)

    # Buttons of the third row
    tk.Button(window, text=',', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: add_character(',')).place(x=25, y=240)
    tk.Button(window, text='(', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('(')).place(x=117, y=240)
    tk.Button(window, text=')', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations(')')).place(x=209, y=240)
    tk.Button(window, text='e', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: add_character('E')).place(x=301, y=240)

    # Buttons of the second grid
    # Buttons of the fourth row
    tk.Button(window, text='7', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(7)).place(x=25, y=300)
    tk.Button(window, text='8', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(8)).place(x=97, y=300)
    tk.Button(window, text='9', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(9)).place(x=169, y=300)
    tk.Button(window, text='DEL', bd=10, bg='yellowgreen', fg='white', width=6, height=2, command=lambda: delete_last()).place(x=241, y=300)
    tk.Button(window, text='AC', bd=10, bg='yellowgreen', fg='white', width=6, height=2, command=lambda: clear_all()).place(x=313, y=300)

    # Buttons of the fifth row
    tk.Button(window, text='4', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(4)).place(x=25, y=370)
    tk.Button(window, text='5', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(5)).place(x=97, y=370)
    tk.Button(window, text='6', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(6)).place(x=169, y=370)
    tk.Button(window, text='x', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('*')).place(x=241, y=370)
    tk.Button(window, text='÷', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('/')).place(x=313, y=370)

    # Buttons of the sixth row
    tk.Button(window, text='1', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(1)).place(x=25, y=440)
    tk.Button(window, text='2', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(2)).place(x=97, y=440)
    tk.Button(window, text='3', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(3)).place(x=169, y=440)
    tk.Button(window, text='+', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('+')).place(x=241, y=440)
    tk.Button(window, text='-', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('-')).place(x=313, y=440)

    # Buttons of the seventh row
    tk.Button(window, text='0', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(0)).place(x=25, y=510)
    tk.Button(window, text='.', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('.')).place(x=97, y=510)
    tk.Button(window, text='GRAPH', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: plot_graph()).place(x=169, y=510)
    tk.Button(window, text='APPROX', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: approximate()).place(x=241, y=510)
    tk.Button(window, text='=', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: evaluate()).place(x=313, y=510)

    # Calculation buttons
    # Buttons second column
    tk.Button(window, text='3D', bd=10, bg='gray40', fg='white', width=5, height=3, command=lambda: plot_3d_graph()).place(x=410, y=510)

    tk.Button(window, text='f/(x)', bd=10, bg='gray40', fg='white', font=('arial', 20), width=3, height=1, command=lambda: differentiate()).place(x=475, y=510)

    tk.Button(window, text='∫', bd=10, bg='gray40', fg='white', font=('arial', 20), width=2, height=1, command=lambda: integrate_indefinitely()).place(x=555, y=510)

    tk.Button(window, text='∫ₐᵇ', bd=10, bg='gray40', fg='white', font=('arial', 20), width=2, height=1, command=lambda: calculate_limits()).place(x=618, y=510)

    tk.Button(window, text='Roots', bd=10, bg='gray40', fg='white', width=10, height=3, command=lambda: show_roots()).place(x=680, y=510)

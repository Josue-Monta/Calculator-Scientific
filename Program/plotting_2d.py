# plotting_2d.py
# Importing libraries
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def plot_graph():
    # We graph the functions
    
    from ui import (main_display, window)
    
    expression = main_display.get()
    expression1 = sym.sympify(expression)
    x = sym.Symbol('x')  # To use the symbol
    values_range = np.linspace(-15, 15, 100, endpoint=True)  # Values that the function will take
    values = []

    figure = plt.figure(figsize=(4, 3), dpi=100)  # A graph is created
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    task_bars = NavigationToolbar2Tk(canvas, window)
    task_bars.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

    for i in range(len(values_range)):  # We are taking values for {y}
        y_value = ((expression1).evalf(subs={x: values_range[i]}))  # The expression is evaluated and the values are substituted
        values.append(y_value)

    figure.add_subplot(111).plot(values_range, values, label='{0}'.format(expression))
    plt.legend(loc='upper left')  # the legend is displayed
    plt.grid()  # The grid is displayed
    canvas.draw()  # The graph is displayed
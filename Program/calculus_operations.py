# calculus_operations.py
# Importing libraries
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def calculate_limits():
    # Function for Defined Integrals
    
    from ui import (display_aux, display_aux2, main_display, aux_display, aux_display3, window)
    display_aux.set('')
    display_aux2.set('')
    expression = main_display.get()
    message = 'The value of the defined integral is:'
    aux_display3.insert(0, message)
    components = expression.split(',')
    lower_limit = float(components[1])
    upper_limit = float(components[2])
    integral_expression = components[0]
    integral_expr = sym.sympify(integral_expression)

    x = sym.Symbol('x')
    integral_result = sym.integrate(integral_expr, (x, lower_limit, upper_limit))
    aux_display.insert(0, integral_result)

    # Graph configuration
    values_range = np.linspace(-15, 15, 100, endpoint=True)
    values = []

    figure = plt.figure(figsize=(4, 3), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    task_bar = NavigationToolbar2Tk(canvas, window)
    task_bar.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

    # Evaluation of the defined integral
    for value in values_range:
        if lower_limit <= value <= upper_limit:
            y_value = integral_expr.evalf(subs={x: value})
            y_value = float(y_value) if y_value.is_real else 0 # Make sure y_value is a floating number
        else:
            y_value = 0
        values.append(y_value)

    ax.fill_between(values_range, values, alpha=0.3, label=f'Area under {integral_expr}')
    ax.plot(values_range, values, label=f'{integral_expr}')
    plt.legend(loc='upper left')
    plt.grid()
    canvas.draw()

def differentiate():
    # Function to derive
     
    from ui import (display_aux, display_aux2, main_display, aux_display, aux_display3, window)
    
    display_aux.set('')
    display_aux2.set('')
    d = main_display.get()
    if 'x' in d:  # The variable by which it will be derived is displayed
        d_expr = sym.sympify(d)
        derivative_result = sym.diff(d_expr, 'x')
        aux_display.insert(0, derivative_result)
        message = 'The derivative is: '
        aux_display3.insert(0, message)
        expression = aux_display.get()  # Graph again
        expression1 = sym.sympify(expression)
        x = sym.Symbol('x')
        values_range = np.linspace(-15, 15, 100, endpoint=True)
        values = []
        figure = plt.figure(figsize=(4, 3), dpi=100)
        ax = figure.add_subplot(111)
        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
        task_bars = NavigationToolbar2Tk(canvas, window)
        task_bars.place(x=410, y=290, relwidth=0.455)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

        for i in range(len(values_range)):
            y_value = ((expression1).evalf(subs={x: values_range[i]}))
            values.append(y_value)
        ax.clear()
        ax.plot(values_range, values, label='{0}'.format(expression))
        plt.grid()
        canvas.draw()
        expression = main_display.get()  # Display along with the graph of the original function
        expression1 = sym.sympify(expression)
        x = sym.Symbol('x')
        values_range = np.linspace(-15, 15, 100, endpoint=True)
        values = []
        figure = Figure(figsize=(4, 3), dpi=100)
        canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
        task_bar = NavigationToolbar2Tk(canvas, window)
        task_bar.place(x=410, y=25, relwidth=0.455)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

        for i in range(len(values_range)):
            y_value = ((expression1).evalf(subs={x: values_range[i]}))
            values.append(y_value)
        ax.plot(values_range, values, label='{0}'.format(expression))
        plt.legend(loc='upper left')
        canvas.draw()

    else:  # differentiation variable for y
        d_expr = sym.sympify(d)
        derivative_result = sym.diff(d_expr, 'y')
        aux_display.insert(0, derivative_result)
        message = 'The derivative is: '
        aux_display3.insert(0, message)
        expression = aux_display.get()
        expression1 = sym.sympify(expression)
        y_value = ''
        y = sym.Symbol('y')
        values_range = np.linspace(-15, 15, 100, endpoint=True)
        values = []
        figure = plt.figure(figsize=(4, 3), dpi=100)
        ax = figure.add_subplot(111)
        canvas = FigureCanvasTkAgg(figure, master=window)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)
        task_bar = NavigationToolbar2Tk(canvas, window)
        task_bar.place(x=410, y=290, relwidth=0.455)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)
        for i in range(len(values_range)):
            y_value = ((expression1).evalf(subs={y: values_range[i]}))
            values.append(y_value)
        ax.clear()
        ax.plot(values_range, values, label='{0}'.format(expression))
        plt.grid()
        canvas.draw()
        # Old graph
        expression = main_display.get()  # Display along with the graph of the original function
        expression1 = sym.sympify(expression)
        x = sym.Symbol('x')
        values_range = np.linspace(-15, 15, 100, endpoint=True)
        values = []
        figure = Figure(figsize=(4, 3), dpi=100)
        canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
        task_bar = NavigationToolbar2Tk(canvas, window)
        task_bar.place(x=410, y=25, relwidth=0.455)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

        for i in range(len(values_range)):
            y_value = ((expression1).evalf(subs={x: values_range[i]}))
            values.append(y_value)
        ax.plot(values_range, values, label='{0}'.format(expression))
        plt.legend(loc='upper left')
        canvas.draw()

def integrate_indefinitely():
    # integrate functions
    from ui import (display_aux, display_aux2, main_display, aux_display, aux_display3, window)
    
    display_aux.set('')
    display_aux2.set('')
    integral = main_display.get()

    # Symbolize the expression
    integral_expr = sym.sympify(integral)
    # Calculate the indefinite integral
    x = sym.Symbol('x')
    integral_result = sym.integrate(integral_expr, x)
    aux_display.insert(0, integral_result)

    # Message on aux_display3
    message = 'The indefinite integral is:'
    aux_display3.insert(0, message)

    # Graph configuration
    values_range = np.linspace(-15, 15, 100, endpoint=True)
    values = []

    figure = plt.figure(figsize=(4, 3), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    task_bar = NavigationToolbar2Tk(canvas, window)
    task_bar.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

    # Evaluation of the integral for each value of x
    for value in values_range:
        y_value = integral_result.evalf(subs={x: value})
        values.append(y_value)

    ax.plot(values_range, values, label=f'{integral_result}')
    plt.legend(loc='upper left')
    plt.grid()

    canvas.draw()

    # Graph of the original function
    original_function_values = []
    for value in values_range:
        y_value = integral_expr.evalf(subs={x: value})
        original_function_values.append(y_value)

    ax.plot(values_range, original_function_values, label=f'{integral_expr}', linestyle='dashed')
    plt.legend(loc='upper left')
    canvas.draw()
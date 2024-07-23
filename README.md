Names Nikolai Panchi and Josue Monta
Grillmaster Calculator
Overview
The Grillmaster Calculator is a scientific calculator developed using Python. It offers advanced mathematical functionalities including trigonometric calculations, logarithms, derivatives, integrals, and 2D/3D graph plotting. This project leverages libraries such as tkinter, sympy, numpy, and matplotlib to create an interactive and comprehensive tool for mathematical computations.

Features
Basic Arithmetic Operations: Addition, subtraction, multiplication, and division.
Trigonometric Functions: Sine (sin), cosine (cos), and tangent (tan) in degrees.
Logarithmic Calculations: Base 10 logarithms (log).
Power and Root Calculations: Exponentiation and square roots.
Parentheses and Constants: Handling of parentheses and mathematical constants like π (pi) and e.
Polynomial Roots: Calculation and display of polynomial roots.
Derivatives: Calculation and display of derivatives.
Integrals: Calculation and display of indefinite and definite integrals.
Graph Plotting: 2D and 3D graph plotting capabilities.
Requirements
Python Version: Python 3.6 or higher.
Libraries:
tkinter: Standard Python library for GUI development.
sympy: For symbolic mathematics.
numpy: For numerical operations.
matplotlib: For 2D and 3D plotting.


Installation
Install required libraries:
pip install sympy numpy matplotlib



Functionality Breakdown
Main Display
Description: Displays the input and results of the operations.
main_display = tkinter.Entry(window, font=('arial', 20), width=23, borderwidth=5, textvariable=display_text, justify=tkinter.RIGHT)
main_display.place(x=25, y=50, width=360, height=70)

Auxiliary Displays
Auxiliary Display 1:
Description: Shows intermediate results or additional information.
Code:
aux_display = tkinter.Entry(window, font=('arial', 20), textvariable=display_aux, width=24, borderwidth=None)
aux_display.place(x=410, y=335, relheight=0.26)


Auxiliary Display 2:
Description: Currently not used directly in the code, can be used for future features.
Code:
aux_display2 = tkinter.Entry(window, width=60, borderwidth=None)
aux_display2.place(x=410, y=25, relheight=0.5)


Auxiliary Display 3:
Description: Displays messages like "The derivative is:" or "The indefinite integral is:".
Code:
aux_display3 = tkinter.Entry(window, font=('arial', 20), textvariable=display_aux2, width=24, borderwidth=1)
aux_display3.place(x=410, y=335, relheight=None)

Key Functionalities
Clear All
Function: Clears the main and auxiliary displays.
Code:
def clear_all():
    global operator
    operator = ''
    display_text.set('')
    display_aux.set('')
    display_aux2.set('')

    figure = plt.figure(figsize=(4, 3), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

    plt.clf()

    Add Character
Function: Adds a character to the main display.
Code:
def add_character(n):
    global index
    main_display.insert(index, n)
    index += 1

Calculate Trigonometric Functions
Function: Calculates the value of trigonometric functions (sin, cos, tan).
Code:
def calculate_trigonometric(expression):
    try:
        if any(func in expression for func in ['sin', 'cos', 'tan']):
            func, num = expression.split('(')
            num = num.rstrip(')')
            number = float(num)

        if func == 'sin':
            result = np.sin(np.deg2rad(number))
        elif func == 'cos':
            result = np.cos(np.deg2rad(number))
        elif func == 'tan':
            result = np.tan(np.deg2rad(number))
        else:
            result = None
        result = round(result, 10)
    except:
        result = None
    return result

Calculate Logarithm
Function: Calculates the logarithm base 10 of a number.
Code:
def calculate_logarithm(num):
    try:
        if 'log' in num:
            start = num.index('(') + 1
            end = num.index(')')
            value = float(num[start:end])
            result = np.log10(value)
    except:
        result = None
    return result


Handle Operations
Function: Inserts operations or functions in the main display.
Code:
def handle_operations(b):
    global index
    if b in ['sin', 'cos', 'tan', 'sqrt', 'log']:
        main_display.insert(index, b + '(')
        index += len(b) + 1
    else:
        main_display.insert(index, b)
        index += 1


Show Roots
Function: Displays the roots of a polynomial.
Code:
def show_roots():
    display_aux.set("")
    display_aux2.set("")
    message = 'The roots are: '
    aux_display3.insert(0, message)
    polynomial = main_display.get()
    poly_expr = sym.sympify(polynomial)
    roots = sym.roots(poly_expr, multiple=True)
    roots_text = ', '.join([str(root.evalf(5)) for root in roots])
    aux_display.insert(0, roots_text)

Delete Last Character
Function: Deletes the last character in the main display.
Code:
def delete_last():
    content = main_display.get()
    if len(content):
        new_content = content[:-1]
        clear_all()
        main_display.insert(0, new_content)
    else:
        clear_all()


Evaluate Expression
Function: Evaluates the entered mathematical expression.
Code:
def evaluate():
    current_state = main_display.get()
    try:
        if any(func in current_state for func in ['sin', 'cos', 'tan']):
            result = calculate_trigonometric(current_state)
        elif 'log' in current_state:
            result = calculate_logarithm(current_state)
        elif any(func in current_state for func in ['E', 'pi']):
            result = sym.sympify(current_state).evalf(15)
        elif 'sqrt' in current_state:
            result = sym.sympify(current_state).evalf(3)
        else:
            result = sym.sympify(current_state)

        clear_all()
        main_display.insert(0, result)
    except:
        clear_all()

Plot Graph (2D)
Function: Plots a 2D graph of the entered function.
Code:
def plot_graph():
    expression = main_display.get()
    expression1 = sym.sympify(expression)
    x = sym.Symbol('x')
    values_range = np.linspace(-15, 15, 100, endpoint=True)
    values = []

    figure = plt.figure(figsize=(4, 3), dpi=100)
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    task_bars = NavigationToolbar2Tk(canvas, window)
    task_bars.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

    for i in range(len(values_range)):
        y_value = ((expression1).evalf(subs={x: values_range[i]}))
        values.append(y_value)

    figure.add_subplot(111).plot(values_range, values, label='{0}'.format(expression))
    plt.legend(loc='upper left')
    plt.grid()
    canvas.draw()

Plot Graph (3D)
Function: Plots a 3D graph of the entered function.
Code:
def plot_3d_graph():
    expression = main_display.get()
    expression1 = sym.sympify(expression)
    x, y = sym.symbols('x y')

    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(-10, 10, 100)
    Y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(X, Y)
    Z = sym.lambdify((x, y), expression1)(X, Y)

    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'3D Graph of {expression}')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    task_bar = NavigationToolbar2Tk(canvas, window)
    task_bar.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)
    canvas.draw()

Calculate Definite Integrals
Function: Calculates and displays definite integrals.
Code:
def calculate_limits():
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

    values_range = np.linspace(-15, 15, 100, endpoint=True)
    values = []

    figure = plt.figure(figsize=(4, 3), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    task_bar = NavigationToolbar2Tk(canvas, window)
    task_bar.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

    for value in values_range:
        if lower_limit <= value <= upper_limit:
            y_value = integral_expr.evalf(subs={x: value})
            y_value = float(y_value) if y_value.is_real else 0
        else:
            y_value = 0
        values.append(y_value)

    ax.fill_between(values_range, values, alpha=0.3, label=f'Area under {integral_expr}')
    ax.plot(values_range, values, label=f'{integral_expr}')
    plt.legend(loc='upper left')
    plt.grid()

    canvas.draw()

Differentiate Functions
Function: Calculates and displays derivatives.
Code:
def differentiate():
    display_aux.set('')
    display_aux2.set('')
    d = main_display.get()
    if 'x' in d:
        d_expr = sym.sympify(d)
        derivative_result = sym.diff(d_expr, 'x')
        aux_display.insert(0, derivative_result)
        message = 'The derivative is: '
        aux_display3.insert(0, message)

        expression = aux_display.get()
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
        expression = main_display.get()
        expression1 = sym.sympify(expression)
        x = sym.Symbol('x')
        values_range = np.linspace(-15, 15, 100, endpoint=True)
        values = []
        figure = plt.figure(figsize=(4, 3), dpi=100)
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
    else:
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

        expression = main_display.get()
        expression1 = sym.sympify(expression)
        x = sym.Symbol('x')
        values_range = np.linspace(-15, 15, 100, endpoint=True)
        values = []
        figure = plt.figure(figsize=(4, 3), dpi=100)
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

Integrate Indefinitely
Function: Calculates and displays indefinite integrals.
Code:
def integrate_indefinitely():
    display_aux.set('')
    display_aux2.set('')
    integral = main_display.get()

    integral_expr = sym.sympify(integral)
    x = sym.Symbol('x')
    integral_result = sym.integrate(integral_expr, x)
    aux_display.insert(0, integral_result)

    message = 'The indefinite integral is:'
    aux_display3.insert(0, message)

    values_range = np.linspace(-15, 15, 100, endpoint=True)
    values = []

    figure = plt.figure(figsize=(4, 3), dpi=100)
    ax = figure.add_subplot(111)
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
    task_bar = NavigationToolbar2Tk(canvas, window)
    task_bar.place(x=410, y=290, relwidth=0.455)
    canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

    for value in values_range:
        y_value = integral_result.evalf(subs={x: value})
        values.append(y_value)

    ax.plot(values_range, values, label=f'{integral_result}')
    plt.legend(loc='upper left')
    plt.grid()

    canvas.draw()

    original_function_values = []
    for value in values_range:
        y_value = integral_expr.evalf(subs={x: value})
        original_function_values.append(y_value)

    ax.plot(values_range, original_function_values, label=f'{integral_expr}', linestyle='dashed')
    plt.legend(loc='upper left')
    canvas.draw()


Creating Buttons

# First Row Buttons
button11 = tkinter.Button(window, text='x', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('x')).place(x=25, y=140)
button12 = tkinter.Button(window, text='log()', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('log')).place(x=117, y=140)
button13 = tkinter.Button(window, text='x^', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('**')).place(x=210, y=140)
button14 = tkinter.Button(window, text='π', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('pi')).place(x=301, y=140)

# Second Row Buttons
button21 = tkinter.Button(window, text='√', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('sqrt')).place(x=25, y=190)
button22 = tkinter.Button(window, text='sin', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('sin')).place(x=117, y=190)
button23 = tkinter.Button(window, text='cos', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('cos')).place(x=209, y=190)
button24 = tkinter.Button(window, text='tan', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('tan')).place(x=301, y=190)

# Third Row Buttons
button31 = tkinter.Button(window, text=',', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: add_character(',')).place(x=25, y=240)
button32 = tkinter.Button(window, text='(', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations('(')).place(x=117, y=240)
button33 = tkinter.Button(window, text=')', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: handle_operations(')')).place(x=209, y=240)
button34 = tkinter.Button(window, text='e', bd=10, bg='gray5', fg='white', width=8, height=1, command=lambda: add_character('E')).place(x=301, y=240)

# Fourth Row Buttons
button41 = tkinter.Button(window, text='7', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(7)).place(x=25, y=300)
button42 = tkinter.Button(window, text='8', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(8)).place(x=97, y=300)
button43 = tkinter.Button(window, text='9', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(9)).place(x=169, y=300)
button44 = tkinter.Button(window, text='DEL', bd=10, bg='yellowgreen', fg='white', width=6, height=2, command=lambda: delete_last()).place(x=241, y=300)
button45 = tkinter.Button(window, text='AC', bd=10, bg='yellowgreen', fg='white', width=6, height=2, command=lambda: clear_all()).place(x=313, y=300)

# Fifth Row Buttons
button51 = tkinter.Button(window, text='4', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(4)).place(x=25, y=370)
button52 = tkinter.Button(window, text='5', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(5)).place(x=97, y=370)
button53 = tkinter.Button(window, text='6', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(6)).place(x=169, y=370)
button54 = tkinter.Button(window, text='x', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('*')).place(x=241, y=370)
button55 = tkinter.Button(window, text='÷', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('/')).place(x=313, y=370)

# Sixth Row Buttons
button61 = tkinter.Button(window, text='1', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(1)).place(x=25, y=440)
button62 = tkinter.Button(window, text='2', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(2)).place(x=97, y=440)
button63 = tkinter.Button(window, text='3', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(3)).place(x=169, y=440)
button64 = tkinter.Button(window, text='+', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('+')).place(x=241, y=440)
button65 = tkinter.Button(window, text='-', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('-')).place(x=313, y=440)

# Seventh Row Buttons
button71 = tkinter.Button(window, text='0', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: add_character(0)).place(x=25, y=510)
button72 = tkinter.Button(window, text='.', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: handle_operations('.')).place(x=97, y=510)
button73 = tkinter.Button(window, text='GRAPH', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: plot_graph()).place(x=169, y=510)
button74 = tkinter.Button(window, text='APPROX', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: approximate()).place(x=241, y=510)
button75 = tkinter.Button(window, text='=', bd=10, bg='gray40', fg='white', width=6, height=2, command=lambda: evaluate()).place(x=313, y=510)

# Additional Buttons
button0 = tkinter.Button(window, text='3D', bd=10, bg='gray40', fg='white', width=5, height=3, command=lambda: plot_3d_graph()).place(x=410, y=510)
button1 = tkinter.Button(window, text='f/(x)', bd=10, bg='gray40', fg='white', font=('arial', 20), width=3, height=1, command=lambda: differentiate()).place(x=475, y=510)
button2 = tkinter.Button(window, text='∫', bd=10, bg='gray40', fg='white', font=('arial', 20), width=2, height=1, command=lambda: integrate_indefinitely()).place(x=555, y=510)
button3 = tkinter.Button(window, text='∫ₐᵇ', bd=10, bg='gray40', fg='white', font=('arial', 20), width=2, height=1, command=lambda: calculate_limits()).place(x=618, y=510)
button4 = tkinter.Button(window, text='Roots', bd=10, bg='gray40', fg='white', width=10, height=3, command=lambda: show_roots()).place(x=680, y=510)


Graph:

![image](https://github.com/user-attachments/assets/98fe4a8b-a038-4035-b3e6-51af4457c21c)

3D Graph:

![image](https://github.com/user-attachments/assets/5795da9c-0c84-4cbe-8640-ee35b82e77ba)

Arithmetical operations:

![image](https://github.com/user-attachments/assets/9c81cd58-f2a7-4d6a-9ced-5e5efff792b7)

Derivate:

![image](https://github.com/user-attachments/assets/eb7bc762-6aa4-4779-80af-1887276a5a52)

Integral:

![image](https://github.com/user-attachments/assets/14a137f7-fe7d-4409-aff6-ea5d9d4a4fd5)

Roots:


![image](https://github.com/user-attachments/assets/bd66fc0d-bc24-4c06-bf1e-b54c181be7d6)






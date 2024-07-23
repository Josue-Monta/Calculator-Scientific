# operations.py
# Importing libraries
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Now we define the code for the functions
index = 0
 

def clear_all():
    # This function is used to clear the code
    
        from ui import (display_text, display_aux, display_aux2, window)
        global operator
        operator = ''
        display_text.set('')  # We leave the screen empty
        display_aux.set('')
        display_aux2.set('')

        figure = plt.figure(figsize=(4, 3), dpi=100)  # Figure dimensions and sizes are defined
        canvas = FigureCanvasTkAgg(figure, master=window)  # The drawing area is defined
        canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
        toolbar = NavigationToolbar2Tk(canvas, window)  # A toolbar is added to improve graphs
        toolbar.place(x=410, y=290, relwidth=0.455)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)

        plt.clf()  # Clear graph content

def add_character(n):
    # Function to appear on screen with buttons
    
        from ui import (main_display)
        global index  # To use the variable anywhere in the code
        main_display.insert(index, n)
        index += 1  # Characters are added so they are not deleted

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

def handle_operations(b):
    # Function to solve arithmetic operations
    
        from ui import ( main_display,  window)
        global index
        if b in ['sin', 'cos', 'tan', 'sqrt', 'log']:  # Checks if it is a trigonometric function
            main_display.insert(index, b + '(')  # Inserts the function with opening parenthesis
            index += len(b) + 1  # Increments the index
        else:
            main_display.insert(index, b)  # Normally inserts the number or symbol
            index += 1  # Increments the index
            
def show_roots():
     # Function to display roots
     
        from ui import (display_aux, display_aux2, main_display, aux_display,  aux_display3, window)
        display_aux.set("")
        display_aux2.set("")
        message = 'The roots are: '
        aux_display3.insert(0, message)
        polynomial = main_display.get()
        poly_expr = sym.sympify(polynomial)
        roots = sym.roots(poly_expr, multiple=True)
        roots_text = ', '.join([str(root.evalf(5)) for root in roots])
        aux_display.insert(0, roots_text)

def delete_last():
    # Function to delete character by character
    
        from ui import ( main_display)
        content = main_display.get()  # screen content
        if len(content):  # Number of characters >0
            new_content = content[:-1]  # The last element of the screen is removed
            clear_all()
            main_display.insert(0, new_content)  # The remaining characters are shown, not counting the deleted one
        else:
            clear_all()  # Call the function in case of having no characters

def evaluate():
    # To evaluate operations and present results
    
        from ui import (main_display)
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
                result = sym.sympify(current_state) # The screen content becomes a mathematical expression

            clear_all()
            main_display.insert(0, result) # The solution is printed
        except:
            clear_all()

def approximate():
    # Show values in decimal form
    # 15 decimals are shown
        from ui import (main_display,)
        content = main_display.get()
        approximation = (sym.sympify(content)).evalf(15)
        clear_all()
        main_display.insert(0, approximation)

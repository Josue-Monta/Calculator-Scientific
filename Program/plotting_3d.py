# plotting_3d.py
# Importing libraries
import sympy as sym
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D



def plot_3d_graph():
    # We graph 3d the functions
    
    from ui import (main_display, window)
    try:
        expression = main_display.get()
        expression1 = sym.sympify(expression)
        x, y = sym.symbols('x y')  # Define symbols for variables x and y

        fig = plt.figure(figsize=(6, 5))
        ax = fig.add_subplot(111, projection='3d')

        X = np.linspace(-10, 10, 100)  # Generate data for the 3D surface
        Y = np.linspace(-10, 10, 100)
        X, Y = np.meshgrid(X, Y)
        Z = sym.lambdify((x, y), expression1)(X, Y)

        ax.plot_surface(X, Y, Z, cmap='viridis')  # Graphs the surface

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'3D Graph of {expression}')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.get_tk_widget().place(x=25, y=25, relwidth=0.455, relheight=0.44)
        canvas.get_tk_widget().place(x=410, y=25, relwidth=0.455)
        canvas.draw()  # Displays the Graph
        
    except Exception as e:
        print(f"Error: {e}")

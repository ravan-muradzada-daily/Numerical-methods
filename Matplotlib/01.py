import numpy as np
import matplotlib.pyplot as plt
# We use this modul

def f(x):
    return x*x - 2*x + 3

'''
    Matplotlib.pyplot is used to sketch the graph of functions and note some special things on it.

    To use it, of course, we need x values and f(x).
    I will use sample x values and f(x) function here.

    Some methods of matplotlib:

    1. plot(x, y, label = "...", color = "...")
        This function sketches the graph according to x and y values. Note that, our x and y should be sequence (like array).
        Such us, x = np.array([1, 4, 8, 9])  and y = f(x). Here it calculates the results according to f function using elements of x. 
        Then sketch the graph according to these values.
        However, it is better to use linspace(..) method for x, instead. How does it work? -> The first and second parameters are starting and stopping points of x, correspondingly. The third parameter is the number of points between start and stop points. So the sequence is divided to the number of equal parts (=third parameterer). linspace(...) functions comes from numpy.

        If we want to show just one point in the graph, we can also use plot() function, but here we should specify the color of the point.
        Note that, the color should be always the third variable and written using "*" then the first letter of the color, like "*r" for red.

        In the method, label parameter writes about the function. We can write anything here.

        For the graph sketching, we can use color parameter and need to write the name of color, like color="blue".
    
    2. title(...)
        This method gives the title to the graph. Anything we can write here.
    
    3. xlabel(...) and ylabel(...)
        These give the names to x and y labels, correspondingly.

    4. grid(True)
        This method enables the grids in the graph.
    
    5. legend()
        This writes the labels. (From the plot() method). It is good always to use it at the last and once.

    6. show()
        This shows us the sketched graph. We have to always use it at the last and once.

    7. axhline(k, color=' ', lw = n)
        This adds a horizontal line at y=k to the plot. The color argument specifies the line's color, and lw (line width) sets the thickness of the line.
    
    8. axvline(k, color=' ', lw = n)
        This function adds a vertical line at x=k. The color argument specifies the line's color, and lw (line width) sets the thickness of the line.

    9. scatter(x, y, label = "...")
        It is mostly the same with plot() method, but its line is more thick.

    10. xlim(start, stop) 
        (start, stop) is the range here for x.
        Any data points outside this range will not be displayed. 
        It is useful when you want to focus on a specific region of the plot along the x-axis.

    11. ylim(start, stop)
        (start, stop) is the range here for y.
        Any data points outside this range will not be displayed.
        It is useful for zooming in on a specific region of the plot along the y-axis.
'''

#x = np.array([1, 4, 8, 9])
x = np.linspace(1, 10, 1000) # Creates a range
y = f(x)

plt.plot(x, y, label="f(x) = x^2 - 2*x + 3", color="orange") # Sketch the graph

plt.title('Graph of f(x)') # Give the title
 
plt.xlabel('x') # Gives the name to x label
plt.ylabel('y') # Gives the name to y label

plt.axhline(4, color='blue', lw=2) # y = 4
plt.axvline(3, color='green', lw=1.75) # x = 3

plt.plot(9, 8, "*b", label="Some point") # Blue point in (9, 8)

plt.xlim(0, 8) 
plt.ylim(-5, 11)

plt.grid(True) # Enables the grids

plt.legend()
plt.show()
from sympy import lambdify, symbols, diff
import numpy as np
import random
from matplotlib import pyplot as plt

def apply_GD(function_equation, x, y, learning_rate = 0.1):
    partial_derivative_x = diff(function_equation,x)
    partial_derivative_y = diff(function_equation,y)

    print(partial_derivative_x, partial_derivative_y)

    x_list = list()
    y_list = list()

    x0 = random.randint(-10,10)
    y0 = random.randint(-10,10)

    # print(x0, y0, end='\n')
    x_list.append(x0)
    y_list.append(y0)
    
    for i in range(4000):
        eval_partial_derivative_at_x = partial_derivative_x.subs(x, x0)
        eval_partial_derivative_at_y = partial_derivative_y.subs(y, y0)

        x0 = x0 - (learning_rate * eval_partial_derivative_at_x)
        y0 = y0 - (learning_rate * eval_partial_derivative_at_y)

        x_list.append(x0)
        y_list.append(y0)

    # print(eval_test_x, eval_test_y)
    # plt.scatter(x_list, y_list)
    # plt.show()

    return x_list, y_list

def main():

    x = symbols('x')
    y = symbols('y')

    function_equation = x**2 - 6*x + y**2 +10*y +20

    learning_rate = 0.001

    x_coordinates_list, y_coordinates_list = apply_GD(function_equation, x, y, learning_rate)

    print(x_coordinates_list[len(x_coordinates_list)-1], y_coordinates_list[len(y_coordinates_list)-1])

    numpy_function = lambdify([x,y], function_equation, 'numpy')

    x_grid = np.linspace(-10, 10, 40)
    y_grid = np.linspace(-10, 10)

    X, Y = np.meshgrid(x_grid, y_grid)
    Z = numpy_function(X, Y)

    x_array = np.array(x_coordinates_list, dtype="float64")
    y_array = np.array(y_coordinates_list, dtype="float64")
    z_coordinates_list = list(numpy_function(x_array, y_array))

    ax = plt.axes(projection = '3d')
    ax.plot_surface(X, Y, Z, cstride = 1, rstride = 1, cmap = "winter", edgecolor = None)
    ax.plot(x_coordinates_list, y_coordinates_list, z_coordinates_list, 'ro', markersize = 5)
    ax.set_title("Gradient Descent \n Learning rate = {0}\n Starting Point = ({1},{2})\n Final Point = ({3},{4})\n Number of iterations = 4000".format(learning_rate,
                                                                                                                                                        x_coordinates_list[0],
                                                                                                                                                        y_coordinates_list[0],
                                                                                                                                                        x_coordinates_list[len(x_coordinates_list)-1],
                                                                                                                                                        y_coordinates_list[len(y_coordinates_list)-1]))
    plt.show()

if __name__ == "__main__":
    main()








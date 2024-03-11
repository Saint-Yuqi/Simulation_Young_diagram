import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def f(x):
    return x ** 2


def plot_lamerey_diagram(initial_point, iterations):
    x = np.linspace(-2, 2, 400)
    y = f(x)

    plt.figure(figsize=(10, 10))

    # Plot y=x diagonal
    plt.plot(x, x, 'b--', label="y=x")

    # Plot the function
    plt.plot(x, y, 'r', label="f(x) = x^2")

    current_point = initial_point
    for i in tqdm(range(iterations)):
        next_point = f(current_point)

        # Plot the vertical line from current_point to f(current_point)
        plt.plot([current_point, current_point], [current_point, next_point], 'g-')

        # Plot the horizontal line (reflection over y=x) to the diagonal
        plt.plot([current_point, next_point], [next_point, next_point], 'g-')

        current_point = next_point

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Lamerey Diagram for f(x) = x^2")
    plt.legend()
    plt.grid(True)
    plt.show()


# Test the function
plot_lamerey_diagram(0.5, 2)
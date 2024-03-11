import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


# Define the original function
def f(x):
    return r * (1 - x) * x


# Function that composes f with itself k times
def compose_f_k_times(x, k):
    for _ in tqdm(range(k)):
        x = f(x)
    return x


# Choose a k value for the number of compositions
r = 3
k = 3
m = 100

x_values = np.linspace(0, 1, m)

# Compute the composed function values
y_values = [compose_f_k_times(x_i, k) for x_i in x_values]

# Plotting the points
plt.scatter(x_values, y_values, color='blue')  # using scatter for individual points

# Labelling the axes
plt.xlabel('x_i')
plt.ylabel(f'f^({k})(x_i)')

# Title of the plot
plt.title(f'Graph of f^({k})(x_i) for {m}  integer points')

# Show grid
plt.grid(True)

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Function that composes logistic_map with itself k times and checks the range
def compose_logistic_map_k_times(x, k, r):
    for _ in tqdm(range(k)):
        x = logistic_map(r, x)
    return x

# Set the r value
r = 7

# Generate 100 normalized x_i points
x_values = np.linspace(0, 1, 1000)

# Define the levels of k
k_values = range(1, 6)

# Prepare to store the results
results = []

# Compute the composed function values and store them with color coding
for k in k_values:
    for x_i in x_values:
        y = compose_logistic_map_k_times(x_i, k, r)
        if 0 <= y <= 1:
            color = 'blue'
        else:
            color = 'white'
        results.append((x_i, k, color))

# Plot each point
for x_i, k, color in tqdm(results):
    plt.scatter(x_i, k, color=color, edgecolor='none', s=10)

# Labelling the axes
plt.xlabel('Normalized x_i')
plt.ylabel('Levels of k')

# Title of the plot
plt.title('Logistic Map Behavior for k Levels')

# Show grid
plt.grid(True)

# Adjust the plot range for better visualization
plt.ylim(0.5, 5.5)
plt.xlim(0, 1)

# Show the plot
plt.show()

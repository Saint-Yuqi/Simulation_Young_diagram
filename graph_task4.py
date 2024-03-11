import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Define the Lyapunov exponent calculation function
def lyapunov_exponent(r, x0, n):
    lyapunov = 0
    x = x0
    for i in tqdm(range(n)):
        x = logistic_map(r, x)
        # Calculate the derivative
        derivative = r - 2 * r * x
        # Check if the derivative is zero and skip the log calculation if it is
        if derivative != 0:
            lyapunov += np.log(abs(derivative))
        else:
            # If the derivative is zero, we can continue to the next iteration
            # without adding anything to the Lyapunov sum
            continue
    return lyapunov / n if n > 0 else float('-inf')  # Avoid division by zero if n is not positive


# Set the range of r and the initial condition x0
r_values = np.linspace(2, 4, 1000)
x0 = 0.1
n = 1000  # Number of iterations

# Calculate the Lyapunov exponent for each value of r
lyapunov_exponents = [lyapunov_exponent(r, x0, n) for r in r_values]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(r_values, lyapunov_exponents, ',r', alpha=1.0,  markersize=100)
plt.title('Lyapunov Exponent for Logistic Map')
plt.xlabel('r')
plt.ylabel('Lyapunov Exponent')
plt.grid(True)
plt.show()

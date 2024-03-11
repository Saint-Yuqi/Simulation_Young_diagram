import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import patches
import numpy as np

import random
from tqdm import tqdm
import math


def add_box(young_diagram):
    num = len(young_diagram)
    choices = []

    # Add a box to an existing row in the Young diagram
    for i in range(num):
        if i == 0 or young_diagram[i - 1] > young_diagram[i]:
            new_diagram = young_diagram.copy()
            new_diagram[i] += 1
            choices.append((new_diagram, (new_diagram[i] - 1, i)))

    # Add a new row to the Young diagram
    new_diagram = young_diagram + [1]
    choices.append((new_diagram, (0, num)))

    # Choose one of the possibilities uniformly at random
    chosen_diagram, position_added = random.choice(choices)
    return chosen_diagram, position_added


def generate_young_diagram(n):
    young_diagram = [1]
    positions = [(0, 0)]
    for _ in range(n - 1):
        young_diagram, position = add_box(young_diagram)
        positions.append(position)
    return young_diagram, positions


def build_deterministic_path(positions, n):
    path = [positions[0]]  # Starting position
    current_pos = positions[0]

    while current_pos != positions[-1]:
        neighbors = []

        # Check right neighbor
        if current_pos[0] + 1 < n and (current_pos[0] + 1, current_pos[1]) in positions:
            neighbors.append((current_pos[0] + 1, current_pos[1]))

        # Check top neighbor
        if current_pos[1] + 1 < n and (current_pos[0], current_pos[1] + 1) in positions:
            neighbors.append((current_pos[0], current_pos[1] + 1))

        # Check top right neighbor if not in the most right column and the most bottom row
        if current_pos[0] + 1 < n and current_pos[1] + 1 < n and (current_pos[0] + 1, current_pos[1] + 1) in positions:
            neighbors.append((current_pos[0] + 1, current_pos[1] + 1))

        # Select the neighbor with the smallest number
        if neighbors:
            next_pos = min(neighbors, key=lambda x: positions.index(x))
            path.append(next_pos)
            current_pos = next_pos
        else:
            break

    return path


def draw_young_diagram_with_path(partition, path, positions):
    # Create a plot with matplotlib
    fig, ax = plt.subplots(figsize=(10, 10))

    max_dim = max(sum(partition), len(partition))  # Get the maximum dimension of the Young diagram

    fontsize = max(6, int(15 * 20 / max_dim))  # Adjust the fontsize based on the size of the diagram

    # Add rectangles for each box in the Young diagram
    for i in (range(len(partition))):
        for j in range(partition[i]):
            ax.add_patch(
                plt.Rectangle((j, i), 1, 1, fill=True, facecolor='lightgrey', edgecolor='black', linewidth=0.5))
            number = positions.index((j, i)) + 1  # Get the box number
            ax.text(j + 0.5, i + 0.5, str(number), ha='center', va='center', color='black', fontsize=fontsize)
    # Draw the deterministic path with arrows
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]
        arrow = patches.FancyArrowPatch((start[0] + 0.5, start[1] + 0.5),
                                        (end[0] + 0.5, end[1] + 0.5),
                                        arrowstyle='->', mutation_scale=20, color='red')
        ax.add_patch(arrow)

    ax.set_xlim([-0.5, max(partition) + 0.5])
    ax.set_ylim([-0.5, len(partition) + 0.5])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


def modify_path_and_positions(original_path, original_positions):
    # Remove the endpoint from the path
    new_path = original_path[:-1]

    # Create a dictionary for faster lookup of position indices
    position_indices = {pos: i for i, pos in enumerate(original_positions)}
    # Shift the positions in the modified path
    modified_positions = original_positions.copy()

    for i in reversed(range(1, len(new_path))):
        modified_positions[position_indices[original_path[i + 1]]] = new_path[i]

    del modified_positions[1]

    return modified_positions


def generate_modified_young_diagram(path, positions):
    # Modify the path and get the adjusted positions
    modified_positions = modify_path_and_positions(path, positions)

    # Determine the new size of each row in the diagram
    row_lengths = {}
    for col, row in modified_positions:
        row_lengths[row] = row_lengths.get(row, 0) + 1

    # Create the partition as a list of row lengths
    partition = [row_lengths.get(i, 0) for i in range(max(row_lengths.keys()) + 1)]

    # Debug prints
    # print("Original Path:", path)
    # print("Original Positions:", positions)
    # print("Modified Positions:", modified_positions)
    # print("Partition:", partition)

    return partition, modified_positions


def calculate_u_values_over_iterations(num_iterations, n):
    def calculate_u_value(endpoint):
        x, y = endpoint
        return (x - y) / math.sqrt(n)

    u_values = []  # To store the u values for each iteration

    for _ in tqdm(range(num_iterations)):
        # Generate and process the original diagram
        young1, position1 = generate_young_diagram(n)
        path1 = build_deterministic_path(position1, n)
        endpoint1 = path1[-1]
        u1 = calculate_u_value(endpoint1)

        # Generate and process the modified diagram
        partition2, position2 = generate_modified_young_diagram(path1, position1)
        path2 = build_deterministic_path(position2, n)
        endpoint2 = path2[-1]
        u2 = calculate_u_value(endpoint2)

        # Store the u values
        u_values.append((u1, u2))
        # print(f"u1: {u1}, u2: {u2}")  # Debugging output
    return u_values


def plot_u_values(u_values, n, num_iterations):
    # Unpack the u values for plotting
    u1_values, u2_values = zip(*u_values)

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(u1_values, u2_values, alpha=0.7)

    # Add titles and labels
    plt.title(f"Distribution of u Values for n = {n}, Iterations = {num_iterations}")
    plt.xlabel("$u_1$")
    plt.ylabel("$u_2$")

    # Add grid for better readability
    plt.grid(True)

    # Show the plot
    plt.show()


def count_close_u_values(u_values, epsilon=0.1):
    close_count = 0
    for u1, u2 in u_values:
        if abs(u1 - u2) <= epsilon:
            close_count += 1
    return close_count


num_iterations = 1000  # Define the number of iterations

n = 100000  # Size of the Young diagram

# Get the u values for multiple iterations
u_values = calculate_u_values_over_iterations(num_iterations, n)
close_count = count_close_u_values(u_values, epsilon=0.1)
print(f"Number of u_values close to the line u1 = u2: {close_count}, and the probability of u_values close to the u1 = u2: {close_count / num_iterations}")
# Plot the u v   alues
plot_u_values(u_values, n, num_iterations)

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import numpy as np
from scipy.optimize import curve_fit
import random


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
    for i in range(len(partition)):
        for j in range(partition[i]):
            ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor='lightgrey', edgecolor='black', linewidth=0.5))
            #number = positions.index((j, i)) + 1  # Get the box number
            #ax.text(j + 0.5, i + 0.5, str(number), ha='center', va='center', color='black', fontsize = fontsize)

    # Draw the deterministic path
    path_x = [p[0] + 0.5 for p in path]  # Adding 0.5 to center the path in the boxes
    path_y = [p[1] + 0.5 for p in path]
    ax.plot(path_x, path_y, color='red', marker='o', markersize=0.001)

    ax.set_xlim([-0.5, max(partition) + 0.5])
    ax.set_ylim([-0.5, len(partition) + 0.5])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


n = 1000  # Number of boxes to add

# Generate Young diagram and track the positions of added boxes
young_diagram1, positions1 = generate_young_diagram(n)

# Build the deterministic path
path1 = build_deterministic_path(positions1, n)

# Visualize the Young diagram and deterministic path
draw_young_diagram_with_path(young_diagram1, path1, positions1)

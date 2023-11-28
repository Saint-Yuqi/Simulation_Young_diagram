import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from scipy.stats import chisquare
import random
from tqdm import tqdm


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


def record_boxes_and_endpoints(n, iterations):
    all_boxes = {}  # To record all boxes that appear
    endpoints = {}  # To record frequency of endpoints

    for _ in range(iterations):
        young_diagram, positions = generate_young_diagram(n)
        path = build_deterministic_path(positions, n)
        endpoint = path[-1]
        endpoints[endpoint] = endpoints.get(endpoint, 0) + 1
        for position in positions:
            all_boxes[position] = True  # Simply mark the position as seen

    return all_boxes, endpoints


def draw_combined_young_diagram(all_boxes, endpoints):
    fig, ax = plt.subplots()

    max_val = max(endpoints.values(), default=0)
    colormap = plt.get_cmap('Greens')
    norm = colors.Normalize(0, max_val)

    max_x = max([x for x, y in all_boxes.keys()], default=0)  # Maximum x-coordinate
    max_y = max([y for x, y in all_boxes.keys()], default=0)  # Maximum y-coordinate

    for (x, y), _ in tqdm(all_boxes.items()):
        freq = endpoints.get((x, y), 0)  # Use 0 if the box wasn't an endpoint
        color = 'white' if freq == 0 else colormap(norm(freq))
        ax.add_patch(plt.Rectangle((x, y), 1, 1, fill=True, facecolor=color, edgecolor='black', linewidth=0.5))

    ax.set_xlim([-0.5, max_x + 1.5])
    ax.set_ylim([-0.5, max_y + 1.5])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])
    ax.margins(0.05)  # Adding 5% margin around the graph
    plt.show()


def draw_young_diagram_with_path(partition, path, positions):
    # Create a plot with matplotlib
    fig, ax = plt.subplots(figsize=(10, 10))

    max_dim = max(sum(partition), len(partition))  # Get the maximum dimension of the Young diagram

    # fontsize = max(6, int(15 * 20 / max_dim))  # Adjust the fontsize based on the size of the diagram

    # Add rectangles for each box in the Young diagram
    for i in tqdm(range(len(partition))):
        for j in range(partition[i]):
            ax.add_patch(
                plt.Rectangle((j, i), 1, 1, fill=True, facecolor='lightgrey', edgecolor='black', linewidth=0.5))
            # number = positions.index((j, i)) + 1  # Get the box number
            # ax.text(j + 0.5, i + 0.5, str(number), ha='center', va='center', color='black', fontsize = fontsize)

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


def draw_circle_and_sectors(ax, all_boxes):
    # Radius of the circle
    r = max(x for (x, y) in all_boxes.keys()) + 4
    # The upper right corner
    ur_corner_x = max(x for (x, y) in all_boxes.keys())
    ur_corner_y = max(y for (x, y) in all_boxes.keys())
    # Center of the circle
    circle_center = (ur_corner_x + 1, ur_corner_y + 1)

    # Draw the circle
    circle = plt.Circle(circle_center, r, color='blue', fill=False)
    ax.add_artist(circle)

    # Calculate and draw the sectors (approximate with lines for visualization)
    for i in tqdm(range(0, 5)):
        angle = 2 * np.pi + (i / 5) * (np.pi / 2)  # Divide the quarter circle into 5 parts
        x = circle_center[0] - r * np.cos(angle)
        y = circle_center[1] - r * np.sin(angle)
        ax.plot([circle_center[0], x], [circle_center[1], y], color='blue')


def draw_combined_young_diagram_with_circle(all_boxes, endpoints):
    fig, ax = plt.subplots()

    max_val = max(endpoints.values(), default=1)
    colormap = plt.get_cmap('Greens')
    norm = colors.Normalize(0, max_val)
    max_x = max([x for x, y in all_boxes.keys()], default=0)  # Maximum x-coordinate
    max_y = max([y for x, y in all_boxes.keys()], default=0)  # Maximum y-coordinate

    # Drawing the boxes of the Young diagram
    for (x, y), _ in tqdm(all_boxes.items()):
        freq = endpoints.get((x, y), 0)
        color = 'white' if freq == 0 else colormap(norm(freq))
        ax.add_patch(plt.Rectangle((x, y), 1, 1, fill=True, facecolor=color, edgecolor='black', linewidth=0.5))

    # After drawing the Young diagram, call the function to draw the circle and sectors
    draw_circle_and_sectors(ax, all_boxes)

    # Set the limits based on the Young diagram dimensions
    ax.set_xlim([-0.5, max_x + 1.5])
    ax.set_ylim([-0.5, max_y + 1.5])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


def count_endpoints_in_sectors(n, iterations,k):
    sector_counts = [0] * 5
    sector_angle = (np.pi / 2) / 5  # Each sector angle in the bottom-left quarter circle
    all_boxes, endpoints = record_boxes_and_endpoints(n, iterations)
    r = max(x for (x, y) in all_boxes1.keys()) + k
    # The upper right corner
    ur_corner_x = max(x for (x, y) in all_boxes.keys())
    ur_corner_y = max(y for (x, y) in all_boxes.keys())
    # Center of the circle
    circle_center = (ur_corner_x + 1, ur_corner_y + 1)

    for endpoint, count in endpoints.items():
        dx = endpoint[0] - circle_center[0]
        dy = endpoint[1] - circle_center[1]
        distance = np.sqrt(dx**2 + dy**2)

        # Ensure the endpoint is within the circle
        if distance <= r:
            angle = np.arctan2(dy, dx)

            # Adjust angle for the bottom-left quarter
            if angle < 0:
                angle += 2 * np.pi

            # Check if the endpoint falls within the bottom-left quarter
            if np.pi <= angle < 3 * np.pi / 2:
                # Calculate the sector index
                sector_index = int((angle - np.pi) / sector_angle)
                sector_counts[sector_index] += count

    return sector_counts




def test_uniform_distribution(sector_counts):
    chi_square, p_value = chisquare(sector_counts)
    return chi_square, p_value


n2 = 100
iterations2 = 100

# Record the boxes and endpoints
all_boxes1, endpoints1 = record_boxes_and_endpoints(n2, iterations2)
# Assuming endpoints is a dictionary with endpoints as keys


for k in range(0, 10):
    sector_counts = count_endpoints_in_sectors(n2, iterations2,k)
    print("Endpoints in each sector:", sector_counts)
    # Perform the chi-squared test
    chi_square_statistic, p_value = test_uniform_distribution(sector_counts)

    print(f"Chi-squared Statistic: {chi_square_statistic}, P-value: {p_value}")

    # If the p-value is less than 0.05, we reject the null hypothesis of uniform distribution
    if p_value < 0.05:
        print("The distribution of endpoints among the sectors is not uniform.")
    else:
        print("The distribution of endpoints among the sectors is uniform.")

# Draw the combined diagram with the circle and sectors
# draw_combined_young_diagram_with_circle(all_boxes1, endpoints1)



# n1 = 100
# iterations1 = 100
# # partition1, positions1 = generate_young_diagram(n1)
# # path1 = build_deterministic_path(positions1, n1)
# # draw_young_diagram_with_path(partition1, path1, positions1)
# all_boxes1, endpoints1 = record_boxes_and_endpoints(n1, iterations1)
# draw_combined_young_diagram(all_boxes1, endpoints1)
#

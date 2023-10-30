import matplotlib.pyplot as plt
import matplotlib.colors as colors
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


def draw_combined_young_diagram(all_boxes, endpoints, n):
    fig, ax = plt.subplots()

    max_val = max(endpoints.values(), default=0)
    colormap = plt.get_cmap('Greens')
    norm = colors.Normalize(0, max_val)

    max_x = max([x for x, y in all_boxes.keys()], default=0)  # Maximum x-coordinate
    max_y = max([y for x, y in all_boxes.keys()], default=0)  # Maximum y-coordinate

    for (x, y), _ in all_boxes.items():
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

    fontsize = max(6, int(15 * 20 / max_dim))  # Adjust the fontsize based on the size of the diagram

    # Add rectangles for each box in the Young diagram
    for i in range(len(partition)):
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


n = 100
iterations = 1000

all_boxes, endpoints = record_boxes_and_endpoints(n, iterations)
draw_combined_young_diagram(all_boxes, endpoints, n)

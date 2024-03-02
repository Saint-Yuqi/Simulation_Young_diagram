import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.transforms


def generate_young_diagram(N):
    # Initialize the particles and diagram
    particles = {i: 0 for i in range(-N + 1, 1)}  # Particles from -N+1 to 0
    diagram = []

    for _ in range(N):
        # Available moves are where the particle to the right is higher or non-existent
        available_moves = [pos for pos in particles if pos + 1 not in particles or particles[pos + 1] > particles[pos]]

        # If no available moves, break
        if not available_moves:
            break

        # Move a random particle
        move_from = random.choice(available_moves)
        move_to = move_from + 1
        particles[move_to] = particles[move_from] + 1  # Increase the height
        diagram.append((move_to, particles[move_to]))  # Add new box position

        # Remove the particle that moved
        del particles[move_from]

    return diagram


def draw_young_diagram(diagram, N):
    fig, ax = plt.subplots()

    # Define transformation for rotation
    t = plt.gca().transData
    tr = matplotlib.transforms.Affine2D().rotate_deg_around(0, 0, 45)

    # Plot boxes
    for x, y in diagram:
        if y >= abs(x):  # Only plot boxes within the boundary
            # Create a rectangle with the transformation
            rect = plt.Rectangle((x - 0.5, y - 0.5), 1, 1, fill=True, edgecolor='black', transform=tr + t)
            ax.add_patch(rect)

    # Set plot limits
    ax.set_xlim([-N, N])
    ax.set_ylim([0, 2 * N])  # Extend the y-limit to accommodate the rotation
    ax.set_aspect('equal')

    # Draw boundary line y = |x|
    boundary_x = np.linspace(-N, N, 1000)
    boundary_y = abs(boundary_x)
    ax.plot(boundary_x, boundary_y, color='red', linestyle='--')

    # Apply rotation to the plot
    plt.gca().set_transform(tr + t)

    # Invert the y-axis to match the Young diagram orientation
    plt.gca().invert_yaxis()

    plt.show()


# Number of steps (boxes to add)
N = 10
young_diagram = generate_young_diagram(N)
draw_young_diagram(young_diagram, N)

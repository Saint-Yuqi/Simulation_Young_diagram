# import matplotlib.pyplot as plt
# import numpy as np
# import random
#
#
# def generate_young_diagram(N):
#     # Initialize the particles
#     particles = set(range(-N + 1, 1))
#     # Initialize the diagram as a dictionary with keys as the diagonal levels
#     diagram = {i: 0 for i in range(-N + 1, N)}
#
#     for _ in range(N):
#         # Choose a random particle that can move (i.e., it is not blocked by the y = |x| line)
#         particle = random.choice(sorted(particles))
#
#         # Move the particle diagonally up and to the right
#         diagram[particle] += 1
#         particles.remove(particle)
#         if particle + 1 < N:
#             particles.add(particle + 1)
#
#     return diagram
#
#
# def draw_young_diagram(diagram, N):
#     fig, ax = plt.subplots()
#
#     # Draw the Young diagram
#     for diag_level, height in diagram.items():
#         for i in range(height):
#             # Calculate the center of the box
#             center_x = diag_level
#             center_y = N - 1 - i
#             # Draw a rotated square (diamond) to represent the box
#             diamond = plt.Polygon([
#                 (center_x - 0.5, center_y),
#                 (center_x, center_y - 0.5),
#                 (center_x + 0.5, center_y),
#                 (center_x, center_y + 0.5)
#             ], closed=True, fill=True, edgecolor='black')
#             ax.add_patch(diamond)
#
#     # Draw the boundary line y = |x|
#     boundary_x = np.linspace(-N, N, 400)
#     ax.plot(boundary_x, abs(boundary_x), 'r--')
#
#     # Set the limits and aspect of the plot
#     ax.set_xlim(-N, N)
#     ax.set_ylim(0, 2 * N)
#     ax.set_aspect('equal')
#
#     # Invert the y-axis to match the Young diagram orientation
#     ax.invert_yaxis()
#     plt.show()
#
#
# # Number of steps (boxes to add)
# N = 10
# young_diagram = generate_young_diagram(N)
# draw_young_diagram(young_diagram, N)

import matplotlib.pyplot as plt
import random

def draw_young_diagram(partition):
    # Calculate the total number of boxes in the Young diagram
    n = sum(partition)

    # Create a 2D array representing the Young diagram
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]
    label = 1
    # Label each box in the Young diagram with a unique number
    for i in range(len(partition)):
        for j in range(partition[i]):
            diagram[i][j] = label
            label += 1

    # Create a plot with matplotlib
    fig, ax = plt.subplots()

    # Add rectangles for each box in the Young diagram
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            ax.add_patch(plt.Rectangle((j, len(diagram) - i - 1), 1, 1, fill=False))
            #ax.text(j + 0.5, len(diagram) - i - 0.5, str(diagram[i][j]), ha='center', va='center')

    # Set the x and y limits of the plot
    ax.set_xlim([-1, len(diagram[0]) + 1])
    ax.set_ylim([-1, len(diagram) + 1])

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')

    # Turn off axis labels
    ax.axis('off')

    # Show the plot
    plt.show()

def add_box(young_diagram):
    # Get the length of the current Young diagram
    n = len(young_diagram)
    # Store all the possibilities of the Young diagram
    choices = []

    # Add a box to an existing row in the Young diagram
    for i in range(n):
        if i == 0 or young_diagram[i - 1] > young_diagram[i]:
            new_diagram = young_diagram.copy()
            new_diagram[i] += 1
            choices.append(new_diagram)

    # Add a new row to the Young diagram
    choices.append(young_diagram + [1])

    # Choose one of the possibilities uniformly at random
    return random.choice(choices)

def generate_young_diagram(n):
    # Generate a Young diagram with n boxes

    young_diagram = [1]
    for _ in range(n - 1):
        young_diagram = add_box(young_diagram)
    return young_diagram

def simulation_young_diagram(n):

    young_diagram = [1]
    for _ in range(n - 1):
        print(young_diagram)
        #draw_young_diagram(young_diagram)
        young_diagram = add_box(young_diagram)
    return young_diagram


n = 10
simulation_young_diagram(n)


# n = 4  # Number of boxes to add to the Young diagram
# young_diagram = generate_young_diagram(n)
# print(young_diagram)
#
# # Draw the Young diagram
# draw_young_diagram(young_diagram)

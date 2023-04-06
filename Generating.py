import matplotlib.pyplot as plt
import random


def draw_young_diagram(partition):
    n = sum(partition)

    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]

    for i in range(len(partition)):
        for j in range(partition[i]):
            diagram[i][j] = n
            n -= 1

    [fig, ax] = plt.subplots()

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            ax.add_patch(plt.Rectangle((j, len(diagram) - i - 1), 1, 1, fill=False))
            if diagram[i][j] != 0:
                ax.text(j + 0.5, len(diagram) - i - 0.5, str(diagram[i][j]), ha='center', va='center')
    ax.set_xlim([-0.5, len(diagram[0]) - 0.5])
    ax.set_ylim([-0.5, len(diagram) - 0.5])
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

def add_box(young_diagram):
    n = len(young_diagram)
    choices = []

    # Add a box to an existing row
    for i in range(n):
        if i == 0 or young_diagram[i - 1] > young_diagram[i]:
            new_diagram = young_diagram.copy()
            new_diagram[i] += 1
            choices.append(new_diagram)

    # Add a new row
    choices.append(young_diagram + [1])

    # Choose one of the possibilities uniformly at random
    return random.choice(choices)

def generate_young_diagram(n):
    young_diagram = [1]
    for _ in range(n - 1):
        young_diagram = add_box(young_diagram)
    return young_diagram

# Example usage:
n = 10  # Number of boxes to add to the Young diagram
young_diagram = generate_young_diagram(n)
print(young_diagram)

draw_young_diagram(young_diagram)
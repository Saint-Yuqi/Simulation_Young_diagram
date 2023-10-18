import matplotlib.pyplot as plt
import random
from IPython.display import clear_output
import time


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


def simulation_young_diagram(n, delay=0.1):
    label = 1
    young_diagram = [1]
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, fill=False))
    ax.text(0.5, 0.5, str(label), ha='center', va='center')
    for _ in range(n - 1):
        old_diagram = young_diagram.copy()
        ax.set_xlim([0, n])
        ax.set_ylim([0, n])
        # Set the aspect ratio of the plot to be equal
        ax.set_aspect('equal')
        plt.show()
        time.sleep(delay)
        clear_output(wait=True)
        young_diagram = add_box(young_diagram)
        label += 1
        if (len(young_diagram) - len(old_diagram) == 1):
            ax.add_patch(plt.Rectangle((0, len(old_diagram)), 1, 1, fill=False))
            ax.text(0.5, len(old_diagram) + 0.5, str(label), ha='center', va='center')
            continue

        for i in range(len(young_diagram)):
            if (young_diagram[i] - old_diagram[i] == 1):
                ax.add_patch(plt.Rectangle((old_diagram[i] , i), 1, 1, fill=False))
                ax.text(old_diagram[i] + 0.5, i + 0.5, str(label), ha='center', va='center')
                break

    # Set the x and y limits of the plot
    ax.set_xlim([0, young_diagram[0] + 1])
    ax.set_ylim([0, len(young_diagram) + 1])
    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')
    # Turn off axis labels
    #ax.axis('off')
    # Show the plot
    plt.show()


n = 10
partition = [2,1,1,1]

simulation_young_diagram(n,delay=0.1)

import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

def add_box(young_diagram):
    n = len(young_diagram)
    choices = []
    for i in range(n):
        if i == 0 or young_diagram[i - 1] > young_diagram[i]:
            new_diagram = young_diagram.copy()
            new_diagram[i] += 1
            choices.append(new_diagram)

    choices.append(young_diagram + [1])

    return random.choice(choices)

def update(frame, young_diagram, ax):
    ax.clear()
    old_diagram = young_diagram.copy()
    young_diagram[:] = add_box(young_diagram)
    label = frame + 2

    for i in range(len(young_diagram)):
        for j in range(young_diagram[i]):
            ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False))
            if old_diagram[i] == j:
                ax.text(j + 0.5, i + 0.5, str(label), ha='center', va='center')
            elif i < len(old_diagram) and old_diagram[i] > j:
                ax.text(j + 0.5, i + 0.5, str(j + 1), ha='center', va='center')

    ax.set_xlim([0, young_diagram[0] + 1])
    ax.set_ylim([0, len(young_diagram) + 1])
    ax.set_aspect('equal')
    ax.axis('off')

def simulation_young_diagram(n):
    young_diagram = [1]
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, fill=False))
    ax.text(0.5, 0.5, '1', ha='center', va='center')

    ani = FuncAnimation(fig, update, frames=range(n - 1), fargs=(young_diagram, ax), interval=500, repeat=False)

    plt.show()

n = 10
simulation_young_diagram(n)

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import random
import matplotlib.cm as cm
import numpy as np


def draw_young_diagram(partition):
    # Create a 2D array representing the Young diagram
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]
    # label = 1
    # Label each box in the Young diagram with a unique number
    # for i in range(len(partition)):
    #     for j in range(partition[i]):
    #         diagram[i][j] = label
    #         label += 1

    # Create a plot with matplotlib
    fig, ax = plt.subplots()

    # Add rectangles for each box in the Young diagram
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            ax.add_patch(plt.Rectangle((j, len(diagram) - i - 1), 1, 1, fill=False))
            # ax.text(j + 0.5, len(diagram) - i - 0.5, str(diagram[i][j]), ha='center', va='center')

    # Set the x and y limits of the plot
    ax.set_xlim([-1, len(diagram[0]) + 1])
    ax.set_ylim([-1, len(diagram) + 1])

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')

    # # Turn off axis labels
    # ax.axis('off')

    # Show the plot
    plt.show()


def draw_young_diagram_log_green_level(partition, box_counts={}, n=1, save_plot=False, filename=''):
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]
    fig, ax = plt.subplots(figsize=(10, 10))

    if box_counts:
        max_freq = max(box_counts.values())
        min_freq = min(box_counts.values())
    else:
        max_freq = 1
        min_freq = 0

    # Normalize the frequencies using the range of frequencies
    normalized_box_counts = {key: (value - min_freq) / (max_freq - min_freq) for key, value in box_counts.items()}

    # Use the modified 'Greens' colormap
    cmap = cm.get_cmap('Greens')
    colormap = colors.LinearSegmentedColormap.from_list("custom_colormap",
                                                        [cmap(1), cmap(0.6), cmap(0.4), cmap(0)])

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            key = (j, i)
            if key in normalized_box_counts:
                freq = normalized_box_counts[key]
                color = colormap(freq)
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='black', linewidth=0.5))
    ax.set_xlim([0, len(diagram[0]) + 10])
    ax.set_ylim([0, len(diagram) + 10])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    if save_plot:
        plt.savefig(filename)

    plt.show()


def draw_young_diagram_green_level(partition, box_counts={}, n=1):
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]
    fig, ax = plt.subplots(figsize=(10, 10))

    if box_counts:
        max_freq = max(box_counts.values())
    else:
        max_freq = 1

    normalized_box_counts = {key: value / max_freq for key, value in box_counts.items()}

    # Create a custom inverted green colormap
    cmap = cm.get_cmap('Greens')
    colormap = colors.LinearSegmentedColormap.from_list("custom_colormap",
                                                        [cmap(1), cmap(0.6), cmap(0.4), cmap(0)])

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            key = (j, i)
            if key in normalized_box_counts:
                freq = normalized_box_counts[key]
                color = colormap(freq)
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='black', linewidth=0.5))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black', linewidth=0.5))

    ax.set_xlim([0, len(diagram[0]) + 10])
    ax.set_ylim([0, len(diagram) + 10])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


def draw_young_diagram_light_green_level(partition, box_counts={}, n=1, save_plot=False, filename=''):
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]
    fig, ax = plt.subplots(figsize=(10, 10))

    if box_counts:
        max_freq = max(box_counts.values())
        min_freq = min(box_counts.values())
    else:
        max_freq = 1
        min_freq = 0

    # Normalize the frequencies using the range of frequencies
    # Subtract the normalized frequency from 1 to reverse the colormap
    normalized_box_counts = {key: 1 - (value - min_freq) / (max_freq - min_freq) for key, value in box_counts.items()}

    cmap = cm.get_cmap('Greens')

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            key = (j, i)
            if key in normalized_box_counts:
                freq = normalized_box_counts[key]
                color = cmap(freq)
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='black', linewidth=0.5))

    ax.set_xlim([0, len(diagram[0]) + 10])
    ax.set_ylim([0, len(diagram) + 10])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    if save_plot:
        plt.savefig(filename)

    plt.show()



def draw_young_diagram_gray_level(partition, box_counts={}, n=1):
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]
    fig, ax = plt.subplots(figsize=(10, 10))

    if box_counts:
        max_freq = max(box_counts.values())
    else:
        max_freq = 1

    normalized_box_counts = {key: value / max_freq for key, value in box_counts.items()}

    # Create a custom green colormap
    cmap = cm.get_cmap('Greens')
    colormap = colors.LinearSegmentedColormap.from_list("custom_colormap",
                                                        [cmap(0), cmap(0.4), cmap(0.6), cmap(1)])

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            key = (j, i)
            if key in normalized_box_counts:
                freq = normalized_box_counts[key]
                color = colormap(freq)

                # Reduce the box edge width
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='black', linewidth=0.5))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black', linewidth=0.5))

    ax.set_xlim([0, len(diagram[0]) + 10])
    ax.set_ylim([0, len(diagram) + 10])
    ax.set_aspect('equal')

    # Remove axis labels and ticks
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


def draw_young_diagram_greens_level(partition, box_counts={}, n=1):
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]
    fig, ax = plt.subplots(figsize=(10, 10))

    if box_counts:
        max_freq = max(box_counts.values())
        min_freq = min(box_counts.values())
    else:
        max_freq = 1
        min_freq = 0

    # Normalize the frequencies using the range of frequencies
    normalized_box_counts = {key: (value - min_freq) / (max_freq - min_freq) for key, value in box_counts.items()}

    # Create a custom inverted green colormap
    cmap = cm.get_cmap('Greens_r')
    colormap = colors.LinearSegmentedColormap.from_list("custom_colormap",
                                                        [cmap(0), cmap(0.4), cmap(0.6), cmap(1)])

    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            key = (j, i)
            if key in normalized_box_counts:
                freq = normalized_box_counts[key]
                color = colormap(freq)
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='white', linewidth=0.5))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black', linewidth=0.5))

    ax.set_xlim([0, len(diagram[0]) + 10])
    ax.set_ylim([0, len(diagram) + 10])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

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


def count_boxes(young_diagram, box_counts={}):
    for i in range(len(young_diagram)):
        for j in range(young_diagram[i]):
            key = (j, i)
            box_counts[key] = box_counts.get(key, 0) + 1
    return box_counts


def generate_young_diagram(n):
    # Generate a Young diagram with n boxes

    young_diagram = [1]
    for _ in range(n - 1):
        young_diagram = add_box(young_diagram)
    return young_diagram


def simulation_young_diagram_partition(n):
    young_diagram = [1]
    i = 0
    for _ in range(n - 1):
        print(young_diagram)
        if i < n - 2:
            input("Press Enter to continue...")
            i += 1
        else:
            print("The completed Young diagram")
        young_diagram = add_box(young_diagram)
    return young_diagram


def simulation_young_diagram_step(n):
    young_diagram = [1]
    for _ in range(n - 1):
        draw_young_diagram(young_diagram)
        young_diagram = add_box(young_diagram)
    return young_diagram


# def animation_Young_diagram(n):
def simulation_young_diagram(n):
    label = 1
    young_diagram = [1]
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), 0.1, 0.1, fill=False))
    # ax.text(0.5, 0.5, str(label), ha='center', va='center')
    for _ in range(n - 1):
        old_diagram = young_diagram.copy()
        young_diagram = add_box(young_diagram)
        label += 1
        if len(young_diagram) - len(old_diagram) == 1:
            ax.add_patch(plt.Rectangle((0, len(old_diagram)), 0.1, 0.1, fill=False))
            # ax.text(0.5, len(old_diagram) + 0.5, str(label), ha='center', va='center')
            continue

        for i in range(len(young_diagram)):
            if young_diagram[i] - old_diagram[i] == 1:
                ax.add_patch(plt.Rectangle((old_diagram[i], i), 0.1, 0.1, fill=False))
                # ax.text(old_diagram[i] + 0.5, i + 0.5, str(label), ha='center', va='center')
                break

        # Set the x and y limits of the plot
    ax.set_xlim([-1, young_diagram[0] + 1])
    ax.set_ylim([-1, len(young_diagram) + 1])

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')

    # Turn off axis labels
    ax.axis('off')

    # Show the plot
    plt.show()


def simulation_young_diagram(n):
    label = 1
    young_diagram = [1]
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), 0.1, 0.1, fill=False))
    # ax.text(0.5, 0.5, str(label), ha='center', va='center')
    for _ in range(n - 1):
        old_diagram = young_diagram.copy()
        young_diagram = add_box(young_diagram)
        label += 1
        if (len(young_diagram) - len(old_diagram) == 1):
            ax.add_patch(plt.Rectangle((0, len(old_diagram)), 0.1, 0.1, fill=False))
            # ax.text(0.5, len(old_diagram) + 0.5, str(label), ha='center', va='center')
            continue

        for i in range(len(young_diagram)):
            if (young_diagram[i] - old_diagram[i] == 1):
                ax.add_patch(plt.Rectangle((old_diagram[i], i), 0.1, 0.1, fill=False))
                # ax.text(old_diagram[i] + 0.5, i + 0.5, str(label), ha='center', va='center')
                break

        # Set the x and y limits of the plot
    ax.set_xlim([-1, young_diagram[0] + 1])
    ax.set_ylim([-1, len(young_diagram) + 1])

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')

    # Turn off axis labels
    ax.axis('off')

    # Show the plot
    plt.show()


def final_young_diagram(n, t):
    final_diagram = []
    box_counts = {}
    for _ in range(n):
        young_diagram = generate_young_diagram(t)

        if len(final_diagram) < len(young_diagram):
            final_diagram += [0] * (len(young_diagram) - len(final_diagram))
        elif len(final_diagram) > len(young_diagram):
            young_diagram += [0] * (len(final_diagram) - len(young_diagram))

        final_diagram = [max(x, y) for x, y in zip(final_diagram, young_diagram)]
        box_counts = count_boxes(final_diagram, box_counts)
    print(box_counts)
    draw_young_diagram_light_green_level(final_diagram,box_counts, n)
    # draw_young_diagram_light_green_level(final_diagram, box_counts, n)
    # draw_young_diagram_gray_level(final_diagram, box_counts, n)
    return final_diagram


n = 100
t = 100

final_young_diagram(n, t)
# simulation_young_diagram_step(n)
# n = 4  # Number of boxes to add to the Young diagram
# young_diagram = generate_young_diagram(n)
# print(young_diagram)
#
# # Draw the Young diagram
# draw_young_diagram(young_diagram)

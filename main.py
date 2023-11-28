import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import numpy as np
from scipy.optimize import curve_fit
import random


def draw_young_diagram(partition):
    # Create a 2D array representing the Young diagram
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]

    # Create a plot with matplotlib
    fig, ax = plt.subplots()

    # Add rectangles for each box in the Young diagram
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False))

    # Set the x and y limits of the plot
    ax.set_xlim([-1, len(diagram[0]) + 10])
    ax.set_ylim([-1, len(diagram) + 10])

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')

    # Show the plot
    plt.show()

def draw_young_diagram_gray_level(partition, box_counts = {}, n = 1, save_plot=False, filename=''):
    # Create a 2D array representing the Young diagram
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]

    # Create a plot with matplotlib
    fig, ax = plt.subplots(figsize=(10, 10))

    # Add rectangles for each box in the Young diagram
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            key = (j, i)
            if key in box_counts:
                freq = box_counts[key]
                gray_level = 1 - freq / n
                color = (gray_level, gray_level, gray_level)
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='white',  linewidth=0.5))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='black',  linewidth=0.5))

    # Set the x and y limits of the plot
    ax.set_xlim([0, len(diagram[0]) + 10])
    ax.set_ylim([0, len(diagram) + 10])

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')

    # Remove axis labels and ticks
    ax.set_xticks([])
    ax.set_yticks([])

    if save_plot:
        plt.savefig(filename)
    # Show the plot
    plt.show()
def draw_young_diagram_normalize_gray_level(partition, box_counts={}, n=1, save_plot=False, filename=''):
    diagram = [[0 for j in range(partition[i])] for i in range(len(partition))]

    # Increase the figure size
    fig, ax = plt.subplots(figsize=(10, 10))

    if box_counts:
        max_freq = max(box_counts.values())
    else:
        max_freq = 1

    normalized_box_counts = {key: value / max_freq for key, value in box_counts.items()}

    cmap = cm.get_cmap('gray')
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

    if save_plot:
        plt.savefig(filename)

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

def draw_young_diagram_dark_green_level(partition, box_counts={}, n=1, save_plot=False, filename=''):
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

    cmap = cm.get_cmap('Greens')  # Use the original 'Greens' colormap

    # Create a custom colormap with 100 segments
    colormap = colors.LinearSegmentedColormap.from_list(
        "custom_colormap",
        [cmap(0.2)] + [cmap(i / 100) for i in range(20, 101)]
    )


    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            key = (j, i)
            if key in normalized_box_counts:
                freq = normalized_box_counts[key]
                color = colormap(freq)
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, facecolor=color, edgecolor='white', linewidth=0.5))
            else:
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='white', linewidth=0.5))

    ax.set_xlim([0, len(diagram[0]) + 10])
    ax.set_ylim([0, len(diagram) + 10])
    ax.set_aspect('equal')

    ax.set_xticks([])
    ax.set_yticks([])

    if save_plot:
        plt.savefig(filename)

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

def generate_young_diagram(n, young_diagram = [1]):
    # Generate a Young diagram with n boxes
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

def simulation_young_diagram(n, young_diagram = [1], label = 1):
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), 0.1, 0.1, fill=False))
    # ax.text(0.5, 0.5, str(label), ha='center', va='center')
    for _ in range(n - 1):
        old_diagram = young_diagram.copy()
        young_diagram = add_box(young_diagram)
        label += 1
        if (len(young_diagram) - len(old_diagram) == 1):
            ax.add_patch(plt.Rectangle((0, len(old_diagram)), 0.1, 0.1, fill=False))
            continue

        for i in range(len(young_diagram)):
            if (young_diagram[i] - old_diagram[i] == 1):
                ax.add_patch(plt.Rectangle((old_diagram[i], i), 0.1, 0.1, fill=False))
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
        #print(box_counts)
    draw_young_diagram_light_green_level(final_diagram, box_counts, n, save_plot=True, filename= '/Users/yang/PycharmProjects/Young_diagram/light_green_1.png')
    #draw_young_diagram_gray_level(final_diagram, box_counts, n)
    #draw_young_diagram_dark_green_level(final_diagram, box_counts, n, save_plot=True, filename= '/Users/yang/PycharmProjects/Young_diagram/dark_green_3.png')

    return final_diagram


def draw_upper_bound_curve(young_diagram):
    # Get the maximum value from the diagram
    max_value = max(young_diagram)

    # Create a list that starts at max_value and decreases as we move along the x-axis
    upper_bound_curve = [max_value - i / len(young_diagram) for i in range(len(young_diagram))]

    # Plot the curve
    plt.plot(upper_bound_curve, color='red')
    plt.title('Upper Bound Curve of Young Diagram')
    plt.xlabel('Row index')
    plt.ylabel('Row length')


n = 1000
t = 100
final_young_diagram(n, t)

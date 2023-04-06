import random

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
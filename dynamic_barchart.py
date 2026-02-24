import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Categories
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
num_categories = len(categories)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_ylim(0, 50)  # Set y-axis limits
bars = ax.bar(categories, [0]*num_categories, color='skyblue', edgecolor='black')

# Animation function
def update(frame):
    # Generate new random values for each category
    values = np.random.randint(0, 50, num_categories)
    for bar, val in zip(bars, values):
        bar.set_height(val)
    ax.set_title(f"Dynamic Bar Chart - Frame {frame}")
    return bars

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=500, blit=True)

plt.show()

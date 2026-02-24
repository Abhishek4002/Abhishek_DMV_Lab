import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Initial data
data = np.random.randint(0, 100, 100)

# Initial histogram
bars = ax.hist(data, bins=10, color='skyblue', edgecolor='black')[2]

# Animation update function
def update(frame):
    ax.clear()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    new_data = np.random.randint(0, 100, 100)
    ax.hist(new_data, bins=10, color='skyblue', edgecolor='black')
    
    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

# Create animation
ani = FuncAnimation(fig, update, interval=500)

plt.show()
                
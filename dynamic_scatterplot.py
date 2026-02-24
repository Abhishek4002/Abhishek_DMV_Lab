import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Number of points
num_points = 30

# Initial random positions
x = np.random.rand(num_points) * 10
y = np.random.rand(num_points) * 10

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
scat = ax.scatter(x, y, s=100, c=np.random.rand(num_points), cmap='viridis', edgecolor='black')

plt.title("Dynamic Scatter Plot")

# Animation function
def update(frame):
    # Move points randomly
    global x, y
    x += (np.random.rand(num_points) - 0.5) * 0.5
    y += (np.random.rand(num_points) - 0.5) * 0.5
    
    # Keep points within the axes
    x = np.clip(x, 0, 10)
    y = np.clip(y, 0, 10)
    
    # Update scatter plot data
    scat.set_offsets(np.c_[x, y])
    scat.set_array(np.random.rand(num_points))  # change colors dynamically
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=100, blit=True)

plt.show()

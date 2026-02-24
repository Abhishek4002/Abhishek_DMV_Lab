import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

x_data = []
y_data = []

line, = ax.plot([], [], color='blue', linewidth=2)

# Animation function
def update(frame):
    x_data.append(frame * 0.1)
    y_data.append(np.sin(frame * 0.1))
    
    line.set_data(x_data, y_data)
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.title("Dynamic Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()

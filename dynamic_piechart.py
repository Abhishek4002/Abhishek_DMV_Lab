import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Categories
labels = ['Python', 'Java', 'C++', 'JavaScript']
num_labels = len(labels)

# Create figure and axis
fig, ax = plt.subplots()
ax.axis('equal')  # keeps pie chart perfectly circular

# Initial pie chart
data = np.random.randint(10, 50, num_labels)
wedges, texts, autotexts = ax.pie(
    data, labels=labels, autopct='%1.1f%%', startangle=90
)

# Animation update function
def update(frame):
    ax.clear()
    ax.axis('equal')  # maintain circular shape
    data = np.random.randint(10, 50, num_labels)
    ax.pie(
        data, labels=labels, autopct='%1.1f%%', startangle=90,
        colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
    )
    ax.set_title(f"Dynamic Pie Chart - Frame {frame}")

# Create animation
ani = FuncAnimation(fig, update, frames=50, interval=1000)

plt.show()

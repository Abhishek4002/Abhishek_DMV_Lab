import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_aspect('equal')  # ensures the circle stays perfectly round

# Create the circle
circle = plt.Circle((0, 2.5), 0.3, color='blue')
ax.add_patch(circle)

# Animation function
def update(frame):
    x = frame * 0.1
    circle.center = (x % 10, 2.5)  # moves along X-axis and resets
    return circle,

# Create animation
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.title("Animated Circle Moving Along X-Axis")
plt.show()

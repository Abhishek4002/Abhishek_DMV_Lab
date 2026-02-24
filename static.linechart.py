import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue', linewidth=2, label='sin(x)')

plt.title("Static Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.random.rand(50) * 10  # 50 random x-values from 0 to 10
y = np.random.rand(50) * 10  # 50 random y-values from 0 to 10
colors = np.random.rand(50)   # Random colors for each point
sizes = np.random.randint(50, 300, size=50)  # Random sizes for points

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis', edgecolor='black')

plt.title("Static Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.colorbar(label='Color Scale')  # Show color scale

plt.show()

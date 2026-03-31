import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(0)

# Create negatively correlated data
x = np.random.rand(50)
y = -x + np.random.normal(0, 0.1, 50)

# Create clusters
cluster1_x = np.random.normal(0.2, 0.05, 20)
cluster1_y = np.random.normal(0.8, 0.05, 20)

cluster2_x = np.random.normal(0.8, 0.05, 20)
cluster2_y = np.random.normal(0.2, 0.05, 20)

# Combine all data
x = np.concatenate([x, cluster1_x, cluster2_x])
y = np.concatenate([y, cluster1_y, cluster2_y])

# Add outliers
x = np.append(x, [0.1, 0.9])
y = np.append(y, [2, -1])

# Plot
plt.scatter(x, y)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Negative Correlation, Clusters, and Outliers")

plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate random data (example dataset)
data = np.random.normal(loc=50, scale=10, size=1000)

# Create histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

plt.title("Static Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

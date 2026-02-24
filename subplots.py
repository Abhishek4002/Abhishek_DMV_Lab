import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

# Create subplots (1 row, 2 columns)
plt.figure(figsize=(10,4))

# Subplot 1
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y1")

# Subplot 2
plt.subplot(1, 2, 2)
plt.scatter(x, y2)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y2")

plt.tight_layout()
plt.show()
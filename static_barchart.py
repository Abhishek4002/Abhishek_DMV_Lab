import matplotlib.pyplot as plt

# Data
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [25, 40, 30, 10]
colors = ['red', 'yellow', 'pink', 'brown']

# Create bar chart
plt.figure(figsize=(8,5))
plt.bar(categories, values, color=colors, edgecolor='black')

# Add title and labels
plt.title("Static Bar Chart Example")
plt.xlabel("Fruits")
plt.ylabel("Quantity")

plt.show()

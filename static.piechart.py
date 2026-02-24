import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Make it a perfect circle
plt.axis('equal')

plt.title("Programming Language Popularity")
plt.show()

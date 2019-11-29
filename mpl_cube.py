import matplotlib.pyplot as plt

x_cubes = list(range(1,5001))
y_cubes = [x**3 for x in x_cubes]
plt.scatter(x_cubes, y_cubes, c=y_cubes, cmap=plt.cm.Reds, edgecolor='none', linewidth=5)

plt.title("Cube Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube or Value", fontsize=14)


plt.show()
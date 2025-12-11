import matplotlib.pyplot as plt


x = [1, 1, 5, 5, 1]  
y = [1, 5, 5, 1, 1]


plt.figure(figsize=(8, 8), dpi=100)


plt.plot(x, y, 'b-', linewidth=3, label='Квадрат')
plt.scatter(x[:-1], y[:-1], color='red', s=100, zorder=5)


points = [(1, 1), (1, 5), (5, 5), (5, 1)]
labels = ['(1,1)', '(1,5)', '(5,5)', '(5,1)']
for (px, py), label in zip(points, labels):
    plt.text(px + 0.15, py + 0.15, label, fontsize=12, fontweight='bold')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.gca().set_aspect('equal', adjustable='box')

plt.legend(loc='upper left', fontsize=11)

plt.savefig('square.png')
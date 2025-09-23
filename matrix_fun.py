import matplotlib.pyplot as plt
import numpy as np

matrix_A = [
    [1, 0, -1, 0, 0],
    [0, 1, 0, -1, 0],
    [0, 0, 1, 0, -1],
    [-1, 0, 0, 1, 0]
]
matrix_B = [
    [0.5, 0.1, 0.3, 0.2],
    [0.2, 0.4, 0.1, 0.3],
    [0.3, 0.2, 0.4, 0.1],
    [0.1, 0.3, 0.2, 0.4],
    [0.4, 0.3, 0.1, 0.2]
]

# Compute AB
matrix_AB = []
for row_index in range(len(matrix_A)):
    new_row = []
    for col_index in range(len(matrix_B[0])):
        dot_product = sum(matrix_A[row_index][k] * matrix_B[k][col_index] for k in range(len(matrix_B)))
        new_row.append(dot_product)
    matrix_AB.append(new_row)

# Convert to numpy array
Z = np.array(matrix_AB)

# Create X and Y coordinates for 3D plot
X, Y = np.meshgrid(np.arange(Z.shape[1]), np.arange(Z.shape[0]))

# Create figure with 2 subplots
fig = plt.figure(figsize=(12, 5))

# ---- Heatmap ----
ax1 = fig.add_subplot(1, 2, 1)
heatmap = ax1.imshow(Z, cmap='viridis', interpolation='nearest')
fig.colorbar(heatmap, ax=ax1, label='Value')
ax1.set_title('Heatmap of Matrix AB')
ax1.set_xlabel('Column Index')
ax1.set_ylabel('Row Index')

# ---- 3D Surface ----
from mpl_toolkits.mplot3d import Axes3D
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k')
ax2.set_title('3D Surface Plot of Matrix AB')
ax2.set_xlabel('Column Index')
ax2.set_ylabel('Row Index')
ax2.set_zlabel('Value')

plt.tight_layout()
plt.show()

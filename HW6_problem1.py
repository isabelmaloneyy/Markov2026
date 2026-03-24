import numpy as np
import matplotlib.pyplot as plt

p = np.array([[0, 1, 0, 0, 0],
              [1/3, 0, 2/3, 0, 0],
              [0, 1/2, 0, 1/2, 0],
              [0, 0, 2/3, 0, 1/3],
              [0, 0, 0, 1, 0]])

q0 = np.array([0, 0, 1, 0, 0])

p50 = np.linalg.matrix_power(p, 50)
q50 = q0 @ p50
print("q_50 =", q50)

pi = np.array([1/12, 1/4, 1/3, 1/4, 1/12])

x = np.arange(5)

plt.plot(x, q50, marker='o', label='$q_{50}$')
plt.plot(x, pi, marker='o', label='$\pi$')
plt.xlabel('State')
plt.ylabel('Probability')
plt.xticks(x)
plt.title('$q_{50}$ vs Stationary Distribution')
plt.legend()
plt.show()

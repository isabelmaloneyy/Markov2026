import numpy as np
import matplotlib.pyplot as plt
import random

# b) Finding theoretical stationary distribution numerically

K = 0.1
a = 0.04
b = 0.16

p = np.array([[1-K*np.exp(a*1), K*np.exp(a*1), 0, 0, 0],
             [K*np.exp(b*1), 1-K*np.exp(b*1)-K*np.exp(a*2), K*np.exp(a*2), 0, 0],
             [0, K*np.exp(b*2), 1-K*np.exp(b*2)-K*np.exp(a*3), K*np.exp(a*3), 0],
             [0, 0, K*np.exp(b*3), 1-K*np.exp(b*3)-K*np.exp(a*4), K*np.exp(a*4)],
             [0, 0, 0, K*np.exp(b*4), 1-K*np.exp(b*4)]])

eigenvalues, eigenvectors = np.linalg.eig(p.T)

# Find eigenvalue closest to 1 qnd get corresponding eigenvector
idx = np.isclose(eigenvalues, 1)
stationary_vec = eigenvectors[:, idx][:, 0].real

# Normalize the vector 
pi = stationary_vec/stationary_vec.sum()

print(pi)

# c) Simulating the Markov chain

start = 1
n = 1000000
states = [start]
for _ in range(n):
    current_state = states[-1]
    next_state = np.random.choice(5, p=p[current_state])
    states.append(next_state)

dist = np.bincount(states) / len(states)
print(dist)

plt.hist(states, bins=np.arange(-0.5, 5.5, 1), density=True, alpha=0.6, color='blue', edgecolor='black')
plt.title('Simulated Stationary Distribution')
plt.xlabel('State')
plt.ylabel('Probability')
plt.xticks(range(5), labels=['1', '2', '3', '4', '5'])

# d) Theoretical and simulated values plot

# Theoretical values from part a
denom = np.sum([np.exp((a-b)*i*(i-1)/2) for i in range(1, 6)])
stationary_dist = np.array([np.exp((a-b)*i*(i-1)/2) / denom for i in range(1, 6)])

plt.bar(np.arange(5)-0.3, stationary_dist,  color='green', label='Theoretical (part a)', width=0.3)
plt.bar(np.arange(5), pi, color='red', label='Theoretical (part b)', width=0.3)
plt.bar(np.arange(5)+0.3, dist, color='blue', label='Simulated', width=0.3)
plt.title('Theoretical vs Simulated Stationary Distribution')
plt.xlabel('State')
plt.ylabel('Probability')
plt.xticks(range(5), labels=['1', '2', '3', '4', '5'])
plt.legend()

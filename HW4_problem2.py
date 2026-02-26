import numpy as np
from scipy.stats import binom

# Part a: Calculating the transition probabilities

# Calculate the PMF
p_55 = binom.pmf(5, 5, 0.9)
p_54 = binom.pmf(4, 5, 0.9)
p_53 = binom.pmf(3, 5, 0.9)
p_52 = binom.pmf(2, 5, 0.9)
p_51 = binom.pmf(1, 5, 0.9)
p_50 = binom.pmf(0, 5, 0.9)

print("Transition probabilities from state 5:")
print(f"To state 5: {p_55:.4f}")
print(f"To state 4: {p_54:.4f}")
print(f"To state 3: {p_53:.4f}")
print(f"To state 2: {p_52:.4f}")
print(f"To state 1: {p_51:.4f}")
print(f"To state 0: {p_50:.5f}")

p_44 = binom.pmf(4, 4, 0.9)
p_43 = binom.pmf(3, 4, 0.9)
p_42 = binom.pmf(2, 4, 0.9)
p_41 = binom.pmf(1, 4, 0.9)
p_40 = binom.pmf(0, 4, 0.9)

print("\nTransition probabilities from state 4:")
print(f"To state 4: {p_44:.4f}")
print(f"To state 3: {p_43:.4f}")
print(f"To state 2: {p_42:.4f}")
print(f"To state 1: {p_41:.4f}")
print(f"To state 0: {p_40:.4f}")    

p_33 = binom.pmf(3, 3, 0.9)
p_32 = binom.pmf(2, 3, 0.9)
p_31 = binom.pmf(1, 3, 0.9)
p_30 = binom.pmf(0, 3, 0.9)

print("\nTransition probabilities from state 3:")
print(f"To state 3: {p_33:.4f}")
print(f"To state 2: {p_32:.4f}")
print(f"To state 1: {p_31:.4f}")
print(f"To state 0: {p_30:.4f}")

p_22 = binom.pmf(2, 2, 0.9)
p_21 = binom.pmf(1, 2, 0.9)
p_20 = binom.pmf(0, 2, 0.9)

print("\nTransition probabilities from state 2:")
print(f"To state 2: {p_22:.4f}")
print(f"To state 1: {p_21:.4f}")
print(f"To state 0: {p_20:.4f}")

p_11 = binom.pmf(1, 1, 0.9)
p_10 = binom.pmf(0, 1, 0.9)

print("\nTransition probabilities from state 1:")
print(f"To state 1: {p_11:.4f}")
print(f"To state 0: {p_10:.4f}")

# Part b: Time until all machines fail

A = np.array([[1, 0, 0, 0, 0, 0],
              [p_10, p_11-1, 0, 0, 0, 0],
                [p_20, p_21, p_22-1, 0, 0, 0],
                [p_30, p_31, p_32, p_33-1, 0, 0],
                [p_40, p_41, p_42, p_43, p_44-1, 0],
                [p_50, p_51, p_52, p_53, p_54, p_55-1]])
b = np.array([0, -1, -1, -1, -1, -1])
expected_times = np.linalg.solve(A, b)
print("\nExpected time until all machines fail from each state:")
for i in range(6):
    print(f"State {i}: {expected_times[i]:.4f} weeks")

# Part c: Stationary distribution

p = np.array([[0,0,0,0,0,1],
              [p_10, p_11, 0, 0, 0, 0],
                [p_20, p_21, p_22, 0, 0, 0],
                [p_30, p_31, p_32, p_33, 0, 0],
                [p_40, p_41, p_42, p_43, p_44, 0],
                [p_50, p_51, p_52, p_53, p_54, p_55]])

eigenvalues, eigenvectors = np.linalg.eig(p.T)

# Find eigenvalue closest to 1 qnd get corresponding eigenvector
idx = np.isclose(eigenvalues, 1)
stationary_vec = eigenvectors[:, idx][:, 0].real

# Normalize the vector 
pi = stationary_vec/stationary_vec.sum()

print(pi)

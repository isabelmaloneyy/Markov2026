from sympy import var, Matrix, solve, symbols

# b) Find the eigenvalues and eigenvectors of the transition matrix P.
a = var('a')

p = Matrix([[1-a, a, 0],
            [a, 0, 1-a],
            [0, 1-a, a]])

p_trans = p.T
eigenvals = p.eigenvals()
eigenvectors = p.eigenvects()

print("Eigenvalues:", eigenvals)
print("Eigenvectors:", eigenvectors)

# c) Compute q_n = A^n q0 for n = 0, 1, 2, ... and show that it converges to the stationary distribution π as n → ∞.
import numpy as np

a = 0.99

# transition matrix
P = np.array([
    [1-a, a, 0],
    [a, 0, 1-a],
    [0, 1-a, a]
])

A = P.T

# eigen decomposition
eigvals, eigvecs = np.linalg.eig(A)

q0 = np.array([1,0,0])

# solve for coefficients in eigenvector basis
c = np.linalg.solve(eigvecs, q0)
print(c)

# d) Plot the simulated fraction of chains in state 1 as a function of n for N = 100, 1000, and 10000, along with the theoretical expression for q_n[0] (the first component of q_n) on the same plot
import matplotlib.pyplot as plt

steps = 300

def simulate_chains(N, steps):

    states = np.ones(N, dtype=int) 
    fn = []

    for n in range(steps+1):

        fn.append(np.mean(states == 1))

        new_states = states.copy()

        for i in range(N):
            s = states[i] - 1
            new_states[i] = np.random.choice([1,2,3], p=P[s])

        states = new_states

    return np.array(fn)

# run simulations
fn_100 = simulate_chains(100, steps)
fn_1000 = simulate_chains(1000, steps)
fn_10000 = simulate_chains(10000, steps)

# theoretical expression
n = np.arange(steps+1)
qn1 = c[0] + c[1]*(-0.01)**n + c[2]*(-0.99)**n

# plot
plt.figure(figsize=(8,5))

plt.plot(n, fn_100, label="N=100")
plt.plot(n, fn_1000, label="N=1000")
plt.plot(n, fn_10000, label="N=10000")
plt.plot(n, qn1, linewidth=3, label="Theory", alpha=0.5)

plt.xlabel("n")
plt.ylabel("Probability state 1")
plt.title("Convergence to stationary distribution")
plt.legend()
plt.show()

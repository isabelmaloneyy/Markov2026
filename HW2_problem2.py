# Part b

import numpy as np
import time

def newton_method(u, tol=1e-10, maxiter=50):
    x = 1.0  # initial guess
    for _ in range(maxiter):
        fx = 1 - (x + 1) * np.exp(-x) - u
        df = x * np.exp(-x)
        x_new = x - fx / df
        if abs(x_new - x) < tol:
            return max(x_new, 0.0)
        x = max(x_new, 0.0)
    return x

# Sampling
N = 10**6
U = np.random.rand(N)

start = time.time()
samples_1 = np.array([newton_method(u) for u in U])
end = time.time()

print("Inverse sampling runtime:", end - start, "seconds")

# Part c

start = time.time()

samples_2 = []
while len(samples_2) < N:
    Y = np.random.exponential(scale=2)     # g(x)
    U = np.random.rand()
    if U <= (Y * np.exp(-Y)) / ((4/np.e) * 0.5 * np.exp(-Y/2)):
        samples_2.append(Y)

samples_2 = np.array(samples_2)
end = time.time()

print("Acceptance-rejection runtime:", end - start, "seconds")

# Part d

start = time.time()

E1 = np.random.exponential(scale=1, size=N)
E2 = np.random.exponential(scale=1, size=N)
samples_3 = E1 + E2

end = time.time()

print("Sum of exponentials runtime:", end - start, "seconds")

# Part e : Histogram

x = np.linspace(0, 10, 500)
pdf = x * np.exp(-x)

plt.hist(samples_1,bins=100,density=True,alpha=0.7, label=f"Histogram (N = {N})")
plt.plot(x, pdf, linewidth=2, label="Theoretical PDF")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.title(f"Inverse Sampling Method")
plt.xlim(-1, 10)
plt.legend();
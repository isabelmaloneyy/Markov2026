import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(u):
    return u**4 / (1 + u**6)

ref, _ = integrate.quad(f, 0, 1)

x_vals = np.arange(1.0, 5.01, 0.1)
N_vals = np.floor(10**x_vals).astype(int)

rng = np.random.default_rng(68)
E_vals = []

for N in N_vals:
    u = rng.random(N)
    v = rng.random(N)
    E_vals.append(np.mean(v <= f(u)))

E_vals = np.array(E_vals)

plt.figure(figsize=(7,5))
plt.plot(N_vals, E_vals, marker='o', linestyle='-', label='Monte Carlo estimate (E(N))')
plt.axhline(ref, linestyle='--', color='k', label='Reference value')
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('Integral Value')
plt.title(r'Monte Carlo estimation of $\int_0^1 \frac{u^4}{1+u^6}  du$')
plt.legend()
plt.show()

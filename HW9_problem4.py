import numpy as np
import matplotlib.pyplot as plt

beta = 1.0
m_vals = np.arange(2, 200)

tau = np.array([np.sum(1/np.arange(1, m)) for m in m_vals]) / beta
tau_deterministic = np.log(m_vals) / beta

plt.figure()
plt.plot(m_vals, tau, label="$E[\\tau_m]$")
plt.plot(m_vals, tau_deterministic, linestyle='--', label="Deterministic $\\tau_m$")

plt.xlabel("m")
plt.ylabel("Time to reach m")
plt.legend()

plt.show()

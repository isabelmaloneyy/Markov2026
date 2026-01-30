import numpy as np
import matplotlib.pyplot as plt

# Parameters
gamma = 4
x0 = 10
Ns = [100, 1000, 10000]

# Inverse CDF sampler
def sample_power_law(N, gamma, x0):
    U = np.random.rand(N)
    return x0 * (1 - U)**(-1 / (gamma - 1))

# Theoretical PDF
x = np.linspace(x0, 60, 500)
C = (gamma - 1) * x0**(gamma - 1)
pdf = C * x**(-gamma)

# Generate histograms and plots
for N in Ns:
    samples = sample_power_law(N, gamma, x0)

    plt.figure()
    plt.hist(
        samples,
        bins=30,
        density=True,      # normalize to area = 1
        range=(0, 60),
        alpha=0.7
    )
    plt.plot(x, pdf, linewidth=2)
    plt.xlim(0, 60)
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.title(f"Power-law distribution (N = {N})")
    plt.show()

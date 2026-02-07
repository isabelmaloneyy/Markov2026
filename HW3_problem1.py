# Plot for Part d

def f(x):
    return (1/3) * x * (1 + x) * np.exp(-x)

def g(x, a):
    return a**2 * x * np.exp(-a * x)

a_star = np.sqrt(3) - 1

c_star = np.exp(-a_star) / (3 * a_star**2 * (1 - a_star))

x = np.linspace(0, 12, 1000)

plt.plot(x, f(x), label="$f(x)$", linewidth=2)
plt.plot(x, c_star * g(x, a_star), linestyle="--", label="$c(a^*) g_{a^*}(x)$", linewidth=2)
plt.xlabel("x")
plt.ylabel("Density")
plt.title("Acceptance-Rejection")
plt.legend();

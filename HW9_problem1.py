import numpy as np

def simulate_delivery_time(L, alpha, beta):
    i = 0          
    t = 0

    while i != L:
        if i == 0:
            wait = np.random.exponential(1 / alpha)
            t += wait
            i = 1
        else:
            rate = alpha + beta
            wait = np.random.exponential(1 / rate)
            t += wait

            if np.random.rand() < alpha / rate:
                i += 1
            else:
                i -= 1
    return t


def run_simulation(N, L, alpha, beta):
    times = np.zeros(N)

    for k in range(N):
        times[k] = simulate_delivery_time(L, alpha, beta)

    mean_time = np.mean(times)
    var_time = np.var(times)

    return mean_time, var_time


L = 20
alpha = 1
beta = 1
N = 1000

mean_time, var_time = run_simulation(N, L, alpha, beta)

theoretical = L*(L+1)/(2*alpha)

print(f"Simulated mean delivery time: {mean_time:.2f}")
print(f"Theoretical mean delivery time: {theoretical:.2f}")
print(f"Simulated variance: {var_time:.2f}")

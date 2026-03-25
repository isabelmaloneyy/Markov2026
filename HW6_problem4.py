import numpy as np

# b)
np.random.seed(0)

def avalanche_sim(a, max_gen=200):
    X = 1 
    for _ in range(max_gen):
        if X == 0:
            return 1 
        else:
            Z = np.random.binomial(X, 1 - a)
            X = 2 * Z
    return 0

# Run simulation
a = 0.49
results = [avalanche_sim(a) for _ in range(1000)]

print("Experimental extinction probability:", np.mean(results))

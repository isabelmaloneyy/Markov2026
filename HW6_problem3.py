import numpy as np
from scipy.optimize import fsolve

# c)
f = lambda x: np.exp(2*(x-1)) - x

x_initial = 0.5
x_solution = fsolve(f, x_initial)[0]

print(x_solution)

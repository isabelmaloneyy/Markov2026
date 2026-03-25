import scipy as sp
import numpy as np

# b)

f = lambda t: 1 - (1-np.exp(-1/30*t)*(1+1/30*t))*(1-np.exp(-1/20*t)*(1+1/20*t))
sp.integrate.quad(f, 0, np.inf)

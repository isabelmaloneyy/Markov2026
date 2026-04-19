# Problem 1
## a)

import numpy as np

Q = np.array([[-1, 1, 0, 0], 
              [0, -1, 1, 0], 
              [0, 0, -1, 1], 
              [1, 0, 0, -1]])

eigenvalues = np.linalg.eigvals(Q)
print("Eigenvalues of Q:", eigenvalues)

## e)

import matplotlib.pyplot as plt

# Theoretical solution
from scipy.integrate import solve_ivp

def master_equations(t, y):
    dydt = Q.T @ y
    return dydt

y0 = np.array([1/3, 2/3, 0, 0])  
t_span = (0, 10)
solution = solve_ivp(master_equations, t_span, y0, t_eval=np.linspace(0, 10, 100))

y1_solution = solution.y[0]  
t = solution.t

# Simulate the Markov chain
def simulate_chain(t_grid, initial_state):
    t = 0
    state = initial_state
    states = np.zeros(len(t_grid), dtype=int)
    
    i = 0
    while i < len(t_grid):
        wait = np.random.exponential(1.0)
        t_next = t + wait
        
        while i < len(t_grid) and t_grid[i] < t_next:
            states[i] = state
            i += 1
        
        state = (state % 4) + 1  
        t = t_next
    
    return states


def run_simulation(N, t_grid):
    counts = np.zeros(len(t_grid))
    
    for _ in range(N):
        initial_state = 1 if np.random.rand() < 1/3 else 2
        
        states = simulate_chain(t_grid, initial_state)
        
        counts += (states == 1)
    
    return counts / N

t_grid = np.linspace(0, 5, 200)

Ns = [100, 1000, 10000, 100000]

plt.figure(figsize=(10,6))

# Plot theoretical solution
plt.plot(t, y1_solution, 'k', linewidth=2, label='Theory')

# Plot simulations
for N in Ns:
    f_t = run_simulation(N, t_grid)
    plt.plot(t_grid, f_t, label=f'N={N}', alpha=0.7)

plt.xlim(0, 5)
plt.ylim(0, 0.5)

plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.title('Fraction of time in state 1 at time t')

plt.show()

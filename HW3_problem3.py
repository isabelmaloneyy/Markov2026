# Part e

p = [[9/10, 1/10, 0],
    [0, 7/8, 1/8],
    [2/5, 0, 3/5]]

p_50 = np.array(p)

np.linalg.matrix_power(p_50, 50)

# Part f: Simulating the Markov chain 

current_state = 0  # Start with G
path = [current_state]

# Run simulation
for _ in range(10000):
    next_state = np.random.choice([0, 1, 2], p=p_50[current_state])
    path.append(next_state)
    current_state = next_state

count_G = path.count(0)
count_G/len(path)

import numpy as np

# Part b

p = np.array([[1/2, 1/2, 0, 0, 0, 0],
                [0, 1/2, 1/2, 0, 0, 0],
                [1/3, 0, 1/3, 1/3, 0, 0],
                [0, 0, 0, 1/2, 1/2, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0]])

p_5 = np.linalg.matrix_power(p, 5)
p_5[0,3]

# Part c

X5 = []

# Run simulation
for _ in range(10000):
    current_state = 0  

    for _ in range(5):
        next_state = np.random.choice([0, 1, 2, 3, 4, 5], p=p[current_state])
        current_state = next_state
    X5.append(current_state)

count_G = X5.count(3)
count_G/len(X5)


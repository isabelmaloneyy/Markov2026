import random
import numpy as np

p = 0.35
q = 0.40
s = 0.25
i = 10
N = 100000

final_money = []

for _ in range(N):
    money = i
    while money > 0:
        r = random.random()
        if r < p:
            money += 1
        elif r < p + q:
            money -= 1
        else:
            final_money.append(money)
            break
    final_money.append(money)

simulated_mean = np.mean(final_money)
print("Simulated expected value:", simulated_mean)

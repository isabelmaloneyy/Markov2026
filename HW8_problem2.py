import sympy as sp
import numpy as np

lambda_n = sp.symbols('lambda_n')
lambda_d = sp.symbols('lambda_d')
mu_n = sp.symbols('mu_n')
mu_d = sp.symbols('mu_d')

eq1 = sp.Eq(- (lambda_n + lambda_d) * sp.symbols('P1') + mu_n * sp.symbols('P2') + mu_d * sp.symbols('P3'), 0)
eq2 = sp.Eq(lambda_n * sp.symbols('P1') - mu_n * sp.symbols('P2'), 0)
eq3 = sp.Eq(lambda_d * sp.symbols('P1') - mu_d * sp.symbols('P3'), 0)
solution = sp.solve((eq1, eq2, eq3), (sp.symbols('P1'), sp.symbols('P2'), sp.symbols('P3')))

print("Stationary distribution:")
print(solution)

Q_trans = np.array([[-2, 1, 1],
                     [1, -1, 0],
                     [1, 0, -1]])

eigenvalues, eigenvectors = np.linalg.eig(Q_trans)
print("Eigenvalues of Q^T:")
print(eigenvalues)

import numpy as np

v = np.array([3, 4])
print(np.linalg.norm(v))      # L2 norm = 5.0  (√(9+16))
print(np.linalg.norm(v, 1))   # L1 norm = 7.0  (3+4)
# Ridge regression penalizes L2 norm, Lasso penalizes L1 norm
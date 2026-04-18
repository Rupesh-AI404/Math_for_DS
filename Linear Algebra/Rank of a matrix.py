import numpy as np

X = np.array([[1, 2, 3],
              [2, 4, 6],
              [0, 1, 0]])

print(np.linalg.matrix_rank(X))  # 2, not 3, because row 2 is a multiple of row 1
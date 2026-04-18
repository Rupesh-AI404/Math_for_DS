from numpy.linalg import norm
import numpy as np

a = np.array([1, 2, 3])   # user A's ratings
b = np.array([2, 4, 6])   # user B's ratings

similarity = np.dot(a, b) / (norm(a) * norm(b))
print(similarity)   # 1.0 → perfectly similar direction
# This is how Netflix finds "users like you"
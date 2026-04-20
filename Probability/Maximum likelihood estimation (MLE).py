import numpy as np
from scipy.optimize import minimize_scalar

# Simplest MLE: find the p that maximizes likelihood of our coin data
k, n = 8, 10

def neg_log_likelihood(p):
    # Log avoids tiny floating point numbers; minimize negative = maximize
    return -(k * np.log(p) + (n-k) * np.log(1-p))

result = minimize_scalar(neg_log_likelihood, bounds=(0.01, 0.99), method='bounded')
print(f"MLE estimate of p = {result.x:.2f}")   # 0.80
# The MLE answer is always k/n = 8/10 = 0.80
# sklearn does the same thing for every parameter it learns